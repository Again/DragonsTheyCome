#!/usr/bin/python
#
# main.py
# Copyright (C) David J Wiebe 2010 <davidwiebe2@gmail.com>
# 
# DragonsTheyCome is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# DragonsTheyCome is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

import game_screen, level
import pygame, sys, os
from pygame.locals import *

class Sprite(pygame.sprite.Sprite):
	def __init(self):
		pygame.sprite.Sprite.__init__(self)
	
	def update(self):
		print("Updating")

class Player():
	def __init(self):
		#TODO write Player constructor
		print("create player constructor")
	
	def button_pushed(self, keystate):
		if keystate[K_UP]:
			print("up")
		elif keystate[K_DOWN]:
			print("down")
		elif keystate[K_LEFT]:
			print("left")
		elif keystate[K_RIGHT]:
			print("right")

def main():
	screen = game_screen.Screen()
	current_level = level.Level()
	player = Player()
	clock = pygame.time.Clock()

	run = True
	while run:
		events = pygame.event.get()
		
		for event in events:
			if event.type == QUIT:
				run = False
			
			keystate = pygame.key.get_pressed()
			player.button_pushed(keystate)
			
		pygame.display.flip()
		clock.tick(30)
	        
if __name__ == "__main__":
    main()