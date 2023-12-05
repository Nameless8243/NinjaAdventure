import os
import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        # Get the directory of the current file (tile.py)
        current_file_dir = os.path.dirname(os.path.abspath(__file__))
        # Build the absolute path to the rock.png image
        image_path = os.path.join(current_file_dir, '../graphics/test/rock.png')
        # Ensure the path is in the correct format for the current operating system
        normalized_path = os.path.normpath(image_path)
        # Load the image using the normalized path
        self.image = pygame.image.load(normalized_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)