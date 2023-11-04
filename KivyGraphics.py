from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from Upgrades.Incubator import Incubator


class BoxLayouts(BoxLayout):
    def showSpeed(self):
        incubator = Incubator()
        print(incubator.getSpeed())

class MainWidget(Widget):
    pass


class IdleAntsApp(App):
    pass


IdleAntsApp().run()
