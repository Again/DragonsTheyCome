# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor Boston, MA 02110-1301,  USA

import pygame, sys, os
from pygame.locals import *

class Screen:
	def __init__(self):
		print("Initialzing pygame...")
		pygame.init()
		self.window = pygame.display.set_mode((800, 480))
		pygame.display.set_caption('Dragons!  They come!')
		self.main_surface = pygame.display.get_surface()
		
		self.sprite_list = []
	
	def add_sprite(self, s):
		sprite_list.add(s)