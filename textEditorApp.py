import logging
import sys
import kivy
import Widgets
from kivy.app import App
from kivy.properties import *


class textEditorApp(App):
    def build(self):
        return Widgets.view(cmd_line_args=sys.argv[1:])

if __name__=="__main__":
    textEditorApp().run()
    
