
import pygame
import StyleGuide

class ColorButton:
	def __init__(self, x, y, c=(150,150,150)):
		self.x = x
		self.y = y
		self.color = c
		self.width = 25
		self.height = 25
		self.surface = pygame.Surface((self.width, self.height))
		self.surface.fill(self.color)
   
	def is_clicked(self, absx, absy, mouseclick):
		if mouseclick:
			mx, my = pygame.mouse.get_pos()
			if mx>absx and mx<absx+self.width and my>absy and my<absy+self.height:
				return True
			else:
				return False
		else:
			return False

	def draw(self, p):
		p.blit(self.surface, (self.x, self.y))
