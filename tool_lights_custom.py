import random
import requests

SelectedData = 0
LED_SIZE = 200

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

NAME = "Custom Fairy String Remote"
DATA = [
	["Red", "color=16711680"],
	["Green", "color=65280"],
	["Blue", "color=255"],
	["Cyan", "color=65535"],
	["Yellow", "color=16776960"],
	["Magenta", "color=16711935"],
	["Black", "color=0"],
	["White", "color=16777215"],
	["Random Single Color", RandomSingleColor],
	["Random Multi Color", RandomMultiColor]
]

def Open():
	pass

def Close():
	pass

def PullTrigger():
	global SelectedData
	if callable( DATA[SelectedData][1] ):
		requests.post( f"http://colorselector.local/state?{DATA[SelectedData][1]()}" )
	else:
		requests.post( f"http://colorselector.local/state?{DATA[SelectedData][1]}" )

def ChangeData( index ):
	global SelectedData
	SelectedData = index
