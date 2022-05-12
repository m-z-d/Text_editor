from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.filechooser import FileChooser
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.core.window import Window
from kivy.properties import *

class menuBar(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows=1
        self.size_hint_x=1
        self.size_hint_y=0.05
#       ——————————————————————————————
        self.file_menu_button = Button(
            text="File",
            font_size=12
        )
        self.filemenu=DropDown()
        self.filemenu_fileselect=Button(
            text="Open File"
        )
        self.filemenu.add_widget(self.filemenu_fileselect)
        self.file_menu_button.bind(on_press=self.filemenu.open)
        self.insert_menu = Button(
            text="Insert",
            font_size=12
        )
        self.add_widget(self.file_menu_button)
        self.add_widget(self.insert_menu)

class view(RelativeLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.Welcome_view()
    def Welcome_view(self):
        username=""
        self.name="Welcome screen"
        Welcome_label=Label(text="Welcome to the Generic Text Editor Project\n\nby LasevIX_",
        font_name="fonts/Helvetica.ttf",
        font_size=24,
        valign="center",
        halign="center",
        bold=True,
        size_hint_y=0.5,
        size_hint_x=1,
        pos_hint={"x":0,"y":0.5},
        )
        self.add_widget(Welcome_label)
        start_button=Button(text="Click here to start,\nor press any key",
        size_hint_y=0.15,
        size_hint_x=0.3,
        pos_hint={"x":0.7/2,"y":0.2},
        valign="center",
        halign="center",
        font_size=24
        )
        start_button.bind(on_press=self.Edit_view)
        self.add_widget(start_button)
    def Edit_view(self,caller,**kwargs):
        self.clear_widgets()
        menus=menuBar(pos_hint={"x":0,"y":0.95})
        self.add_widget(menus)
        textinput=TextInput(
            size_hint=(0.85,0.9),
            pos_hint={"x":0.25,"y":0},
            background_color= [0.3,0.3,0.3,1]

        )
        self.add_widget(textinput)

        