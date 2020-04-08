from lcdbackpack import LcdBackpack
import time


def connect():
	lcd = LcdBackpack("/dev/ttyACM0", 115200)
	lcd.connect()
	return lcd
	
def displayState(lcd, state):
	lcd.clear()
	state = [item.replace("’", "") for item in state]
	lcd.set_cursor_position(1, 1)
	lcd.write(state[0])
	if len(state) > 1:
		lcd.set_cursor_position(1, 2)
		lcd.write(state[1])

  