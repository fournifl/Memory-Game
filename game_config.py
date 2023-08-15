import os

NUM_TILES_SIDE = 4

IMAGE_SIZE = 220
SCREEN_SIZE = 220 * NUM_TILES_SIDE
NUM_TILES_TOTAL = NUM_TILES_SIDE ** 2
MARGIN = 8  

ASSET_DIR = 'assets'
SOUND_DIR = 'sounds'
# ~ ASSET_FILES = [x for x in os.listdir(ASSET_DIR) if x[-3:].lower() == 'png']
ASSET_FILES = [x for x in os.listdir(ASSET_DIR) if x[-4:].lower() == 'jpeg']
print(ASSET_FILES)
assert len(ASSET_FILES) == 8
