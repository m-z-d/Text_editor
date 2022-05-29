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
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle

class BackgroundLayout(RelativeLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(0.1,0.1, 0.15, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class fileHandler():
    #open file; autosave; put text into textinput at open.
    def __init__(self,filepath:str="",**kwargs) -> None:
        if len(filepath)>1:
            self.filepath=filepath
        else:
            self.filepath="untitled.txt"
        x=None
        try: x= open(self.filepath,"x")
        except: pass
        if x!=None : x.close()
    def get_content(self):
        with open(self.filepath,'r') as file:
            file_content=file.read()
            Logger.info("FileRead:"+file_content)
            return file_content
    def set_content(self,text:str):
        """WARNING: TRUNCATES ALL PREVIOUS CONTENT"""
        with open(self.filepath,'w') as file:
            file.write(text)
            Logger.info("FileWrite:"+text)
    def append_content(self,text:str,end_l_string:str='\n'):
        with open(self.filepath,'a') as file:
            file.write(text+end_l_string)
            Logger.info("FileAppend:"+text)

class TextInputCustom(RelativeLayout):
    def __init__(self,file:fileHandler, **kwargs):
        super().__init__(**kwargs)
        startup_text=file.get_content()
        self.text_box=TextInput(
            text=startup_text,
            background_normal="0x000000ff",
            background_color=[0.2,0.2,0.225,1],
            foreground_color=[0.7,0.7,0.8,1],
            cursor_color = [0.7,0.7,0.8,1]

        )
        self.add_widget(self.text_box)
    def save_to_file(self,file:fileHandler):
        output="\n".join(self.text_box._lines)
        file.set_content(output)
        Logger.info(f"Saved:{output}")

class FileSelectionPopupContent(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols=1
        text=Label(text="Type full filepath of the file you want to select and enter:")
        self.input=TextInput(hint_text="filepath",multiline=False)
        self.add_widget(text)
        self.add_widget(self.input)

class sideBar(GridLayout):
    pass

class menuBar(RelativeLayout):
    filepath=StringProperty("")
    filename=StringProperty("Filename not defined")
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_x=1
        self.size_hint_y=0.04
#       ——————————————————————————————
        self.file_menu_button = Button(
            text="File",
            background_normal="0x000000ff",
            background_color=[0.2,0.2,0.225,1],
            color=[0.1,0.6,0.3,1],
            font_size=12,
            size_hint=[0.2,1]
        )
        self.filemenu=DropDown()
        self.filemenu_filename=Label(
            text="Name: "+self.filename,
            size_hint=(0.9,None),
            color=[0.1,0.6,0.3,1],
            height=25,
            font_size=12
        )
        self.filemenu_fileselect=Button(
            text="Open File",
            size_hint=(0.9,None),
            height=25,
            background_normal="0x000000ff",
            background_color=[0.2,0.2,0.225,1],
            color=[0.1,0.6,0.3,1],
            font_size=12
        )
        self.filemenu_properties=Button(
            text="File Properties",
            size_hint=(0.9,None),
            height=25,
            background_normal="0x000000ff",
            background_color=[0.2,0.2,0.225,1],
            color=[0.1,0.6,0.3,1],
            font_size=12
        )
        self.filemenu_save_file=Button(
            text="Save File",
            size_hint=(0.9,None),
            height=25,
            background_normal="0x000000ff",
            background_color=[0.2,0.2,0.225,1],
            color=[0.1,0.6,0.3,1],
            font_size=12
        )
        self.filemenu_fileselect_popup_content=FileSelectionPopupContent()
        self.filemenu_fileselect_popup=Popup(
            title="File Selection",
            content=self.filemenu_fileselect_popup_content,
            size_hint=[0.5,0.2],
            pos_hint={"x":0.25,"y":0.4}
        )
        self.filemenu_fileselect.bind(on_release=self.filemenu_fileselect_popup.open)
        self.filemenu.add_widget(self.filemenu_filename)
        self.filemenu.add_widget(self.filemenu_fileselect)
        self.filemenu.add_widget(self.filemenu_properties)
        self.filemenu.add_widget(self.filemenu_save_file)
        
        self.file_menu_button.bind(on_release=self.filemenu.open)
        self.insert_menu = Button(
            text="Insert",
            background_normal="0x000000ff",
            background_color=[0.2,0.2,0.225,1],
            color=[0.6,0.3,0.1,1],
            font_size=12,
            size_hint=[0.2,1],
            pos_hint={"x":0.2}
        )
        self.add_widget(self.file_menu_button)
        self.add_widget(self.insert_menu)
    def on_filepath(self, instance, value):
        self.filename=value.split("\\")[-1].split("/")[-1]  #extracts filename from full filepath, ignores all folder names etc.
        if len(self.filename)<10:
            self.filemenu_filename.text=self.filename
        else:
            self.filemenu_filename.text=str(self.filename.split(".")[0][:10]+"...")

class view(BackgroundLayout):
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
        start_button=Button(text="Click here to start",
        size_hint_y=0.5,
        size_hint_x=1,
        valign="center",
        halign="center",
        font_size=24,
        background_normal="0x000000ff",
        background_color=[0.1,0.1,0.15,1]
        )
        start_button.bind(on_press=self.Edit_view)
        self.add_widget(start_button)
    def Edit_view(self,*args,**kwargs):
        next_arg_is_filepath=False
        self.clear_widgets()
        for i in self.cmd_line_args:  #detects filepath argument and saves it for use in menus and textinput
            if next_arg_is_filepath:
                self.filepath=i
                Logger.info(f"filepath received: {self.filepath}")
            if i =="-f":
                next_arg_is_filepath=True

        self.file=fileHandler(self.filepath)
        self.menus=menuBar(pos_hint={"x":0,"y":0.96},filepath=self.filepath)
        textinput=TextInputCustom(
            self.file,
            size_hint=(0.85,0.96),
            pos_hint={"x":0.25,"y":0},   
        )
        self.menus.filemenu_save_file.bind(on_press=lambda x:textinput.save_to_file(self.file))  #x is needed to absorb instance information
        self.menus.filemenu_fileselect_popup_content.input.bind(on_text_validate=lambda x:self.set_filepath_from_input(x))
        self.add_widget(self.menus)
        self.add_widget(textinput)
    def on_filepath(self, instance, value):
        self.menus.filepath=value

    def set_filepath_from_input(self,input:TextInput):
        Logger.info("File changed:"+input._get_text())
        self.filepath=input._get_text()
        self.file=fileHandler(self.filepath)


        