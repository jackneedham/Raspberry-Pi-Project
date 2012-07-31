import pygame
from ToolbarButton import ToolbarButton
class Toolbar:
	def __init__(self, parent):
		self.parent = parent
		self.width = self.parent.get_width()
		self.height = 20
		self.surface = pygame.Surface((self.width, self.height))
		self.surface.fill((230,230,230))
		self.items = []
		self.render()

	def render(self):
		currentx = 0
		for item in xrange(len(self.items)):
			self.items[item].x = currentx
			self.surface.blit(self.items[item].surface, (self.items[item].x, 0))
			currentx += self.items[item].surface.get_width()

	def get_clicked(self, mouseclick):
		clicked = []
		for item in self.items:
			if item.show_menu:
				for menu_item in item.menu.items:
					if menu_item.is_clicked(item.x+menu_item.x, menu_item.y+21, mouseclick): # needs to be fed ABS positions
						clicked.append(menu_item)
		return clicked
	def draw(self):
		self.surface.fill((230,230,230))
		for item in self.items:
			item.draw(self.surface)
			if item.show_menu:
				item.menu.draw()

		self.parent.blit(self.surface, (0,0))
		pygame.draw.line(self.parent, (255,255,255), (0,self.height), (self.width,self.height))
