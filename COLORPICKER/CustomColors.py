import pygame

from ColorButton import ColorButton

class CustomColors:
	def __init__(self, x, y, w):
		self.x = x
		self.y = y
		self.width = w
		self.height = 50
		self.surface = pygame.Surface((self.width, self.height))
		self.grid = []
		for x in range(2):
			for i in range(8):
				self.grid.append(ColorButton(i*25,25*x,(212,212,212)))
		self.grid[0].color = (255,255,0)
		self.grid[0].surface.fill(self.grid[0].color)


	def draw(self, parent):
		for colorbtn in self.grid:
			colorbtn.draw(self.surface)		
		pygame.draw.line(self.surface, (100,100,100), (0,25), (self.width,25))
		pygame.draw.line(self.surface, (100,100,100), (0,0), (self.width,0))
		pygame.draw.line(self.surface, (100,100,100), (0,49), (self.width,49))
		pygame.draw.line(self.surface, (100,100,100), (self.width-1,0), (self.width-1,50))
		for i in range(8):
			pygame.draw.line(self.surface, (100,100,100), (25*i, 0), (25*i,50))
		parent.blit(self.surface, (self.x, self.y))
