from __future__ import print_function
import kivy
kivy.require('1.9.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader

class SoundTest(BoxLayout):

    def __init__(self, **kwargs):
        super(SoundTest, self).__init__(**kwargs)
        button = Button(text='Play sound')
        self.add_widget(button)
        button.bind(on_release=self.PlaySound)

    def PlaySound(self, widget):
        snd = SoundLoader.load('../assets/audio/scotch.ogg')
        snd.bind(on_stop=self.UnloadSoundWhenDone)
        snd.play()
        print ("play", snd)

    def UnloadSoundWhenDone(self, snd):
        print ("unload", snd)
        snd.unload()


class MyApp(App):

    def build(self):
        return SoundTest()

if __name__ == '__main__':
    MyApp().run()