import pygame
from Button import Button
from Menu import Menu

class ToolbarButton(Button):
	def __init__(self,x,y,text,parent, items=[]):
		Button.__init__(self, x,y,text,parent)
		self.show_menu = False
		self.menu = Menu(self.parent, self.x, 21, items)

	def render(self):
		# because this class is derived from Button, 
		# the render method is called before menu is defined
		# meaning I had to surround it in a try/except to
		# stop errors
		try:
			self.menu.x = self.x
		except:
			pass
			
		self.surface = pygame.Surface((self.width, self.height)).convert_alpha()
		self.surface.convert_alpha()
		self.surface.fill((0,0,0,0))
		self.surface.blit(self.font.render(self.text, True, (50,50,50)).convert_alpha(),(10,5))
