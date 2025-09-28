from kivy.uix.screenmanager import Screen

class MenuScreen(Screen):
    
    def __init__(self, state, **kwargs):
        super().__init__(**kwargs)
        self.state = state