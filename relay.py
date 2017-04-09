#VARIABLES

BRIGHT=8  #MIN 1, MAX 15
MESSAGE=["Achiredo!  STOP >> CONSUME >> MOVE  --> Ek Baar To Ride Lo :)  "]   # Edit the message to print


#############################################################################

import time
import math
from random import randrange
# Import library
import multilineMAX7219 as LEDMatrix
# Import fonts
from multilineMAX7219_fonts import CP437_FONT, SINCLAIRS_FONT, LCD_FONT, TINY_FONT
# The following imported variables make it easier to feed parameters to the library functions
from multilineMAX7219 import DIR_L, DIR_R, DIR_U, DIR_D
from multilineMAX7219 import DIR_LU, DIR_RU, DIR_LD, DIR_RD
from multilineMAX7219 import DISSOLVE, GFX_ON, GFX_OFF, GFX_INVERT
# Initialise the library and the MAX7219/8x8LED arrays
LEDMatrix.init()
try:
	LEDMatrix.brightness(BRIGHT)	#LEDMatrix.send_matrix_letter(0,0x48)
	LEDMatrix.scroll_message_horiz(MESSAGE)
except KeyboardInterrupt:
    # reset array
    LEDMatrix.scroll_message_horiz(["","Goodbye!",""], 1, 8)
    LEDMatrix.clear_all()
