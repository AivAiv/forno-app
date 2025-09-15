from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.text import LabelBase

# Import schermate
from ui.components.clickableimage.clickableimage import ClickableImage
from ui.components.temperature_control.temperature_control import TemperatureControl
from ui.pages.standby.standby import StandbyScreen
from ui.pages.home.home import HomeScreen

class MyScreenManager(ScreenManager):
    pass

class MyApp(App):
    def __init__(self, state, **kwargs):
        super().__init__(**kwargs)
        self.state = state

    def build(self):
        # Carico i .kv qui
        Builder.load_file("ui/pages/standby/standby.kv")
        Builder.load_file("ui/pages/home/home.kv")

        # Registro font se serve
        LabelBase.register(
            name="InriaSans",
            fn_regular="assets/fonts/Inria_Sans/InriaSans-Regular.ttf"
        )

        sm = MyScreenManager()
        sm.add_widget(StandbyScreen(name="standby", state=self.state))
        sm.add_widget(HomeScreen(name="home", state=self.state))
        sm.current = "standby"
        return sm
