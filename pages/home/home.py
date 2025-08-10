from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty, ListProperty, BooleanProperty, StringProperty
from kivy.graphics import Color, Rectangle

class HomeScreen(Screen):
    value = NumericProperty(0)  # Valore da 0 a 500
    background_color = ListProperty([1, 1, 1, 1])  # colore RGBA

    light_value = BooleanProperty(False)
    aspiration_value = BooleanProperty(False)
    current_temperature = StringProperty("236°C")
    top_temp = NumericProperty(0)
    middle_temp = NumericProperty(0)
    bottom_temp = NumericProperty(0)

    # Lista dei colori (in RGB, normalizzati 0-1), ordinati da caldo a freddo
    colors = [
        (52/255, 137/255, 235/255),   # più freddo
        (52/255, 235/255, 162/255),
        (143/255, 235/255, 52/255),
        (235/255, 217/255, 52/255),
        (235/255, 153/255, 52/255),
        (235/255, 61/255, 52/255),   # più caldo
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(value=self.update_background)
        with self.canvas.before:
            self.color_instruction = Color(*self.background_color)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect, size=self.update_rect)
        self.update_background(None, self.value) # Inizializza background

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def update_background(self, instance, value):
        # Normalizziamo il valore da 0 a 1
        normalized = max(0, min(1, value / 500))

        # Calcoliamo a quale intervallo appartiene il valore
        segment_length = 1 / (len(self.colors) - 1)
        segment_index = int(normalized / segment_length)
        if segment_index >= len(self.colors) - 1:
            segment_index = len(self.colors) - 2

        # Interpolazione lineare fra i due colori del segmento
        local_t = (normalized - segment_index * segment_length) / segment_length
        c1 = self.colors[segment_index]
        c2 = self.colors[segment_index + 1]

        interpolated = [
            c1[i] + (c2[i] - c1[i]) * local_t
            for i in range(3)
        ]
        # Aggiorniamo il colore con alfa 1
        self.background_color = interpolated + [1]

        # Applichiamo il colore al canvas
        self.color_instruction.rgba = self.background_color

    def switch_light(self):
        self.light_value = not self.light_value
        print(f"LUCE: {self.light_value}")
    
    def switch_aspiration(self):
        self.aspiration_value = not self.aspiration_value
        print(f"ASPIRAZIONE: {self.aspiration_value}")
