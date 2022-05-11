import logging
import kivy
import Widgets
from kivy.app import App
from kivy.properties import *

class textEditorApp(App):
    def build(self):
        return Widgets.view()

if __name__=="__main__":
    textEditorApp().run()

