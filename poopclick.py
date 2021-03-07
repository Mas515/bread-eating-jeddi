#The purpose of this section is the part of the app that is anger release. You tap the screen and a poop emoji appears in this location
from pynput import mouse
#from pynput.mouse import Button, Controller # I can't have this line when I'm switching to the button option
from kivy.uix.image import Image
from kivy.lang import Builder
class MainApp(App):
#This works to just display the image
    # def build(self):
    #     img = Image(source='/Users/marine/hackherthon/poop.png',
    #                 size_hint=(1, .5),
    #                 pos_hint={'center_x':.5, 'center_y':.5})
    #     return img
#I now want the image display to be linked to click position
	# def build(self):
	# 	def on_click(x, y, button, pressed):
	# 		if pressed:
	# 			img = Image(source='/Users/marine/hackherthon/poop.png',
	# 					size_hint=(1, .5), pos_hint={'center_x':x, 'center_y':y})
	# 			return img
	# 		if not pressed:
	# 			return False
	# 	listener = mouse.Listener(on_click=on_click)
	# 	listener.start()
	# 	return img # it's a problem that the img is in the subfunction but we couldn't change it.
#Since the code above didn't work we tried making a button you click and the poop emojis appear
#it didn't work either
    def build(self):
        button = Button(text='Hello from Kivy',
                        size_hint=(.5, .5),
                        pos_hint={'center_x': .5, 'center_y': .5})
        button.bind(on_press=self.on_press_button)
        return button
    def on_press_button(self, instance):
        img = Image(source='/Users/marine/hackherthon/poop.png',
                    size_hint=(1, .5),
                    pos_hint={'center_x':.5, 'center_y':.5})
        Builder.load_string("""
BoxLayout:
    orientation: "vertical"
    Image:
        id: image
        source: "/Users/marine/hackherthon/poop.png"
            """)
        return img
if __name__ == '__main__':
    app = MainApp()
    app.run()