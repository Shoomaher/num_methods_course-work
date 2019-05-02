from kivy.app import App
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = (900, 800)

Builder.load_file('MainScreen.kv')


class MainApp(App):
    def build(self):
        my_activity = Factory.MyActivity()
        return my_activity


if __name__ == "__main__":
    MainApp().run()
