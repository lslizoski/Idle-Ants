from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget

from kivy.graphics import Line

class MainWidget(Widget):
    pass
class Line1(Widget):
    pass
class Line2(Widget):
    pass
class Line3(Widget):
    pass
class LineCircle(Widget):
    pass
class LineRectangle(Widget):
    pass

class AntApp(App):
    pass

class AntApp2(App):
    def build(self):
        root = GridLayout(cols = 3, padding = 50, spacing = 100)
        root.add_widget(Line1())
        root.add_widget(Line2())
        root.add_widget(Line3())
        root.add_widget(LineCircle())
        root.add_widget(LineRectangle())
        return root

AntApp().run()