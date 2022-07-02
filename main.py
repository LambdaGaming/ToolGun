import eel
import importlib
from gpiozero import Button
import os
from pathlib import Path
import psutil
import subprocess
import sys

TRIGGER_BUTTON = 26
trigger = Button( TRIGGER_BUTTON, False )

CURRENT_PROGRAM = None
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
	KillCurrentProgram()
	sys.exit()

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

def KillCurrentProgram():
	if CURRENT_PROGRAM is not None:
		CURRENT_MODULE.Close()
		CURRENT_PROGRAM.terminate()

@eel.expose
def ChangeTool( name ):
	global CURRENT_PROGRAM, CURRENT_MODULE
	KillCurrentProgram()
	CURRENT_PROGRAM = subprocess.Popen( args = ["python3", f"{name}.py"], stdout = subprocess.PIPE )
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
	eel.start( "main.html", size = ( 256, 256 ), close_callback = lambda *args: None )
