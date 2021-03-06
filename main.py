from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from functools import partial

class crapapp(App):
    def build(self):
        return Label(text="Welcome to the crap app – it's okay to feel crap")

if __name__ == '__main__':
    crapapp().run()