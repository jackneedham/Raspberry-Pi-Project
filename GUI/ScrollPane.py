import pygame

class ScrollPane:
	def __init__(self, x, y, w, h, ch):
		self.x = x
		self.y = y
		self.width = w
		self.height = h
		self.content_height = ch
		self.clicked = False
		self.scrolldown = False
		self.scrollup = False
		self.render()
	def render(self):
		self.content_y = 0
		self.surface = pygame.Surface((self.width, self.height))
		self.surface.fill((255,255,255))
		self.content_surface = pygame.Surface((self.width, self.content_height)) # for testing purposes
		self.content_surface.fill((255,255,255))
		self.scrollbar_surface = pygame.Surface((10, self.height/((self.content_surface.get_height()+0.0)/(self.height+0.0))))
		self.scrollbar_surface.fill((50,50,50))
		self.scrollspace = self.height - self.scrollbar_surface.get_height()
		self.scrollbar_pos = 0

	def update(self, absx, absy):
		if not self.clicked:
			if self.is_clicked(absx+self.width-10, absy+self.scrollbar_pos, 10, self.scrollbar_surface.get_height()):
				self.clicked = True
				mx, my = pygame.mouse.get_pos()
				scrolly = absy+self.scrollbar_pos
				self.offset_y = my - scrolly
		else:
			mx, my = pygame.mouse.get_pos()
			self.scrollbar_pos = my - absy - self.offset_y
		if not pygame.mouse.get_pressed()[0]:
			self.clicked = False
		if self.scrollbar_pos < 0:
			self.scrollbar_pos = 0
		if self.scrollbar_pos > self.scrollspace:
			self.scrollbar_pos = self.scrollspace
		self.content_y = -1*(((self.scrollbar_pos+0.0)/(self.height))*(self.content_height+0.0))
		if self.scrolldown:
			self.content_y -= 5
			self.scrollbar_pos += 5
			self.scrolldown = False
		if self.scrollup:
			self.content_y += 5
			self.scrollbar_pos -= 5
			self.scrollup = False
		if self.scrollbar_pos == 0:
			self.content_y = 0




	def is_clicked(self,x,y,w,h):
		mx, my = pygame.mouse.get_pos()
		if pygame.mouse.get_pressed()[0]:
			if mx > x and mx < x+w and my > y and my< y+h:
				return True
			else:
				return False
		else:
			return False

	def draw(self, p):
		self.surface.fill((255,255,255))
		self.surface.blit(self.content_surface, (0,self.content_y))
		self.surface.blit(self.scrollbar_surface, (self.width-10,self.scrollbar_pos))
		pygame.draw.line(self.surface, (200,200,200), (0,0), (self.width, 0))
		pygame.draw.line(self.surface, (200,200,200), (0,0), (0, self.height))
		pygame.draw.line(self.surface, (200,200,200), (self.width-1,0), (self.width-1, self.height))
		pygame.draw.line(self.surface, (200,200,200), (0,self.height-1), (self.width, self.height-1))
		pygame.draw.line(self.surface, (200,200,200), (self.width-10, 0), (self.width-10, self.height-1))
		p.blit(self.surface, (self.x, self.y))

