import random

class Thermocouple:
    """
    Driver per la termocoppia.
    Non mantiene stato, legge solo il valore.
    """
    def __init__(self, channel: int, state, start_temp: float = 20.0):
        self.channel = channel
        self.state = state # TODO: Remove
        self._current_temp = start_temp

    def read_temp(self) -> float:
        target = self.state.get_target()
        delta = target - self._current_temp

        # Scegli quanto velocemente la temperatura cambia
        step = 2.0  # °C per ciclo max
        if abs(delta) > 0.5:
            self._current_temp += step * (1 if delta > 0 else -1)

        # Piccola variazione casuale per renderla meno "perfetta"
        self._current_temp += random.uniform(-0.2, 0.2)

        return round(self._current_temp, 1)
