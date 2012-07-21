import pygame

def get_font_size():
	size = 10
	A_width = 0
	while A_width <= 6.5:
		size += 1
		font = pygame.font.SysFont('Sans', size)
		A_width, h = font.size('A')
	return size+1