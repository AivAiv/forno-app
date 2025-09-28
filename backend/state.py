# backend/state.py
from threading import Lock

class SystemState:
    def __init__(self):
        self._lock = Lock()
        self._is_on = False

        # Heating
        self._current_temp = 0.0
        self._target_temp = 0.0
        self._top_heater_perc = 100
        self._bottom_heater_perc = 100
        self._top_heater_on = False
        self._bottom_heater_on = False

        # Instrumentation
        self._light = False
        self._aspiration = False
    
    def start_hoven(self, is_on):
        with self._lock:
            self._is_on = is_on

    def is_hoven_on(self):
        with self._lock:
            return self._is_on
    
    # Heating
    def set_target(self, temp):
        with self._lock:
            self._target_temp = temp

    def get_target(self):
        with self._lock:
            return self._target_temp

    def update_temp(self, temp):
        with self._lock:
            self._current_temp = temp

    def get_temp(self):
        with self._lock:
            return self._current_temp
    
    def set_top_heater_perc(self, temp_perc: int):
        with self._lock:
            self._top_heater_perc = temp_perc

    def get_top_heater_perc(self):
        with self._lock:
            return self._top_heater_perc
        
    def set_bottom_heater_perc(self, temp_perc: int):
        with self._lock:
            self._bottom_heater_perc = temp_perc

    def get_bottom_heater_perc(self):
        with self._lock:
            return self._bottom_heater_perc

    def set_top_heater_on(self, status: bool):
        with self._lock:
            self._top_heater_on = status

    def is_top_heater_on(self):
        with self._lock:
            return self._top_heater_on
    
    def set_bottom_heater_on(self, status: bool):
        with self._lock:
            self._bottom_heater_on = status

    def is_bottom_heater_on(self):
        with self._lock:
            return self._bottom_heater_on
    
    # Instrumentation
    def set_light(self, light):
        with self._lock:
            self._light = light

    def get_light(self):
        with self._lock:
            return self._light
    
    def print_state(self):
        print(f"[STATE] --- CURRENT STATE ---")
        print(f"[STATE] Hoven running: {self.is_hoven_on()}")
        print(f"[STATE] Light on: {self.get_light()}")
        print(f"[STATE] --- Heating ---")
        print(f"[STATE] Heat target: {self.get_target()}")
        print(f"[STATE] Current temp: {self.get_temp()}")
        print(f"[STATE] Top heater perc: {self.get_top_heater_perc()}")
        print(f"[STATE] Bottom heater perc: {self.get_bottom_heater_perc()}")
        print(f"[STATE] Top heater on: {self.is_top_heater_on()}")
        print(f"[STATE] Bottom heater on: {self.is_bottom_heater_on()}")
        print(f" ")
    