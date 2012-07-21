import pygame

class Slider:
	def __init__(self, x, y, w, rang, title=None):
		self.title = title
		self.x = x
		self.y = y
		self.width = w
		self.lowest, self.heighest = rang
		self.slider_pos = 0
		self.offset_x = 0
		self.clicked = False
		self.render()
		
	def render(self):
		self.surface = pygame.Surface((self.width, 10))
		self.slider = pygame.Surface((10,10))
		self.slider.fill((255,0,255))

	def draw(self, parent):
		self.surface.fill((255,255,255))
		pygame.draw.line(self.surface, (0,0,0), (0,5), (self.width, 5))
		self.surface.blit(self.slider, (self.slider_pos, 0))
		parent.blit(self.surface, (self.x,self.y))
		
	def update(self, absx, absy):
		if not self.clicked:
			if self.is_clicked(absx+self.slider_pos, absy, 10, 10):
				self.clicked = True
				mx, my = pygame.mouse.get_pos()
				scrollx = absx+self.slider_pos
				self.offset_x = mx - scrollx
		else:
			mx, my = pygame.mouse.get_pos()
			self.slider_pos = mx - absx - self.offset_x
		if not pygame.mouse.get_pressed()[0]:
			self.clicked = False
		if self.slider_pos < 0:
			self.slider_pos = 0
		if self.slider_pos+10 > self.width:
			self.slider_pos = self.width-10
			
	
	def get_value(self):
		return (((0.0+self.slider_pos)/(self.width-10.0))*(self.heighest))+self.lowest
			
	def is_clicked(self,x,y,w,h):
		mx, my = pygame.mouse.get_pos()
		if pygame.mouse.get_pressed()[0]:
			if mx > x and mx < x+w and my > y and my< y+h:
				return True
			else:
				return False
		else:
			return False
