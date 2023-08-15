import pdb
import random
import os
import game_config as gc

from pygame import image, transform

animals_count = dict((a, 0) for a in gc.ASSET_FILES)


def available_animals():
    return [animal for animal, count in animals_count.items() if count < 2]


def get_row_of_index(index):
    return index // gc.NUM_TILES_WIDTH


def get_col_of_index(index):
    return index % gc.NUM_TILES_WIDTH


def test(index):
    return index // gc.NUM_TILES_WIDTH, index % gc.NUM_TILES_HEIGHT

class Animal:
    def __init__(self, index):
        self.index = index
        self.name = random.choice(available_animals())
        self.image_path = os.path.join(gc.ASSET_DIR, self.name)
        self.sound_path = os.path.join(gc.SOUND_DIR, self.name.replace('.jpeg', '.wav'))
        self.row = get_row_of_index(index)
        self.col = get_col_of_index(index)
        self.skip = False
        self.image = image.load(self.image_path)
        self.image = transform.scale(self.image, (gc.IMAGE_SIZE - 2 * gc.MARGIN, gc.IMAGE_SIZE - 2 * gc.MARGIN))
        self.box = self.image.copy()
        self.box.fill((200, 200, 200))

        animals_count[self.name] += 1
