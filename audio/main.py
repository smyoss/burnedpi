import os
os.environ['KIVY_AUDIO'] = 'sdl2'

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, ObjectProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader

class SoundBoard(Screen):
	def scotch(self):
		sound = SoundLoader.load('../assets/audio/scotch.wav')
		if sound:
			sound.play()
			sound.seek(0.00)
			print("Sound found at %s" % sound.source)
			print("Sound is %.3f seconds" % sound.length)
			print("Sound status %s" % sound.status)

class RootScreen(ScreenManager):
	pass
	
class audio(App):
	def build(self):
		return SoundBoard()

if __name__ == "__main__":
    audio().run()