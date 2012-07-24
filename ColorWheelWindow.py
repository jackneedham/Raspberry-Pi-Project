import pygame

from GUI.Window import Window
from GUI.Slider import Slider
from GUI.Button import Button

from COLORPICKER.ColorWheel import ColorWheel
from COLORPICKER.CustomColors import CustomColors

class ColorWheelWindow(Window):
	def __init__(self, x, y, w, h, p):
		Window.__init__(self,x,y,w,h,p,"Color Picker")	
		self.wheel = ColorWheel(120, 30)
		self.sliders = []
		self.sliders.append(Slider(10,50,100,(0,255), 'red'))
		self.sliders.append(Slider(10,90,100,(0,255), 'green'))
		self.sliders.append(Slider(10,130,100,(0,255), 'blue'))
		self.labels = [] # I call them labels but they're really just buttons without actions!
		self.labels.append(Button(0,30,"Red:", self.surface, (255,255,255)))
		self.labels.append(Button(0,70,"Green:", self.surface, (255,255,255)))
		self.labels.append(Button(0,110,"Blue:", self.surface, (255,255,255)))
		self.buttons = []
		self.buttons.append(Button(10, 160, "Choose", self.surface, (50,50,50)))
		self.current_color_box = pygame.Surface((50,50))
		self.custom_colors = CustomColors(70, 200, 200)
		self.custom_selected = 0

	def draw(self):
		for label in self.labels:
			label.draw(self.surface)
		for slider in self.sliders:
			slider.draw(self.surface)
		for button in self.buttons:
			button.draw(self.surface)
		self.wheel.draw(self.surface)
		pygame.draw.line(self.surface, (200,200,200), (10,190), (self.width-10, 190))
		self.surface.blit(self.current_color_box, (10, 200))
		self.custom_colors.draw(self.surface)
		btn = self.custom_colors.grid[self.custom_selected]
		zerox = self.custom_colors.x+btn.x # just using vars to
		zeroy = self.custom_colors.y+btn.y # keep the lines nice and short
		# manually drawing lines because a for loop is achieves the same thing
		# in only a couple of lines less but with far more resources used
		pygame.draw.line(self.surface, (0,0,0), (zerox,zeroy), (zerox+23, zeroy),2)
		pygame.draw.line(self.surface, (0,0,0), (zerox,zeroy), (zerox, zeroy+23),2)
		pygame.draw.line(self.surface, (0,0,0), (zerox+23,zeroy), (zerox+23, zeroy+24),2)
		pygame.draw.line(self.surface, (0,0,0), (zerox,zeroy+23), (zerox+23, zeroy+23),2)
		Window.draw(self)
		
	def update(self, mouseclick, scrolldown, scrollup, keypressed):

		if self.wheel.is_clicked(self.x+self.wheel.x, self.y+self.wheel.y):
			r,g,b,a = self.wheel.get_color()
			
		else:
			for btn in range(len(self.custom_colors.grid)):
				if self.custom_colors.grid[btn].is_clicked(self.x+self.custom_colors.x+self.custom_colors.grid[btn].x,
				self.y+self.custom_colors.y+self.custom_colors.grid[btn].y, mouseclick):
					self.custom_selected = btn
					if self.custom_colors.grid[btn].color != (212,212,212):
						r,g,b = self.custom_colors.grid[btn].color
		
		for slider in self.sliders:
			slider.update(self.x+slider.x, self.y+slider.y)
			try:
				if slider.title == 'red':
					slider.set_value(r)	
				if slider.title == 'green':
					slider.set_value(g)
				if slider.title == 'blue':
					slider.set_value(b)
			except: # catch 'em all.
				if slider.title == 'red':
					r = slider.get_value()
				if slider.title == 'green':
					g = slider.get_value()
				if slider.title == 'blue':
					b = slider.get_value()

		for button in self.buttons:
			if button.is_clicked(self.x+button.x, self.y+button.y, mouseclick):
				if button.text == 'Choose':
					self.custom_colors.grid[self.custom_selected].color = self.current_color
					self.custom_colors.grid[self.custom_selected].surface.fill(self.current_color)
						
		self.current_color = (r,g,b)
		self.current_color_box.fill(self.current_color)
		Window.update(self, mouseclick, scrolldown, scrollup)

