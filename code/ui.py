import pygame
from settings import *


class UI:
	def __init__(self):
		
		# general
		self.display_surface = pygame.display.get_surface()
		self.font = pygame.font.Font(UI_FONT,UI_FONT_SIZE)

		# bar setup
		self.health_bar_rect = pygame.Rect(10,10,HEALTH_BAR_WIDTH,BAR_HEIGHT) # (left,top,width,height)
		self.energy_bar_rect = pygame.Rect(10,34,ENERGY_BAR_WIDTH,BAR_HEIGHT) # (left,top,width,height)

		# convert weapon dictionary
		self.weapon_graphics = []
		for weapon in weapon_data.values():	#don't need the keys, only the values.
			path = weapon['graphic']	# I only need the graphic, .... save it in 'path'
			weapon = pygame.image.load(path).convert_alpha() # load the weapon picture
			self.weapon_graphics.append(weapon)	# append = add an element (weapon) to the 'self.weapon_graphics' list

		# convert magic dictionary
		self.magic_graphics = []
		for magic in magic_data.values():	#don't need the keys, only the values.
			path = magic['graphic']	# I only need the graphic, .... save it in 'path'
			magic = pygame.image.load(path).convert_alpha() # load the magic picture
			self.magic_graphics.append(magic)	# append = add an element (magic) to the 'self.magic_graphics' list

	def show_bar(self,current,max_amount,bg_rect,color):
		# draw bg
		pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect)

		# converting stat to pixel
		ratio = current / max_amount
		current_width = bg_rect.width * ratio
		current_rect = bg_rect.copy() # I have a rect in the same position and in the same height, but with a different width.
		current_rect.width = current_width

		# drawing the bar
		pygame.draw.rect(self.display_surface,color,current_rect) # this color is getting from the parameters (def show_bar(self.....color))
		pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,bg_rect,3) # the parameter 3 is the linewidth

	def show_exp(self,exp):
		text_surf = self.font.render(str(int(exp)),False,TEXT_COLOR) # (info,AntiAlias,color)
		x = self.display_surface.get_size()[0] - 20
		y = self.display_surface.get_size()[1] - 20
		text_rect = text_surf.get_rect(bottomright = (x,y))

		pygame.draw.rect(self.display_surface,UI_BG_COLOR,text_rect.inflate(20,20)) # .inflate(20,20) is making the rect bigger
		self.display_surface.blit(text_surf,text_rect)
		pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,text_rect.inflate(20,20),3) # border rect with a frame, width of 3

	def selection_box(self,left,top,has_switched):
		bg_rect = pygame.Rect(left,top,ITEM_BOX_SIZE,ITEM_BOX_SIZE)
		pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect) # Draw it
		if has_switched:
			pygame.draw.rect(self.display_surface,UI_BORDER_COLOR_ACTIVE,bg_rect,3)
		else:
			pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,bg_rect,3)
		return bg_rect

	def weapon_overlay(self,weapon_index,has_switched):	# weapon_index == player.py --> class:player --> self.weapon_index = 0
		bg_rect = self.selection_box(10,630,has_switched) # (left,top)
		weapon_surf = self.weapon_graphics[weapon_index]
		weapon_rect = weapon_surf.get_rect(center = bg_rect.center)

		self.display_surface.blit(weapon_surf,weapon_rect)

	def magic_overlay(self,magic_index,has_switched):	# magic_index == player.py --> class:player --> self.magic_index = 0
		bg_rect = self.selection_box(80,635,has_switched) # (left,top)
		magic_surf = self.magic_graphics[magic_index]
		magic_rect = magic_surf.get_rect(center = bg_rect.center)

		self.display_surface.blit(magic_surf,magic_rect)


	def display(self,player):
		#pygame.draw.rect(self.display_surface,'black',self.health_bar_rect) # (surface,color,rect)
		self.show_bar(player.health,player.stats['health'],self.health_bar_rect,HEALTH_COLOR)
		self.show_bar(player.energy,player.stats['energy'],self.energy_bar_rect,ENERGY_COLOR)

		self.show_exp(player.exp) # player.exp == player.py --> class:player --> self.exp

		self.weapon_overlay(player.weapon_index,not player.can_switch_weapon) # with 'not' we are checking an inverse of a variable.
		#self.selection_box(80,635) # for the magic
		self.magic_overlay(player.magic_index,not player.can_switch_magic)