import pygame
from GUI.Window import Window
from GUI.Button import Button
from GUI.TextBox import TextBox
from GUI.ScrollPane import ScrollPane
from GUI.Input import Input

class ToolWindow(Window):
	def __init__(self,x,y,w,h,p):
		Window.__init__(self,x,y,w,h,p, 'Tool Bar')
		self.buttons = []
		self.buttons.append(Button(10, 30, 'Select', self.surface, c=(50,50,50)))
		self.mytextbox = TextBox(00,0, 150, 'Lorem ipsum dolor sit amet, \n \n \n consectetur adipiscing elit. Proin at porta mauris. Aliquam ultricies venenatis nisi, non feugiat elit consequat at. Suspendisse sollicitudin condimentum mauris, vel consequat lorem ornare sed. Vestibulum eu eros libero. Quisque sed purus non orci tincidunt volutpat et in nisi. Fusce quis cursus urna. Aliquam ipsum urna, dictum a convallis sed, tristique eu lectus. In hac habitasse platea dictumst. Praesent vestibulum, diam sit amet sagittis consequat, lacus velit commodo risus, ac congue erat dui nec diam. ?')
		self.mypane = ScrollPane(10, 120, 170, 200, 400)
		self.inputbox = Input(160, 50, 100)

	def draw(self):
		for button in self.buttons:
			button.draw(self.surface)
		self.mytextbox.draw(self.mypane.content_surface)

		self.mypane.draw(self.surface)
		
		self.inputbox.draw(self.surface)
		
		# Inherited draw method from base class, draws onto parent
		Window.draw(self)

	def update(self, mouseclick, scrolldown, scrollup, keypressed):
		for button in self.buttons:
			if button.is_clicked(self.x+button.x, self.y+button.y, mouseclick):
				if self.mytextbox.text.split(' ')[0] == "Cool":
					self.mytextbox.text += ' And again.'
				else:
					self.mytextbox.text = "Cool you clicked a button"
				self.mypane.render()
				self.mytextbox.render()
		self.mypane.scrolldown = scrolldown
		self.mypane.scrollup = scrollup
		self.mypane.update(self.x+self.mypane.x, self.y+self.mypane.y)
		self.inputbox.update(self.x+self.inputbox.x, self.y+self.inputbox.y, mouseclick, keypressed)

		Window.update(self,mouseclick, scrolldown, scrollup)
