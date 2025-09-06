import webview
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

class Api:
	def IsMuted( self ):
		sinkslist = subprocess.run( ["pacmd", "list-sinks"], stdout = subprocess.PIPE )
		result = subprocess.run( ["awk", "/muted/ { print $2 }"], stdout = subprocess.PIPE, input = sinkslist.stdout )
		return "yes" in result.stdout.decode( "utf-8" )

	def GetPerformanceStats( self ):
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
	
	def GetToolList( self ):
		return TOOL_LIST

	def ChangeTool( self, name ):
		global CURRENT_MODULE
		if "Close" in dir( CURRENT_MODULE ):
			CURRENT_MODULE.Close()
		CURRENT_MODULE = importlib.import_module( name )
		if "Open" in dir( CURRENT_MODULE ):
			CURRENT_MODULE.Open()
		mixer.music.load( "sounds/select.wav" )
		mixer.music.play()

	def SendData( self, data ):
		CURRENT_MODULE.SendData( data )

	def GetFilePage( self ):
		return CURRENT_MODULE.HTML

	def Shutdown( self ):
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

if __name__ == "__main__":
	PreloadTools()
	trigger.when_pressed = PullTrigger
	webview.create_window( "Tool Gun", "web/main.html", js_api=Api(), min_size=( 256, 256 ), maximize=True )
	webview.start( gui="gtk" )
