from FoodGenerator import FoodGenerator
from kivy.core.audio import SoundLoader

class AntGenerator:

    foodGenerator = FoodGenerator()

    def __init__(self):
        sound = SoundLoader.load('../Audio/FoodMunch.mp3')
        if sound:
            sound.volume = 1
            sound.play()

    def hasFood(self):
        pass