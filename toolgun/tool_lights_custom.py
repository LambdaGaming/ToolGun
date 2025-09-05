import random
import requests

NAME = "LED Web Server Remote"
MODE = 0
COLOR = ""
LED_SIZE = 200
HTML = """
	<input type="color" id="colorPicker" oninput="pywebview.api.SendData( { 1, colorPicker.value.substring( 1 ) } )">
	<label for="colorPicker">Custom Color</label><br><br>
	<button onclick="pywebview.api.SendData( { 2 } )">Random Single Color</button><br><br>
	<button onclick="pywebview.api.SendData( { 3 } )">Random Multi Color</button>
"""

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

def DataChanged( data ):
	global MODE, COLOR
	MODE = data[0]
	if data[1] is not None:
		convert = int( f"0x{data[1]}", 16 )
		COLOR = f"color={convert}"

def PullTrigger():
	global MODE, COLOR
	if MODE == 2:
		COLOR = RandomSingleColor()
	elif MODE == 3:
		COLOR = RandomMultiColor()
	requests.post( f"http://colorselector.local/state?{COLOR}" )
	print( "Applying color..." )
