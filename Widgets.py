from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class Welcome_view(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size=(200, 300)
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
        pos=(0,300),
        )
        self.add_widget(Welcome_label)
        start_button=Button(text="Click here to start,\nor press any key",
        size_hint_y=0.2,
        size_hint_x=0.4,
        pos_hint={"x":0.3,"y":0.2},
        valign="center",
        halign="center",
        font_size=24
        )
        self.add_widget(start_button)