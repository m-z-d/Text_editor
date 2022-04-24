import logging
import kivy

from kivy.app import App
from kivy.properties import *
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
class base_window(FloatLayout):
    def __init__(self) -> None:
        super().__init__()
        self.text_input=TextInput()
class textEditorApp(App):
    def build(self):
        return base_window()

if __name__=="__main__":
    textEditorApp().run()

