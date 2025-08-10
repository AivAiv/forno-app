from kivy.config import Config

# Imposta il font di default globale a "InriaSans"
Config.set('kivy', 'default_font', ['InriaSans', 'assets/fonts/Inria_Sans/InriaSans-Regular.ttf', 'assets/fonts/Inria_Sans/InriaSans-Bold.ttf', 'assets/fonts/Inria_Sans/InriaSans-Italic.ttf'])
Config.write()

# Imposta dimensioni iniziali finestra
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '800')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

# Importiamo le classi da file separati
from pages.standby.standby import StandbyScreen
from pages.home.home import HomeScreen
from components.clickableimage.clickableimage import ClickableImage
from components.temperature_control.temperature_control import TemperatureControl

from kivy.core.text import LabelBase

# Registra il font personalizzato
LabelBase.register(name='InriaSans', fn_regular='assets/fonts/Inria_Sans/InriaSans-Regular.ttf')

class MyScreenManager(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        sm = MyScreenManager()
        sm.add_widget(StandbyScreen(name='standby'))
        sm.add_widget(HomeScreen(name='home'))
        sm.current = 'standby'
        return sm

if __name__ == '__main__':
    Builder.load_file('pages/standby/standby.kv')      # UI StandbyScreen
    Builder.load_file('components/temperature_control/temperature_control.kv')
    Builder.load_file('pages/home/home.kv')         # UI HomeScreen
    MyApp().run()
