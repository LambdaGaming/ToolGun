import eel
import psutil
import subprocess

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
	subprocess.run( ["amixer set Master " + setting], shell = True )

if __name__ == "__main__":
	eel.init( "web" )
	eel.start( "main.html", size = ( 256, 256 ), close_callback = lambda *args: None )
