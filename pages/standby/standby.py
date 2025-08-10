from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from datetime import datetime

class StandbyScreen(Screen):
    def on_enter(self):
        # Quando entri nella schermata, inizia ad aggiornare
        self.update_time()
        Clock.schedule_interval(self.update_time, 1)  # ogni secondo

    def on_leave(self):
        # Quando esci dalla schermata, ferma l'aggiornamento
        Clock.unschedule(self.update_time)

    def update_time(self, *args):
        now = datetime.now()
        self.ids.time_label.text = now.strftime("%H:%M")
        self.ids.date_label.text = now.strftime("%d-%m-%Y")
