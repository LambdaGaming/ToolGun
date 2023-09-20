import eel
import importlib
import os
import psutil
import subprocess
import time
from gpiozero import Button
from pygame import mixer
from pynput.keyboard import Key, Controller
from random import randint

mixer.init()
trigger = Button( 3 )

CURRENT_MODULE = importlib.import_module( "tool_base" )
TOOL_LIST = []

@eel.expose
def IsMuted():
	sinkslist = subprocess.run( ["pacmd", "list-sinks"], stdout = subprocess.PIPE )
	result = subprocess.run( ["awk", "/muted/ { print $2 }"], stdout = subprocess.PIPE, input = sinkslist.stdout )
	return "yes" in result.stdout.decode( "utf-8" )

@eel.expose
def GetPerformanceStats():
	tempfile = open( "/sys/class/thermal/thermal_zone0/temp" )
	cputemp = round( int( tempfile.read() ) / 1000 )
	stats = [
		psutil.cpu_percent(),
		cputemp,
		psutil.virtual_memory()[2],
		time.strftime( "%H:%M:%S", time.gmtime( time.monotonic() ) )
	]
	tempfile.close()
	return stats

@eel.expose
def Shutdown():
	keyboard = Controller()
	keyboard.press( Key.alt ) # HACK: This is the best way to close the browser window I can find since all other methods are either unsupported or blocked
	keyboard.press( Key.f4 )
	keyboard.release( Key.alt )
	keyboard.release( Key.f4 )
	exit()

# Imports all tools to get their names, might also help with performance when tools get switched
def PreloadTools():
	for file in os.listdir():
		if os.path.isfile( file ) and "tool_" in file and file != "tool_base.py":
			filename = file.split( '.' )[0]
			tempmodule = importlib.import_module( filename )
			TOOL_LIST.append( [tempmodule.NAME, filename] )

def PullTrigger():
	CURRENT_MODULE.PullTrigger()
	mixer.music.load( f"sounds/shoot{randint( 1, 2 )}.wav" )
	mixer.music.play()

@eel.expose
def GetToolList():
	return TOOL_LIST

@eel.expose
def ChangeTool( name ):
	global CURRENT_MODULE
	if "Close" in dir( CURRENT_MODULE ):
		CURRENT_MODULE.Close()
	CURRENT_MODULE = importlib.import_module( name )
	if "Open" in dir( CURRENT_MODULE ):
		CURRENT_MODULE.Open()
	mixer.music.load( "sounds/select.wav" )
	mixer.music.play()

@eel.expose
def GetFilePage():
	return CURRENT_MODULE.HTML

if __name__ == "__main__":
	PreloadTools()
	trigger.when_pressed = PullTrigger
	eel.init( "web" )
	eel.start(
		"main.html",
		size = ( 256, 256 ),
		close_callback = lambda *args: None,
		cmdline_args = ["--force-device-scale-factor=1.25", "--start-maximized"] # Scale factor might need changed depending on the size of your screen
	)
