import pygame

from GUI.Window import Window
from GUI.Slider import Slider
from GUI.Button import Button

class ColorWheel(Window):
	def __init__(self, x, y, w, h, p):
		Window.__init__(self,x,y,w,h,p)	
		self.sliders = []
		self.sliders.append(Slider(10,50,100,(0,255), 'red'))
		self.sliders.append(Slider(10,90,100,(0,255), 'green'))
		self.sliders.append(Slider(10,130,100,(0,255), 'blue'))
		self.labels = [] # I call them labels but they're really just buttons without actions!
		self.labels.append(Button(0,30,"Red:", self.surface, (255,255,255)))
		self.labels.append(Button(0,70,"Green:", self.surface, (255,255,255)))
		self.labels.append(Button(0,110,"Blue:", self.surface, (255,255,255)))
		self.current_color_box = pygame.Surface((50,50))

	def draw(self):
		for label in self.labels:
			label.draw(self.surface)
		for slider in self.sliders:
			slider.draw(self.surface)
		self.surface.blit(self.current_color_box, (120, 40))
		pygame.draw.line(self.surface, (100,100,100), (120,40), (120,90))
		pygame.draw.line(self.surface, (100,100,100), (120,40), (170,40))
		pygame.draw.line(self.surface, (100,100,100), (170,40), (170,90))
		pygame.draw.line(self.surface, (100,100,100), (170,90), (120,90))
		Window.draw(self)
		
	def update(self, mouseclick, scrolldown, scrollup):
		for slider in self.sliders:
			slider.update(self.x+slider.x, self.y+slider.y)
			if slider.title == 'red':
				r = slider.get_value()
			elif slider.title == 'green':
				g = slider.get_value()
			elif slider.title == 'blue':
				b = slider.get_value()
		self.current_color = (r,g,b)
		self.current_color_box.fill(self.current_color)
		Window.update(self, mouseclick, scrolldown, scrollup)

