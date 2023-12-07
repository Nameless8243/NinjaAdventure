import os
import pygame
from settings import *

class Player(pygame.sprite.Sprite):
	def __init__(self,pos,groups,obstacle_sprites):
		super().__init__(groups)
        # Get the directory of the current file (tile.py)
		current_file_dir = os.path.dirname(os.path.abspath(__file__))
        # Build the absolute path to the rock.png image
		image_path = os.path.join(current_file_dir, '../graphics/test/player.png')
        # Ensure the path is in the correct format for the current operating system
		normalized_path = os.path.normpath(image_path)
        # Load the image using the normalized path
		self.image = pygame.image.load(normalized_path).convert_alpha()
		self.rect = self.image.get_rect(topleft=pos)
		#This was only, to load the picture...
######################################################################################

		self.speed = 5
		self.direction =pygame.math.Vector2() 		# if () is empty, it means X0, Y0

		self.obstacle_sprites = obstacle_sprites

	def input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_UP]:
			self.direction.y = -1  # Move up
		elif keys[pygame.K_DOWN]:
			self.direction.y = 1  # Move down
		else:
			self.direction.y = 0

		if keys[pygame.K_LEFT]:
			self.direction.x = -1  # Move left
		elif keys[pygame.K_RIGHT]:
			self.direction.x = 1  # Move right
		else:
			self.direction.x = 0

	def move(self, speed):
		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()

		self.rect.x += self.direction.x * speed
		self.collision("horizontal")
		self.rect.y += self.direction.y * speed
		self.collision("vertical")
		#self.rect.center += self.direction * speed

	def collision(self,direction):
		if direction == "horizontal":
			for sprite in self.obstacle_sprites:
				if sprite.rect.colliderect(self.rect):
					if self.direction.x > 0: #moving right
						self.rect.right = sprite.rect.left
					if self.direction.x < 0: #moving left
						self.rect.left = sprite.rect.right

		if direction == "vertical":
			for sprite in self.obstacle_sprites:
				if sprite.rect.colliderect(self.rect):
					if self.direction.y > 0: #moving down
						self.rect.bottom = sprite.rect.top
					if self.direction.y < 0: #moving up
						self.rect.top = sprite.rect.bottom
					

	def update(self):
		self.input()
		self.move(self.speed)