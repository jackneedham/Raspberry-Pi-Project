
import pygame
import StyleGuide

class Button:
	def __init__(self, x, y, text, parent, c=(150,150,150)):
		self.x = x
		self.y = y
		self.colour = c
		self.parent = parent
		self.text = text
		pygame.font.init()
		self.font = pygame.font.SysFont('Sans', StyleGuide.get_font_size())
		self.width, self.height = self.font.size(self.text)
		self.width += 20
		self.height += 10
		self.surface = pygame.Surface((self.width, self.height))
		self.render()

	def render(self):
		self.surface.fill(self.colour)
		r,g,b = self.colour
		ir = 255-r
		ig = 255-g
		ib = 255-b
		self.surface.blit(self.font.render(self.text, True, (ir,ig,ib)),(10,5))

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
		self.parent = p
		self.parent.blit(self.surface, (self.x, self.y))