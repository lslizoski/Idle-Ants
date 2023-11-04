from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.clock import Clock
from Upgrades.Incubator import Incubator


class BoxLayouts(BoxLayout):
    # Method to be called when a button is pressed
    def showSpeed(self):
        self.incubator = Incubator()
        self.incubator.getSpeed()




class MainWidget(Widget):
    pass


class IdleAntsApp(App):
    pass


IdleAntsApp().run()
