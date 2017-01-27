'''
BURN OS MAIN FILE
====================================

DESIGNED BY STEVE YOSS
JANUARY 2017

THIS PROJECT IS USED TO CREATE A GUI INTERFACE FOR THE RASPBERRY PI TO CONTROL LIGHTS, MUSIC, FLAME AND MORE. 

LEAVE NO TRACE. 

'''
import os
os.environ['KIVY_AUDIO'] = 'sdl2'

from kivy.app import App

#IMPORT ALL THE UX COMPONENTS 
from kivy.clock import Clock
from kivy.uix.accordion import Accordion
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, ObjectProperty, NumericProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.core.image import Image
from kivy.graphics import Color, Rectangle, BorderImage
from kivy.core.audio import SoundLoader
from kivy.uix.image import AsyncImage
Config.set('kivy', 'keyboard_mode', 'systemandmulti')

#BRING IN THE KIVY GARDEN WIDGETS
from kivy.garden.mapview import MapView, MapMarker

import psutil
import random


class LaunchScreen(Screen):
	pass

class LightsScreen(Screen):
	pass
	
class Navigation(Screen):
	pass

class System(Screen):
	def mem():
		mem = p.virtual_memory().percent
		return mem

	def processor():
		processor = p.cpu_percent(interval=1)
		return processor
		
class MusicScreen(Screen):
	pass

class SoundBoard(Screen):
	def scotch(self):
		sound = SoundLoader.load('assets/audio/scotch.wav')
		if sound:
			sound.play()
			sound.seek(0.00)
			print("Sound found at %s" % sound.source)
			print("Sound is %.3f seconds" % sound.length)
			print("Sound status %s" % sound.status)
					
class RootScreen(ScreenManager):
	pass
	
class BurnOsApp(App):
	
	def mem(self):
		mem = psutil.virtual_memory().percent
		mem = '%s' % mem
		return mem
	
	def build(self):
		return RootScreen()

if __name__ == "__main__":
    BurnOsApp().run()