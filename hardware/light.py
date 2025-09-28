try:
    import RPi.GPIO as GPIO
except ImportError:
    # mock per sviluppare su PC
    class GPIO:
        BCM = BOARD = OUT = None
        @staticmethod
        def setmode(x): pass
        @staticmethod
        def setup(pin, mode): print(f"[HARDWARE] Light fake GPIO on")
        @staticmethod
        def output(pin, val): pass
        @staticmethod
        def cleanup(): pass


class Light:
    """
    Driver per la luce del forno.
    """
    def __init__(self, pin: int):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.off()

    def on(self):
        GPIO.output(self.pin, True)
        print(f"[HARDWARE] Light pin {self.pin} -> {True}")

    def off(self):
        GPIO.output(self.pin, False)
        print(f"[HARDWARE] Light pin {self.pin} -> {False}")

    def toggle(self, current_state: bool) -> bool:
        if current_state:
            self.off()
            return False
        else:
            self.on()
            return True