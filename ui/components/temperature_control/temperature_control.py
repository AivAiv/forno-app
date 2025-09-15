from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, StringProperty, ColorProperty
from kivy.clock import Clock
from kivy.core.window import Window

class TemperatureControl(BoxLayout):
    value = NumericProperty(0)
    trail = StringProperty("%")
    step = NumericProperty(1)
    text_color = ColorProperty([1, 1, 1, 1])  # colore testo iniziale (bianco)

    _inc_event = None
    _dec_event = None
    _speed = 0.15
    _boost_event = None
    _boost_delay = 2.0
    _original_step = 1
    _original_color = [1, 1, 1, 1]  # bianco

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_mouse_up=self._global_mouse_up)

    def increment_once(self, dt=None):
        if self.value < 100:
            self.value += self.step
            if self.value > 100:
                self.value = 100

    def decrement_once(self, dt=None):
        if self.value > 0:
            self.value -= self.step
            if self.value < 0:
                self.value = 0

    def _enable_boost(self, dt):
        self.step = 10
        self.text_color = [1, 1, 0, 1]  # giallo

    def start_increment(self):
        self._original_step = self.step
        self._original_color = self.text_color
        self.increment_once()
        self._inc_event = Clock.schedule_interval(self.increment_once, self._speed)
        self._boost_event = Clock.schedule_once(self._enable_boost, self._boost_delay)

    def stop_increment(self):
        if self._inc_event:
            self._inc_event.cancel()
            self._inc_event = None
        if self._boost_event:
            self._boost_event.cancel()
            self._boost_event = None
        self.step = self._original_step
        self.text_color = self._original_color

    def start_decrement(self):
        self._original_step = self.step
        self._original_color = self.text_color
        self.decrement_once()
        self._dec_event = Clock.schedule_interval(self.decrement_once, self._speed)
        self._boost_event = Clock.schedule_once(self._enable_boost, self._boost_delay)

    def stop_decrement(self):
        if self._dec_event:
            self._dec_event.cancel()
            self._dec_event = None
        if self._boost_event:
            self._boost_event.cancel()
            self._boost_event = None
        self.step = self._original_step
        self.text_color = self._original_color

    def _global_mouse_up(self, *args):
        self.stop_increment()
        self.stop_decrement()
