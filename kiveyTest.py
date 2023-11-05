from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from Incubator import Incubator


class BoxLayouts(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.incubator = Incubator()
        self.vali = str(self.incubator.hatchSpeed)

    def upgradeSpeed(self):
        self.incubator.upgradeHatchSpeed()


class MainWidget(Widget):
    pass


class AntsApp(App):
    pass


AntsApp().run()
