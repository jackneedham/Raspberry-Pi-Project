import pygame

from GUI.Window import Window
from GUI.Canvas import Canvas

class CanvasWindow(Window):
	def __init__(self,x,y,p,img,title="Canvas Window"):
		w = img.get_width()
		h = img.get_height()
		Window.__init__(self,x,y,w,h,p,title)
		self.canvas = Canvas(0,20,self.width, self.height, img)
		
	def draw(self):
		self.canvas.draw(self.surface)
		Window.draw(self)
