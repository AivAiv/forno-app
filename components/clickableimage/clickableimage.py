from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

class ClickableImage(ButtonBehavior, Image):
    """Immagine cliccabile che si comporta come un bottone."""
    pass
