import pygame
from Button import Button

class ExitButton(Button):
	def __init__(self, x, y, text, parent, c=(255,0,0)):
		Button.__init__(self, x, y, text, parent, c)
		self.font = pygame.font.SysFont('Calibri', 12)
		self.width -= 10
		self.height = 20
		self.surface = pygame.Surface((self.width, self.height))
		self.render()
	def render(self):
		self.surface.fill(self.colour)
		self.surface.blit(self.font.render(self.text, True, (255,255,255)),(5,5))