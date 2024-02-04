import kivy
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from base_chatbot import base_chatbot


Window.size = (320, 600)

class CineBot(MDApp):
    pass
    def build(self):
        self.title ="CineBot"
        
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_pallete = 'Teal'
        self.theme_cls.accent_pallete = 'Teal'
        self.theme_cls.accent_hue = '400'
        



CineBot().run()