from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

from Game import Game

class BoxLayouts(BoxLayout):
    pass


class FloatLayouts(FloatLayout):
    pass


class MainWidget(Widget):
    pass


class Room3(App):
    """
    def build(self):
        game = Game()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        Clock.schedule_interval(game.layEgg(), game.queenUpgrades.getEggLaySpeed()) #Lays egg every so often
        return MainWidget"""

Room3().run()
