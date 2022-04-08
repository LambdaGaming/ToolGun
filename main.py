import eel
@eel.expose
def IsMuted():
	sinkslist = subprocess.run( ["pacmd", "list-sinks"], stdout = subprocess.PIPE )
	result = subprocess.run( ["awk", "/muted/ { print $2 }"], stdout = subprocess.PIPE, input = sinkslist.stdout )
	return "yes" in result.stdout.decode( "utf-8" )

if __name__ == "__main__":
	eel.init( "web" )
	eel.start( "main.html", size = ( 256, 256 ) )
