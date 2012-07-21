import pygame

class ColorWheel:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.surface = pygame.image.load('img/colorwheel.png').convert_alpha()
		self.pointer_x = 75
		self.pointer_y = 75
		self.pointer = pygame.Surface((5,5)).convert_alpha()
		self.pointer.fill((0,0,0,125))
		self.clicked = False
	
	def is_clicked(self, absx, absy):
		if pygame.mouse.get_pressed()[0]:
			mx, my = pygame.mouse.get_pos()
			if self.clicked:
				self.pointer_x = mx-absx
				self.pointer_y = my-absy
				self.render()
			elif mx>self.pointer_x+absx and mx<self.pointer_x+absx+5 and my>self.pointer_y+absy and my<self.pointer_y+absy+5:
				self.clicked = True
		else:
			self.clicked = False
		return self.clicked

	def render(self):
		self.surface.fill((255,255,255))
		self.surface.blit(pygame.image.load('img/colorwheel.png').convert_alpha(), (0,0))
		self.pointer = pygame.Surface((5,5)).convert_alpha()
		self.pointer.fill((0,0,0,125))
	
	def draw(self, p):
		p.blit(self.surface, (self.x, self.y))
		p.blit(self.pointer, (self.x+self.pointer_x, self.y+self.pointer_y))
