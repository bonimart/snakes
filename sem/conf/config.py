from catppuccin import Flavour

BLOCK_SIZE = 40
HEIGHT = 20
WIDTH = 30
WIN_HEIGHT = BLOCK_SIZE*HEIGHT
WIN_WIDTH = BLOCK_SIZE*WIDTH

PALETTE = Flavour.frappe()
BACKGROUND_COLOR = PALETTE.crust.rgb
SNAKE_COLOR_LIGHT = PALETTE.teal.rgb
SNAKE_COLOR_DARK = [color//2 for color in PALETTE.teal.rgb]
FRUIT_COLOR = PALETTE.peach.rgb
TEXT_COLOR = PALETTE.text.rgba

FONT = "JetBrainsMono Nerd Font"

