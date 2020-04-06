from lcdbackpack import LcdBackpack
import time


def connect():
	lcd = LcdBackpack("/dev/ttyACM0", 115200)
	lcd.connect()
	return lcd

def displaySongInfo(lcd, song, artist):
	lcd.clear()
	# print('----' + song + '----')
	# print('----' + artist + '----')
	# print(len(song),len(artist))

	song = song + ' '
	artist = artist + ' '

	if len(song) < 17:
		song = song + ( (16-len(song) ) * ' ' ) 
	if len(artist) < 17:
		artist = artist + ( (16-len(artist) ) * ' ' )

	if len(song) > len(artist):
		artist = artist + ( (len(song)-len(artist) ) * ' ' )
	else:
		song = song + ( (len(artist)-len(song) ) * ' ' )

	# print('----' + song + '----')
	# print('----' + artist + '----')
	# print(len(song),len(artist))

	lcd.set_cursor_position(1, 1)
	lcd.write(song[:16])
	lcd.set_cursor_position(1, 2)
	lcd.write(artist[:16])
	
def displayState(lcd, state)
	lcd.clear()
	lcd.set_cursor_position(1, 1)
	lcd.write(state[0])
	if len(state) > 1:
		lcd.set_cursor_position(1, 2)
		lcd.write(state[1])