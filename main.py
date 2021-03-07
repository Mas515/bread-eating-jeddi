#import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

from os import path
import PIL.Image
import requests
from io import BytesIO
import webbrowser
import random

ideas = ["Go for a run","Bake a cake","Call a friend","Read a book", "Go outside"]

def fun():  
    ideas = ["Go for a run","Bake a cake","Call a friend","Read a book", "Go outside"]
    print(random.choice(ideas))
    
def song():
    webbrowser.open_new(r"https://open.spotify.com/playlist/2E6fOraA1wbcvsCxHL3F1E")
                        
def film():
    webbrowser.open_new(r"https://www.netflix.com/browse/genre/10579")

def cute2():
    animal1 = requests.get('https://images.pexels.com/photos/148182/pexels-photo-148182.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260')
    animal2 = requests.get('https://images.pexels.com/photos/374906/pexels-photo-374906.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940')
    animal3 = requests.get('https://images.pexels.com/photos/127027/pexels-photo-127027.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500')
    animal4 = requests.get('https://images.pexels.com/photos/257558/pexels-photo-257558.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500')
    animal5 = requests.get('https://images.pexels.com/photos/4588028/pexels-photo-4588028.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500')
    animals = [animal1,animal2,animal3,animal4,animal5]
    img = (PIL.Image.open(BytesIO((random.choice(animals)).content)))
    img.show()

Builder.load_string("""
<HomeScreen>:
    BoxLayout:
        Button:
            text: 'Gimme something to smash'
            on_press: root.manager.current = 'smash'
        Button:
            text: 'Gimme some love'
            on_press: root.manager.current = 'love'

<TakePicScreen>:
    BoxLayout:
        Button:
            text: 'What would you like to explode today?'

<GetLoveScreen>:
    BoxLayout:
        Button:
            text: 'Film'
            on_press: root.manager.current = 'film'
        Button:
            text: 'Idea'
            on_press: root.manager.current = 'idea'
        Button:
            text: 'Song'
            on_press: root.manager.current = 'song'
        Button:
            text: 'Cute animal'
            on_press: root.manager.current = 'animal'
<FilmScreen>:
    BoxLayout:
        Button:
            text: 'Here is your feel-good film'
<IdeaScreen>:
    BoxLayout:
        Button:
            text: "Here is your idea"
<SongScreen>:
    BoxLayout:
        Button:
            text: 'Here is a song for you'
<AnimalScreen>:
    BoxLayout:
        Button:
            text: 'What would you like to explode today?'

""")

# Add the screens
class HomeScreen(Screen):
    pass
class TakePicScreen(Screen):
    pass
class GetLoveScreen(Screen):
    pass
class FilmScreen(Screen):
    pass
class IdeaScreen(Screen):
    pass
class SongScreen(Screen):
    pass
class AnimalScreen(Screen):
    pass

class crapapp(App):
    def build(self):
        # Create the manager
        sm = ScreenManager()

        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(TakePicScreen(name='smash'))
        sm.add_widget(GetLoveScreen(name='love'))
        sm.add_widget(FilmScreen(name='film'))
        sm.add_widget(IdeaScreen(name='idea'))
        sm.add_widget(SongScreen(name='song'))
        sm.add_widget(AnimalScreen(name='animal'))

        return sm

        # home_layout = BoxLayout(padding = 2)
        # btn1 = Button(text = "Gimme something to smash", font_size = 50, background_color = red)
        # layout.add_widget(btn1)
        # btn2 = Button(text = "Gimme some love", font_size = 50, background_color = purple)
        # home_layout.add_widget(btn2)
        # button.bind(on_press=self.on_press_button)
        # return home_layout

    # def on_button_press(self, instance):
    #     button_text = instance.text
    #     if button_text == "Gimme something to smash":
    #         return Label(text="What would you like to explode today?")


    # def __init__(self, **kwargs):
    #     super(HomeScreen, self).__init__(**kwargs)
    #     self.cols = 1
    #     btn1 = Button(text='Gimme something to smash', font_size = 50, background_normal = '', background_color = [0, 0, 0, 1])
    #     btn2 = Button(text='Gimme some love', font_size = 50, background_normal = '', background_color = [156, 39, 176, 0.3])
    #     btn1.bind(on_press=self.callback)
    #     btn2.bind(on_press=self.callback)
    #     self.add_widget(btn1)
    #     self.add_widget(btn2)
    # def callback(self, instance):
    #     print('The button %s state is <%s>' % (instance, instance.state))


# class crapapp(App):
#   	def build(self):
#   		#return Label(text="Welcome to the crap app – it's okay to feel crap")
#   		return HomeScreen()

if __name__ == '__main__':
    crapapp().run()