import eel
import requests

NAME = "BrizLabs Fairy String Remote"
ADDRESS = "0"
PROTOCOL = "NEC"
DATA = [
	["On", "16"],
	["Off", "3"],
	["Auto", "1"],
	["Play/Pause", "6"],
	["4 Hour Timer", "9"],
	["6 Hour Timer", "29"],
	["8 Hour Timer", "31"],
	["Timer Off", "13"],
	["Red 1", "25"],
	["Red 2", "23"],
	["Orange", "64"],
	["Yellow", "10"],
	["Green 1", "27"],
	["Green 2", "18"],
	["Green 3", "76"],
	["Green 4", "30"],
	["Blue 1", "17"],
	["Blue 2", "22"],
	["Blue 3", "4"],
	["Blue 4", "14"],
	["White", "21"],
	["Purple 1", "77"],
	["Purple 2", "0"],
	["Purple 3", "26"],
	["Mode +", "28"],
	["Mode -", "20"],
	["Rainbow", "15"],
	["Halloween", "12"],
	["Dim 50%", "2"],
	["Dim 100%", "72"],
	["Speed +", "84"],
	["Speed -", "5"],
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
	HTML += f"<button onclick='SetBrizlabsData( {d[1]} )'>{d[0]}</button>"

def PullTrigger():
	requests.post( "http://toolgunremote.local/fire" )
	print( "Firing IR emitter..." )
	
@eel.expose
def SetBrizlabsData( data ):
	requests.post( f"http://toolgunremote.local/change?address={ADDRESS}&command={data}&protocol={PROTOCOL.lower()}" )
	print( f"Changing data to {data}" )
