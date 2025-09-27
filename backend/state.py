# backend/state.py
from threading import Lock

class SystemState:
    def __init__(self):
        self._lock = Lock()
        self._current_temp = 0.0
        self._target_temp = 0.0
        self._heater_on = False
        self._is_on = False

        self.light = False
        self.aspiration = False
    
    def start_hoven(self, is_on):
        with self._lock:
            self._is_on = is_on

    def is_hoven_on(self):
        with self._lock:
            return self._is_on

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

    def set_heater(self, status: bool):
        with self._lock:
            self._heater_on = status

    def get_heater(self):
        with self._lock:
            return self._heater_on
    
    def set_light(self, light):
        with self._lock:
            self.light = light

    def get_light(self):
        with self._lock:
            return self.light
    