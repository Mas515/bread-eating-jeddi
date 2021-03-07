from os import path
import PIL.Image
import requests
from io import BytesIO
import webbrowser
import random

animal1 = requests.get('https://images.pexels.com/photos/148182/pexels-photo-148182.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260')
a_1 = PIL.Image.open(BytesIO(animal1.content))
animal2 = requests.get('https://images.pexels.com/photos/374906/pexels-photo-374906.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940')
a_2 = PIL.Image.open(BytesIO(animal2.content))
animal3 = requests.get('https://images.pexels.com/photos/127027/pexels-photo-127027.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500')
a_3 = PIL.Image.open(BytesIO(animal3.content))
animal4 = requests.get('https://images.pexels.com/photos/257558/pexels-photo-257558.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500')
a_4 = PIL.Image.open(BytesIO(animal4.content))
animal5 = requests.get('https://images.pexels.com/photos/4588028/pexels-photo-4588028.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500')
a_5 = PIL.Image.open(BytesIO(animal5.content))

animals = [animal1,animal2,animal3,animal4,animal5]

ideas = ["Go for a run","Bake a cake","Call a friend","Read a book", "Go outside"]
  
from tkinter import *     
top = Tk()  
  
top.geometry("200x100")  
  
def fun():  
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

b1 = Button(top,text = "Idea", command = fun,fg = "teal",bg = "thistle", relief = "ridge",activeforeground = "red",activebackground = "pink",pady=10,padx=10,borderwidth = 5)  
  
b2 = Button(top, text = "Cute", command = cute2,fg = "teal",bg = "lightpink", relief = "ridge",activeforeground = "blue",activebackground = "pink",pady=10,padx=10,borderwidth = 5)  
  
b3 = Button(top, text = "Song",command = song,fg = "goldenrod",bg = "skyblue1", relief = "ridge", activeforeground = "green",activebackground = "pink",pady = 10,borderwidth = 5)  
  
b4 = Button(top, text = "Film",command = film,fg = "darkkhaki",bg = "mistyrose2", relief = "ridge", activeforeground = "yellow",activebackground = "pink",pady = 10,borderwidth = 5)  
  
b1.pack(side = LEFT)  
  
b2.pack(side = RIGHT)  
  
b3.pack(side = TOP)  
  
b4.pack(side = BOTTOM)  
  
top.mainloop()  