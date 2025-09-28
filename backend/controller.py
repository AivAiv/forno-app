# backend/controller.py
import time
import threading
from hardware.thermocouple import Thermocouple
from hardware.heater import Heater
from hardware.light import Light

class Controller(threading.Thread):
    def __init__(self, state):
        super().__init__(daemon=True)
        self.state = state
        self.light = Light(pin=27)
        self.top_heater = Heater(pin=17)
        self.bottom_heater = Heater(pin=18)
        self.thermo = Thermocouple(channel=0, state=self.state)

        self.reset_hoven()

        # Working variables
        self.last_light_state = False
        self.last_top_heater_state = False
        self.last_bottom_heater_state = False
        self.last_hoven_state = False

    def run(self):
        while True:
            if self.state.is_hoven_on() == False:
                if self.last_hoven_state != False:
                    # Turn OFF
                    self.reset_hoven()
                    self.last_hoven_state = False
                    print(f"[CONTROLLER] Hoven OFF")
                continue

            self.state.print_state()

            # Temperature read
            temp = self.thermo.read_temp()
            self.state.update_temp(temp)

            # Heater control
            if temp < self.state.get_target():
                if self.state.is_top_heater_on() != True:
                    self.top_heater.on()
                    self.bottom_heater.on()
                    self.state.set_top_heater_on(True)
                    self.state.set_bottom_heater_on(True)
            else:
                if self.state.is_top_heater_on() != False:
                    self.top_heater.off()
                    self.bottom_heater.off()
                    self.state.set_top_heater_on(False)
                    self.state.set_bottom_heater_on(False)

            # Light control
            if self.state.get_light() != self.last_light_state:
                if self.state.get_light():
                    self.light.on()
                    self.last_light_state = True
                else:
                    self.light.off()
                    self.last_light_state = False

            time.sleep(1)
    
    def reset_hoven(self):
        self.light.off()
        self.top_heater.off()
        self.bottom_heater.off()
