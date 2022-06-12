import eel
import importlib
from gpiozero import Button
import psutil
import subprocess
import sys

TRIGGER_BUTTON = 26
trigger = Button( TRIGGER_BUTTON, False )

CURRENT_PROGRAM = None
CURRENT_MODULE = importlib.import_module( "program_base" )
PROGRAM_LIST = [
	["Smart TV Remote", "program_ir"]
]

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
	sys.exit()

@eel.expose
def GetProgramList():
	return PROGRAM_LIST

def KillCurrentProgram():
	if CURRENT_PROGRAM is not None:
		CURRENT_PROGRAM.terminate()

@eel.expose
def StartProgram( name ):
	global CURRENT_PROGRAM, CURRENT_MODULE
	KillCurrentProgram()
	CURRENT_PROGRAM = subprocess.Popen( args = ["python3", f"{name}.py"], stdout = subprocess.PIPE )
	CURRENT_MODULE = importlib.import_module( name )
	trigger.when_pressed = CURRENT_MODULE.PullTrigger

@eel.expose
def ChangeFunction( func ):
    CURRENT_MODULE.ChangeFunction( func )

@eel.expose
def GetFunctionList():
    funclist = []
    for func in CURRENT_MODULE.FUNCTIONS:
        funclist.append( func[0] )
    return funclist

if __name__ == "__main__":
	eel.init( "web" )
	eel.start( "main.html", size = ( 256, 256 ), close_callback = lambda *args: None )
