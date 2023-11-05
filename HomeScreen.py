from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.uix.image import Image
from kivy.clock import Clock
from Game import Game

class BoxLayouts(BoxLayout):
    pass

class FloatLayouts(FloatLayout):
    game = Game()
    clock = 1

    def __init__(self, **kwargs):
        super(FloatLayouts, self).__init__(**kwargs)
        super().__init__(**kwargs)
        ant = Image(source="images/ant.png")

        # Add the image to the layout
        ant.pos = (0, -100)
        self.add_widget(ant)
        anim = Animation(x=250, y=-410, duration=5) + Animation(x=500, duration=5) + Animation(y=-500, duration=0.1) + Animation(x=-500, y=-500, duration=0.1)
        anim.repeat = True
        anim.start(ant)
        Clock.schedule_interval(self.timers, 1)

    def timers(self, interval):
        if (self.clock % round(self.game.incubator.getHatchSpeed()) == 0):
            self.game.hatchEgg()
            print("Hatch")
        if (self.clock % round(self.game.queenUpgrades.getEggLaySpeed())) == 0:
            self.game.layEgg()
            print("Lay")
        self.clock += 1


    def start(self):
        Clock.unschedule(self.timers)
        Clock.schedule_interval(self.timers, 1)

    def stop(self):
        Clock.unschedule(self.timers)

class MainWidget(Widget):
    pass

class IdleAntsApp(App):
    def build(self):
        return FloatLayouts()

IdleAntsApp().run()
