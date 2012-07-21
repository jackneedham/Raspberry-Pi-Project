import pygame
from Button import Button

class WindowBar:
	def __init__(self, parent, absx, absy, title=None):
		self.x = 0
		self.y = 0
		self.absx = absx
		self.absy = absy
		self.parent = parent
		self.width = self.parent.get_width()
		self.height = 20
		self.surface = pygame.Surface((self.width, self.height))
		self.surface.fill((100,100,100))
		self.title = title
		if self.title != None:
			self.button = Button(0, 0, self.title, self.surface, (100,100,100))

	def isClicked(self):
		# doesn't actually check if clicked, just mouse over
		mx, my = pygame.mouse.get_pos()
		if mx > self.absx and mx < self.absx + self.width and my > self.absy and my < self.absy + self.height:
			return True

	def draw(self):
		if self.title != None:
			self.button.draw(self.surface)
		self.parent.blit(self.surface, (self.x, self.y))