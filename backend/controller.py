# backend/controller.py
import time
import threading
from hardware.thermocouple import get_temperature
from hardware.heater import set_heater
from hardware.light import Light

class Controller(threading.Thread):
    def __init__(self, state):
        super().__init__(daemon=True)
        self.state = state
        self.light = Light(pin=27)

    def run(self):
        while True:
            temp = get_temperature()
            self.state.update_temp(temp)

            # controllo semplice on/off
            if temp < self.state.get_target():
                set_heater(True)
                self.state.set_heater(True)
            else:
                set_heater(False)
                self.state.set_heater(False)
            

            # Accensione/spegnimento luce
            if self.state.get_light():
                self.light.on()
            else:
                self.light.off()

            time.sleep(1)
