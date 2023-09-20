import eel
import requests

NAME = "Samsung TV Remote"
ADDRESS = "1799"
PROTOCOL = "Samsung"
DATA = [
	["Power", "2"], # [Name, IR command in base 10]
	["Source", "1"],
	["1", "4"],
	["2", "5"],
	["3", "6"],
	["4", "8"],
	["5", "9"],
	["6", "10"],
	["7", "12"],
	["8", "13"],
	["9", "14"],
	["-", "35"],
	["0", "17"],
	["Pre-Ch", "19"],
	["Volume Up", "7"],
	["Volume Down", "11"],
	["Mute", "15"],
	["Channel List", "107"],
	["Channel Up", "18"],
	["Channel Down", "16"],
	["Sleep", "3"],
	["Home", "121"],
	["Guide", "79"],
	["Settings", "26"],
	["Up", "96"],
	["Down", "97"],
	["Left", "101"],
	["Right", "98"],
	["Info", "31"],
	["Select", "104"],
	["Return", "88"],
	["Exit", "45"],
	["A", "108"],
	["B", "20"],
	["C", "21"],
	["D", "22"],
	["E-Manual", "63"],
	["P.Size", "62"],
	["CC/VD", "37"],
	["Stop", "70"],
	["Rewind", "69"],
	["Play", "71"],
	["Pause", "74"],
	["Fast Forward", "72"]
]

HTML = """
	<style>
		.fileContainer {
			display: inline-grid;
			grid-template-columns: repeat(auto-fit, 49%);
			column-gap:2%;
			row-gap:5px;
			margin: 0;
			padding: 0;
		}
	</style>
"""

for d in DATA:
	HTML += f"<button onclick='SetRemoteData( {d[1]} )'>{d[0]}</button>"

def PullTrigger():
	requests.post( "http://toolgunremote.local/fire" )
	print( "Firing IR emitter..." )
	
@eel.expose
def SetRemoteData( data ):
	requests.post( f"http://toolgunremote.local/change?address={ADDRESS}&command={data}&protocol={PROTOCOL.lower()}" )
	print( f"Changing data to {data}" )
