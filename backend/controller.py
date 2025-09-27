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
        self.heater = Heater(pin=17)
        self.thermo = Thermocouple(channel=0, state=self.state)

        self.reset_hoven()

        # Internal variables
        self.last_light_state = False
        self.last_heater_state = False
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

            # Temperature read
            temp = self.thermo.read_temp()
            self.state.update_temp(temp)

            # Heater control
            if temp < self.state.get_target():
                if self.state.get_heater() != True:
                    self.heater.on()
                    self.state.set_heater(True)
            else:
                if self.state.get_heater() != False:
                    self.heater.off()
                    self.state.set_heater(False)
            

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
        self.heater.off()
