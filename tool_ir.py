import serial
import time

ser = None

NAME = "Smart TV Remote"
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

def Open():
	global ser
	ser = serial.Serial( "/dev/ttyUSB0", 115200, timeout = 1 )
	ser.setDTR( False )
	time.sleep( 1 )
	ser.flushInput()
	ser.setDTR( True )
	time.sleep( 2 )

def Close():
	pass

def PullTrigger():
	global ser
	ser.write( "fire".encode() )

def ChangeData( index ):
	global ser
	ser.write( ( "address:" + ADDRESS ).encode() )
	ser.write( ( "command:" + DATA[index][1] ).encode() )
	ser.write( ( "protocol" + PROTOCOL ).encode() )
