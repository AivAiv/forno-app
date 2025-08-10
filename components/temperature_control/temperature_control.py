from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, StringProperty
from kivy.clock import Clock

class TemperatureControl(BoxLayout):
    value = NumericProperty(0)
    trail = StringProperty("%")
    step = NumericProperty(1)

    _inc_event = None
    _dec_event = None
    _speed = 0.15  # velocità iniziale (in secondi) quando si tiene premuto

    def increment_once(self, dt=None):
        """Aumenta di uno step singolo."""
        if self.value < 100:
            self.value += self.step

    def decrement_once(self, dt=None):
        """Diminuisce di uno step singolo."""
        if self.value > 0:
            self.value -= self.step

    def start_increment(self):
        """Chiamato quando il pulsante ↑ viene premuto."""
        self.increment_once()  # primo incremento immediato
        self._inc_event = Clock.schedule_interval(self.increment_once, self._speed)

    def stop_increment(self):
        """Chiamato quando il pulsante ↑ viene rilasciato."""
        if self._inc_event:
            self._inc_event.cancel()
            self._inc_event = None

    def start_decrement(self):
        """Chiamato quando il pulsante ↓ viene premuto."""
        self.decrement_once()
        self._dec_event = Clock.schedule_interval(self.decrement_once, self._speed)

    def stop_decrement(self):
        """Chiamato quando il pulsante ↓ viene rilasciato."""
        if self._dec_event:
            self._dec_event.cancel()
            self._dec_event = None
