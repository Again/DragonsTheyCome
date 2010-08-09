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

import pygame, sys, os
from pygame.locals import * 

def setup_screen():
	window = pygame.display.set_mode((600, 480))
	pygame.display.set_caption('Dragons!  They come!')
	screen = pygame.display.get_surface() 

pygame.init()
setup_screen()
