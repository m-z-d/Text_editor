from kivy.core.window import Window
from kivy.logger import Logger
from kivy.properties import *
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.filechooser import FileChooser
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

edited_file = None
class fileHandler():
    #open file; autosave; put text into textinput at open.
    def __init__(self,filepath:str="",**kwargs) -> None:
        self.filepath=filepath
    def get_content(self):
        with open(self.filepath,'r') as file:
            file_content=file.read()
            Logger.info("FileRead:"+file_content)
            return file_content
    def set_content(self,text:str):
        with open(self.filepath,'w') as file:
            file.write(text)
            Logger.info("FileWrite:"+text)
    def append_content(self,text:str,end_l_string:str='\n'):
        with open(self.filepath,'a') as file:
            file.write(text+end_l_string)
            Logger.info("FileAppend:"+text)


class menuBar(GridLayout):
    filepath=StringProperty("")
    filename=StringProperty("filename not defined")
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.rows=1
        self.size_hint_x=1
        self.size_hint_y=0.04
        if len(self.filepath)>0:
            global edited_file
            edited_file = fileHandler(self.filepath)
#       ——————————————————————————————
        self.file_menu_button = Button(
            text="File",
            font_size=12
        )
        self.filemenu=DropDown(
            auto_width=False,
            size_hint_x=0.3)
        self.filemenu_filename=Label(
            text="Name: "+self.filename,
            size_hint=(0.9,None),
            height=25
        )
        self.filemenu_fileselect=Button(
            text="Open File",
            size_hint=(0.9,None),
            height=25,
            font_size=12
        )
        self.filemenu_properties=Button(
            text="File Properties",
            size_hint=(0.9,None),
            height=25,
            font_size=12
        )
        self.filemenu.add_widget(self.filemenu_filename)
        self.filemenu.add_widget(self.filemenu_fileselect)
        self.filemenu.add_widget(self.filemenu_properties)
        
        self.file_menu_button.bind(on_release=self.filemenu.open)
        self.insert_menu = Button(
            text="Insert",
            font_size=12
        )
        self.add_widget(self.file_menu_button)
        self.add_widget(self.insert_menu)
    def on_filepath(self, instance, value):
        self.filename=value.split("\\")[-1].split("/")[-1]

class view(RelativeLayout):
    cmd_line_args=ListProperty([])
    filepath=StringProperty("")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Logger.info(f"Arguments:{self.cmd_line_args}")
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
    def Edit_view(self,*args,**kwargs):
        next_arg_is_filepath=False
        self.clear_widgets()
        for i in self.cmd_line_args:
            if next_arg_is_filepath:
                self.filepath=i
                Logger.info(f"filepath received: {self.filepath}")
            if i =="-f":
                next_arg_is_filepath=True
        menus=menuBar(pos_hint={"x":0,"y":0.96},filepath=self.filepath)
        self.add_widget(menus)
        textinput=TextInput(
            size_hint=(0.85,0.96),
            pos_hint={"x":0.25,"y":0},
            background_color= [0.3,0.3,0.3,1]

        )
        self.add_widget(textinput)

        