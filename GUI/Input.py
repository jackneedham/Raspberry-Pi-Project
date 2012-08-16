import pygame
import StyleGuide

class Input:
	def __init__(self,x,y,w):
		self.x = x
		self.y = y
		self.width = w
		self.height = 20
		self.surface = pygame.Surface((self.width, self.height))
		self.text = 'Hello World'
		self.font = pygame.font.SysFont('Sans', StyleGuide.get_font_size())
		self.focused = False
		self.insertion_point = len(self.text)
		self.insertion_x = 0
		self.render()
	
	def render(self):
		self.surface.fill((255,255,255))
		if self.focused:
			col = (0,0,0)
		else:
			col = (200,200,200)
		t = []
		for l in self.text:
			t.append(l)
		self.text = t
		self.text.insert(self.insertion_point, '|')
		render = self.font.render(''.join(self.text), True, (0,0,0))
		self.text.remove('|')
		self.text = ''.join(self.text)
		
		self.surface.blit(render, (3,3))
		pygame.draw.line(self.surface, col, (0,0), (self.width, 0))
		pygame.draw.line(self.surface, col, (0,0), (0, self.height))
		pygame.draw.line(self.surface, col, (self.width-1,0), (self.width-1, self.height))
		pygame.draw.line(self.surface, col, (0,self.height-1), (self.width, self.height-1))
	
	
	def update(self, absx, absy, mouseclick, keypressed):
		oldval = self.focused
		if mouseclick:
			mx, my = pygame.mouse.get_pos()
			if mx>absx and mx<absx+self.width and my>absy and my<absy+self.height:
				self.focused = True
			else:
				self.focused = False

		if oldval!=self.focused:
			self.render()
		
		if self.focused:
			if keypressed != '':
				if keypressed == 'back':
					if self.text != '':
						t = []
						for l in xrange(len(self.text)):
							if l != self.insertion_point-1:
								t.append(self.text[l])
						self.text = "".join(t)
						self.insertion_point -= 1
				elif keypressed == 'left':
					self.insertion_point -= 1
				elif keypressed == 'right':
					self.insertion_point += 1
				else:
					t = []
					for l in self.text:
						t.append(l)
					t.insert(self.insertion_point, keypressed)
					self.text = "".join(t)
					self.insertion_point += 1
				self.render()
		
	def draw(self, parent):
		pygame.draw.line(self.surface, (100,100,100), (self.insertion_x, 2), (self.insertion_x,self.height-4))
		parent.blit(self.surface, (self.x, self.y))
		
		
