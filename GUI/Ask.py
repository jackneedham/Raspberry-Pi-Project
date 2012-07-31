from Window import Window
from Button import Button
from Input import Input
import pygame

class Ask(Window):
	def __init__(self, question, parent, answer_var):
		self.width = 400
		self.height = 200
		self.parent = parent
		self.x = (parent.get_width()-self.width)/2.0
		self.y = (parent.get_height()-self.height)/2.0
		self.text = question
		answer_var = 'LOL'
		Window.__init__(self, self.x, self.y, self.width, self.height, parent, 'Ask', True)
		self.q_label = Button(20,50,self.text,self.surface, (255,255,255), hpad=0)
		self.a_input = Input(20, 80, 360)
	
	def draw(self):
		self.q_label.draw(self.surface)
		self.a_input.draw(self.surface)
		Window.draw(self)
	
	def update(self,mouseclick, scrolldown=False, scrollup=False, keypressed=''):
		self.a_input.update(self.x+self.a_input.x, self.y+self.a_input.y, mouseclick, keypressed)
		Window.update(self,mouseclick, scrolldown=False, scrollup=False, keypressed='')

