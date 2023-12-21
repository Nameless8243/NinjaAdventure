import os
import pygame
from settings import *

class Player(pygame.sprite.Sprite):
	def __init__(self,pos,groups,obstacle_sprites):
		super().__init__(groups)
		self.image = pygame.image.load('NinjaAdventure/graphics/test/player.png').convert_alpha()
		self.rect = self.image.get_rect(topleft=pos)
		self.hitbox = self.rect.inflate(0,-26)


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

		self.hitbox.x += self.direction.x * speed
		self.collision("horizontal")
		self.hitbox.y += self.direction.y * speed
		self.collision("vertical")
		self.rect.center = self.hitbox.center


	def collision(self,direction):
		if direction == "horizontal":
			for sprite in self.obstacle_sprites:
				if sprite.hitbox.colliderect(self.hitbox):
					if self.direction.x > 0: #moving right
						self.hitbox.right = sprite.hitbox.left
					if self.direction.x < 0: #moving left
						self.hitbox.left = sprite.hitbox.right

		if direction == "vertical":
			for sprite in self.obstacle_sprites:
				if sprite.hitbox.colliderect(self.hitbox):
					if self.direction.y > 0: #moving down
						self.hitbox.bottom = sprite.hitbox.top
					if self.direction.y < 0: #moving up
						self.hitbox.top = sprite.hitbox.bottom
					

	def get_full_magic_damage(self):
		base_damage = self.stats['magic']
		spell_damage = magic_data[self.magic]['strength']
		return base_damage + spell_damage

	def energy_recovery(self):
		if self.energy < self.stats['energy']:
			self.energy += 0.01 * self.stats['magic']
		else:
			self.energy = self.stats['energy']

	def update(self):
		self.input()
<<<<<<< Updated upstream
		self.move(self.speed)
=======
		self.cooldowns()
		self.get_status()
		self.animate()
		self.move(self.speed)
		self.energy_recovery()
>>>>>>> Stashed changes
