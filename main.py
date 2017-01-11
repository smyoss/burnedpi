'''
BURN OS MAIN FILE
====================================

DESIGNED BY STEVE YOSS
JANUARY 2017

THIS PROJECT IS USED TO CREATE A GUI INTERFACE FOR THE RASPBERRY PI TO CONTROL LIGHTS, MUSIC, FLAME AND MORE. 

LEAVE NO TRACE. 

'''

from kivy.app import App

from kivy.uix.accordion import Accordion
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.core.image import Image
from kivy.graphics import BorderImage
from kivy.graphics import Color, Rectangle
from kivy.uix.image import AsyncImage
Config.set('kivy', 'keyboard_mode', 'systemandmulti')

import random

class LaunchScreen(Screen):
	pass

class LightsScreen(Screen):
	pass
	
class MusicScreen(Screen):
	pass
		
class RootScreen(ScreenManager):
	pass
	
class BurnOsApp(App):
    def build(self):
		return RootScreen()
	
if __name__ == "__main__":
    BurnOsApp().run()