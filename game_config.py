import os

# level easy
# NUM_TILES_SIDE = 4
NUM_TILES_WIDTH = 7
NUM_TILES_HEIGHT = 4
IMAGE_SIZE = 220
# SCREEN_SIZE = 220 * NUM_TILES_SIDE
SCREEN_SIZE_WIDTH = 220 * NUM_TILES_WIDTH
SCREEN_SIZE_HEIGHT = 220 * NUM_TILES_HEIGHT

# NUM_TILES_TOTAL = NUM_TILES_SIDE ** 2
NUM_TILES_TOTAL = NUM_TILES_WIDTH * NUM_TILES_HEIGHT
MARGIN = 8

# level intermediate



ASSET_DIR = 'assets'
SOUND_DIR = 'sounds'
# ~ ASSET_FILES = [x for x in os.listdir(ASSET_DIR) if x[-3:].lower() == 'png']
ASSET_FILES = [x for x in os.listdir(ASSET_DIR) if x[-4:].lower() == 'jpeg']
print(ASSET_FILES)
# assert len(ASSET_FILES) == 8
assert len(ASSET_FILES) == 14
