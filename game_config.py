import os

IMAGE_SIZE = 220
SCREEN_SIZE = 220 * 4
NUM_TILES_SIDE = 4
NUM_TILES_TOTAL = 16
MARGIN = 8

ASSET_DIR = 'assets'
SOUND_DIR = 'sounds'
# ~ ASSET_FILES = [x for x in os.listdir(ASSET_DIR) if x[-3:].lower() == 'png']
ASSET_FILES = [x for x in os.listdir(ASSET_DIR) if x[-4:].lower() == 'jpeg']
print(ASSET_FILES)
assert len(ASSET_FILES) == 8
