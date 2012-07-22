import pygame

class ColorWheel:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.surface = pygame.image.load('img/colorwheel.png').convert_alpha()
		self.pointer_x = 75
		self.pointer_y = 75
		self.pointer = pygame.Surface((10,10)).convert_alpha()
		self.pointer.fill((0,0,0,125))
		self.clicked = False
	
	def is_clicked(self, absx, absy):
		if pygame.mouse.get_pressed()[0]:
			mx, my = pygame.mouse.get_pos()
			if self.clicked:
				self.pointer_x = mx-absx
				self.pointer_y = my-absy
				self.render()
			elif mx>self.pointer_x+absx and mx<self.pointer_x+absx+10 and my>self.pointer_y+absy and my<self.pointer_y+absy+10:
				self.clicked = True
		else:
			self.clicked = False
		if self.pointer_x < 0:
			self.pointer_x = 0
		elif self.pointer_x > 137:
			self.pointer_x = 137
		if self.pointer_y < 0:
			self.pointer_y = 0
		elif self.pointer_y > 137:
			self.pointer_y = 137
		return self.clicked

	def render(self):
		self.surface.fill((255,255,255))
		self.surface.blit(pygame.image.load('img/colorwheel.png').convert_alpha(), (0,0))
		self.pointer = pygame.Surface((10,10)).convert_alpha()
		self.pointer.fill((0,0,0,125))
	
	def draw(self, p):
		p.blit(self.surface, (self.x, self.y))
		p.blit(self.pointer, (self.x+self.pointer_x, self.y+self.pointer_y))

	def get_color(self):
		try:
			return self.surface.get_at((self.pointer_x, self.pointer_y))
		except: # pokemon, catch 'em all
			return (0,0,0,0) # this is okay though, it's only one line
