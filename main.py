import eel
from gpiozero import Button
import importlib
import os
import psutil
from pynput.keyboard import Key, Controller
import subprocess

TRIGGER_BUTTON = 26
trigger = Button( TRIGGER_BUTTON, False )

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
		psutil.virtual_memory()[2]
	]
	tempfile.close()
	return stats

@eel.expose
def ToggleMute():
	setting = IsMuted() and "unmute" or "mute"
	subprocess.run( [f"amixer set Master {setting}"], shell = True )

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

@eel.expose
def GetToolList():
	return TOOL_LIST

@eel.expose
def ChangeTool( name ):
	global CURRENT_MODULE
	CURRENT_MODULE.Close()
	CURRENT_MODULE = importlib.import_module( name )
	CURRENT_MODULE.Open()
	trigger.when_pressed = CURRENT_MODULE.PullTrigger

@eel.expose
def ChangeData( index ):
    CURRENT_MODULE.ChangeData( index )

@eel.expose
def GetDataList():
    funclist = []
    for func in CURRENT_MODULE.DATA:
        funclist.append( func[0] )
    return funclist

if __name__ == "__main__":
	PreloadTools()
	eel.init( "web" )
	eel.start(
		"main.html",
		size = ( 256, 256 ),
		close_callback = lambda *args: None,
		cmdline_args = ["--force-device-scale-factor=1.25", "--start-maximized"] # Scale factor might need changed depending on the size of your screen
	)
