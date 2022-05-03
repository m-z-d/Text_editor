import logging
import kivy
import Widgets
from kivy.app import App
from kivy.properties import *
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout

class window(FloatLayout):
    def __init__(self,**kwargs) -> None:
        super().__init__(size=(200, 300),**kwargs)
        self.add_widget(Widgets.Welcome_view(
            size_hint_y=1,
            size_hint_x=1,
            pos=(100,150)
        ))
        # self.text_input=TextInput(background_color=[0,0,0,1],cursor_color=[0.5,0.5,0.5,1],
        # foreground_color=[1,1,1,1],font_name="fonts/Helvetica.ttf")
        # self.add_widget(self.text_input)
        
    # def Welcome_screen(self):
    #     self.name="Welcome screen"
    #     Welcome_label=Label(text="Welcome to the Generic Text Editor Project\n\nby LasevIX_",
    #     font_name="fonts/Helvetica.ttf",
    #     font_size=24,
    #     valign="center",
    #     halign="center",
    #     bold=True,
    #     size_hint_y=0.5,
    #     size_hint_x=1,
    #     pos=(0,300),
    #     )
    #     self.add_widget(Welcome_label)
    #     start_button=Button(text="Click here to start,\nor press any key",
    #     size_hint_y=0.2,
    #     size_hint_x=0.4,
    #     pos_hint={"x":0.3,"y":0.2},
    #     valign="center",
    #     halign="center",
    #     font_size=24
    #     )
    #     self.add_widget(start_button)

class textEditorApp(App):
    def build(self):
        return window()

if __name__=="__main__":
    textEditorApp().run()

