import pygame

from GUI.Window import Window
from GUI.Canvas import Canvas

class CanvasWindow(Window):
	def __init__(self,x,y,p,img,title="Canvas Window"):
		w = img.get_width()
		h = img.get_height()+20
		Window.__init__(self,x,y,w,h,p,title)
		self.canvas = Canvas(0,20,self.width, self.height, img)
		self.old_cursor_x = 0
		self.old_cursor_y = 0
		self.drawing = False
		
	def draw(self):
		self.canvas.draw(self.surface)
		Window.draw(self)
		
	def update(self, mouseclick, scrolldown=False, scrollup=False, keypressed=''):
		if self.is_clicked():
			self.drawing = True
			mx,my = pygame.mouse.get_pos()
			mx -= self.x
			my -= self.y+20
			if mx>=0 and my>=0:
				if self.old_cursor_x != None:
					pygame.draw.line(self.canvas.surface, (0,0,0), (self.old_cursor_x,self.old_cursor_y), (mx, my),6)
				self.old_cursor_x = mx
				self.old_cursor_y = my
		else:
			self.old_cursor_x = None
			self.old_cursor_y = None
			
		Window.update(self, mouseclick, scrolldown, scrollup, keypressed)
		
