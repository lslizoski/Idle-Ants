from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
# from Upgrades.Incubator import Incubator
from kivy.uix.image import Image

# from Upgrades.Incubator import Incubator
class BoxLayouts(BoxLayout):
    # Method to be called when a button is pressed
    # def showSpeed(self):
    #     self.incubator = Incubator()
    #     self.incubator.getSpeed()
    pass

class MainWidget(Widget):
    # Create Method that can be called by with the buttons
    def addInt(self):
        self.incubator = Incubator()
        self.incubator.upgradeHatchSpeed()

class Line1(Widget):
    pass

class AntApp(App):
    pass

class AntApp2(App):
    def build(self):
        layout = FloatLayout()
        # Create an Image widget and set its source to your .png file
        image = Image(source='anthill_tunnels.png')
        image.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        image.size_hint = (None, None)  # Disable size_hint so you can set a fixed size
        image.size = (400, 400)  # Set the size of the image (adjust as needed)

        # Add the image widget to the layout
        layout.add_widget(image)

        return layout
        return image
        root = GridLayout(cols = 3, padding = 50, spacing = 100)
        root.add_widget(Line1())
        return root

AntApp().run()
# AntApp2().run()