from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class DataPanel(BoxLayout):
    def __init__(self, **kwargs):
        super(DataPanel, self).__init__(**kwargs)
        self.orientation = 'vertical'

        top_text = BoxLayout(orientation='horizontal', padding=30)
        top_text.add_widget(Label(text='Enter expression:'))
        top_text.add_widget(Label(text='Enter function edges a and b:'))
        bottom_fields = BoxLayout(
            orientation='horizontal', padding=20, spacing=20)
        bottom_fields.add_widget(Label(text='f(x) = '))

        self.expression = TextInput(multiline=False)
        self.a_edge = TextInput(multiline=False)
        self.b_edge = TextInput(multiline=False)
        self.run_btn = Button(text='RUN')

        bottom_fields.add_widget(self.expression)
        bottom_fields.add_widget(self.a_edge)
        bottom_fields.add_widget(self.b_edge)
        bottom_fields.add_widget(self.run_btn)

        self.add_widget(top_text)
        self.add_widget(bottom_fields)


class MainScreen(BoxLayout):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        self.orientation = 'vertical'
        self.data_panel = DataPanel()
        self.add_widget(self.data_panel)


class MainApp(App):
    def build(self):
        return MainScreen()


if __name__ == "__main__":
    MainApp().run()
