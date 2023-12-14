import pygame
from settings import *
from entity import Entity
from support import *

class Enemy(Entity):		# inherited from entity, means it has the attributes of Entity
	def __init__(self,monster_name,pos,groups,obstacle_sprites):
		
		#general setup
		super().__init__(groups)
		self.sprite_type = 'enemy'

		# graphics setup
		self.import_graphics(monster_name)
		self.status = 'idle'
		self.image = self.animations[self.status][self.frame_index]

		# movement
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0,-10)
		self.obstacle_sprites = obstacle_sprites

		# stats
		self.monster_name = monster_name
		monster_info = monster_data[self.monster_name]
		self.health = monster_info['health']
		self.exp = monster_info['exp']
		self.speed = monster_info['speed']
		self.attack_damage = monster_info['damage']
		self.resistance = monster_info['resistance']
		self.attack_radius = monster_info['attack_radius']
		self.notice_radius = monster_info['notice_radius']
		self.attack_type = monster_info['attack_type']


		

	def import_graphics(self,name):
		self.animations = {'idle':[],'move':[],'attack':[]}		# we want to get (self.animations) dictionary and go for every single key of this dictionary: ('idle':[],'move':[],'attack':[])
		main_path = f'NinjaAdventure/graphics/monsters/{name}/' # this path leads to each individual enemy
		for animation in self.animations.keys():
			self.animations[animation] = import_folder(main_path + animation) # we get the animation from the for loop, this for loop can be idle, move or attack, we are combining them

	def get_player_distance_direction(self,player):
		enemy_vec = pygame.math.Vector2(self.rect.center)		# converting the center of our enemy into a vector
		player_vec = pygame.math.Vector2(player.rect.center)
		distance = (player_vec - enemy_vec).magnitude() # the magnitude is converting the vector to a distance

		if distance > 0:
			direction = (player_vec - enemy_vec).normalize()
		else:
			direction = pygame.math.Vector2()

		return (distance,direction)

	def get_status(self, player):
		distance = self.get_player_distance_direction(player)[0]		# [0] = we only care about distance, not direction

		if distance <= self.attack_radius:
			self.status = 'attack'
		elif distance <= self.notice_radius:
			self.status = 'move'
		else:
			self.status = 'idle'

	def actions(self,player):
		if self.status == 'attack':
			print('attack')
		elif self.status == 'move':
			self.direction = self.get_player_distance_direction(player)[1]	# [1] = now we only need the direction, and don't need the distance
		else:
			self.direction = pygame.math.Vector2()

	def update(self):
		self.move(self.speed)

	def enemy_update(self,player):
		self.get_status(player)
		self.actions(player)