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
	["Red", "16711680"],
	["Green", "65280"],
	["Blue", "255"],
	["Cyan", "65535"],
	["Yellow", "16776960"],
	["Magenta", "16711935"],
	["Black", "0"],
	["White", "16777215"],
	["Random Single Color", RandomSingleColor],
	["Random Multi Color", RandomMultiColor]
]

def Open():
	pass

def Close():
	pass

def PullTrigger():
	global SelectedData
	if type( DATA[SelectedData] ) is function:
		requests.post( f"http://colorselector.local/state?{DATA[SelectedData]()}" )
	else:
		requests.post( f"http://colorselector.local/state?{DATA[SelectedData]}" )

def ChangeData( index ):
	global SelectedData
	SelectedData = index
