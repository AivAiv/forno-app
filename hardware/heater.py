try:
    import RPi.GPIO as GPIO
except ImportError:
    # mock per sviluppo su PC
    class GPIO:
        BCM = OUT = None
        @staticmethod
        def setmode(x): pass
        @staticmethod
        def setup(pin, mode): pass
        @staticmethod
        def output(pin, val): pass
        @staticmethod
        def cleanup(): pass


class Heater:
    """
    Driver per la resistenza (stateless).
    """
    def __init__(self, pin: int):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.off()

    def on(self):
        GPIO.output(self.pin, True)
        print(f"[HARDWARE] Heater pin {self.pin} -> {True}")

    def off(self):
        GPIO.output(self.pin, False)
        print(f"[HARDWARE] Heater pin {self.pin} -> {False}")

    def reach_temperature(self, temperature):
        GPIO.output(self.pin, True)
        print(f"[HARDWARE] Heater pin {self.pin} -> {True}")