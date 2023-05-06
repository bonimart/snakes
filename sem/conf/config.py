from catppuccin import Flavour

BLOCK_SIZE = 40
HEIGHT = 20
WIDTH = 30
WIN_HEIGHT = BLOCK_SIZE*HEIGHT
WIN_WIDTH = BLOCK_SIZE*WIDTH

PALETTE = Flavour.mocha()
BACKGROUND_COLOR = PALETTE.crust.rgb
SNAKE_COLOR = PALETTE.green.rgb
FRUIT_COLOR = PALETTE.yellow.rgb
TEXT_COLOR = PALETTE.teal.rgba

FONT = "JetBrainsMono Nerd Font"

