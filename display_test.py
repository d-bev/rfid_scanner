import I2C_LCD_driver
from time import *

myLCD = I2C_LCD_driver.lcd()

myLCD.lcd_display_string("yo mama", 1)
