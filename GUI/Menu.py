import pygame
from Button import Button

class Menu:
	def __init__(self, parent, x, y, items):
		self.x = x
		self.y = y
		self.parent = parent

		# this builds the list of strings into a list of buttons
		self.items = []
		offy = 0 # this is used to offset the y
		largest_w = 0
		for item in items:
			new_item = Button(self.x, offy, item, self.parent, (255,255,255))
			offy += new_item.surface.get_height()
			if new_item.surface.get_width() > largest_w:
				largest_w = new_item.surface.get_width()
			self.items.append(new_item)

		self.height = offy
		self.width = largest_w

		self.surface = pygame.Surface((self.width, self.height))
		self.surface.fill((255,255,255))

		self.render()

	def render(self):
		for item in self.items:
			item.draw(self.surface)

	def draw(self):
		self.surface.fill((255,255,255))
		self.render()
		self.parent.blit(self.surface, (self.x, self.y))