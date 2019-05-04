from kivy.core.window import Window
from kivy.config import Config
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.app import App
import kivy

Window.clearcolor = (1, 1, 1, 1)
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 1280)
Config.set('graphics', 'height', 720)

Builder.load_file('MainScreen.kv')


class MainApp(App):
    def build(self):
        my_activity = Factory.MyActivity()
        return my_activity


if __name__ == "__main__":
    MainApp().run()
