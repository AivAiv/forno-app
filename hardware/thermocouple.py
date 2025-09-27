import random

class Thermocouple:
    """
    Driver per la termocoppia.
    Non mantiene stato, legge solo il valore.
    """
    def __init__(self, channel: int):
        self.channel = channel
        # Qui puoi inizializzare la libreria hardware reale
        # es. import adafruit_max31855...

    def read_temp(self) -> float:
        # MOCK: restituisce una temperatura finta
        return 20 + random.random() * 500
