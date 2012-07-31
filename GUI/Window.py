import pygame
from WindowBar import WindowBar
from ExitButton import ExitButton
class Window:
	def __init__(self, x, y, width, height, parent, title=None, fullcontrol=False):
		self.type = 'REGULAR'
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.parent = parent
		self.title = title
		self.fullcontrol = fullcontrol
		self.render()
		
		self.exit_btn = ExitButton(self.width-26, 0, "X", self.surface)
		self.exit_btn.x = self.width - self.exit_btn.width
		self.clicked = False

	def render(self):
		self.surface = pygame.Surface((self.width, self.height))
		self.surface.fill((255,255,255))
		self.bar = WindowBar(self.surface, self.x, self.y, self.title)

	def update(self, mouseclick, scrolldown=False, scrollup=False, keypressed=''):
		if self.is_clicked():
			if self.bar.is_clicked():
				if not self.clicked:
					self.clicked = True
					cx, cy = pygame.mouse.get_pos()
					self.offx = cx - self.x
					self.offy = cy - self.y
		if self.clicked:
			cx, cy = pygame.mouse.get_pos()
			self.x = cx-self.offx
			self.y = cy-self.offy
		if not pygame.mouse.get_pressed()[0] and self.clicked == True:
			self.render()
			self.clicked = False

	def is_clicked(self):
		if pygame.mouse.get_pressed()[0]:
			mx, my = pygame.mouse.get_pos()
			if mx > self.x and mx < self.x + self.width and my > self.y and my < self.y + self.height:
				return True
		else:
			return False

	def draw(self):
		self.bar.draw()
		self.exit_btn.draw(self.surface)
		# draw border
		pygame.draw.line(self.surface, (50,50,50), (0,0), (self.width-1, 0))
		pygame.draw.line(self.surface, (50,50,50), (0,0), (0,self.height))
		pygame.draw.line(self.surface, (50,50,50), (0, self.height-1), (self.width-1, self.height-1))
		pygame.draw.line(self.surface, (50,50,50), (self.width-1, 0), (self.width-1, self.height))
		self.parent.blit(self.surface, (self.x, self.y))
