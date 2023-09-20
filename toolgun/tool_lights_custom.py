import eel
import random
import requests

MODE = 0
COLOR = ""
LED_SIZE = 200

@eel.expose
def ChangeColorMode( mode, color = None ):
	global MODE, COLOR
	MODE = mode
	if color is not None:
		convert = int( f"0x{color}", 16 )
		COLOR = f"color={convert}"

def RandomSingleColor():
	rand = random.randint( 0, 0xFFFFFF )
	url = f"color={rand}"
	return url

def RandomMultiColor():
	url = ""
	for i in range( LED_SIZE - 1 ):
		rand = random.randint( 0, 0xFFFFFF )
		url += f"led{i}={rand}&"
	return url

NAME = "LED Web Server Remote"
HTML = """
	<input type="color" id="colorPicker" oninput="eel.ChangeColorMode( 1, colorPicker.value.substring( 1 ) )">
	<label for="colorPicker">Custom Color</label><br><br>
	<button onclick="eel.ChangeColorMode( 2 )">Random Single Color</button><br><br>
	<button onclick="eel.ChangeColorMode( 3 )">Random Multi Color</button>
"""

def PullTrigger():
	global MODE, COLOR
	if MODE == 2:
		COLOR = RandomSingleColor()
	elif MODE == 3:
		COLOR = RandomMultiColor()
	requests.post( f"http://colorselector.local/state?{COLOR}" )
	print( "Applying color..." )
