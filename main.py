import pygame as pg
import random
from settings import *

class Game:
	def __init__(self):
		# initialize game window, etc.
		pg.init()
		pg.mixer.init()
		self.screen = pg.display.set_mode((WIDTH, HEIGHT))
		pg.display.set_caption(TITLE)
		self.clock = pg.time.Clock()
		self.running = True

	def new(self):
		# start a new game 
		pass

	def run(self):
		# Game loop
		self.playing = True # Can be equal to false to stop the game
		while self.playing:
			self.clock.tick(FPS)
			self.events()
			self.update()
			self.draw()

	def update(self):
		# Game loop - Update
		pass

	def events(self):
		# Game loop - Events
		for event in pg.event.get():
		# check for closing the window
			if event.type == pg.QUIT:
				if self.playing:
					self.playing = False
				self.running = False

	def draw(self):
		# Game loop - Render / Draw
		self.screen.fill(BLUE)
		# *after* drawing everything, flip the display 
		pg.display.flip()

	def show_start_screen(self):
		# game start screen
		pass

	def show_go_screen(self):
		# game over / continue
		pass

g = Game()
g.show_start_screen()
while g.running:
	g.new()
	g.show_go_screen()