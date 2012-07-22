import pygame

class Canvas:
	def __init__(self, x, y, w, h, surf):
		self.x = x
		self.y = y
		self.width = w
		self.heigth = h
		self.surface = surf

	def draw(self, p):
		p.blit(self.surface, (self.x,self.y))
