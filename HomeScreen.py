from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from Game import Game


class BoxLayouts(BoxLayout):
    pass


class FloatLayouts(FloatLayout):
    game = Game()

    def __init__(self, **kwargs):
        super(FloatLayouts, self).__init__(**kwargs)
        super().__init__(**kwargs)
        Clock.schedule_interval(self.layEgg, self.game.queenUpgrades.eggLaySpeed)

    def layEgg(self, interval):
        self.game.layEgg()

    def start(self):
        Clock.unschedule(self.layEgg)
        Clock.schedule_interval(self.layEgg, self.game.queenUpgrades.eggLaySpeed)

    def stop(self):
        Clock.unschedule(self.layEgg)

class MainWidget(Widget):
    pass

class IdleAntsApp(App):
    def build(self):
        return FloatLayouts()

IdleAntsApp().run()
