import eel
from gpiozero import Button
import requests

STATS = [
    ["Function: ", ""]
]

CURRENT_FUNCTION = 0
FUNCTIONS = [
    ["Power", "2"], # [Name, IR command]
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

def PullTrigger():
    requests.post( "http://192.168.1.196/fire" )
    # TODO: Sound effects

@eel.expose
def ChangeFunction( func ):
    global CURRENT_FUNCTION
    CURRENT_FUNCTION = func
    requests.post( f"http://192.168.1.196/change?command={FUNCTIONS[CURRENT_FUNCTION][1]}" )
    # TODO: Send data to esp32 to change function

@eel.expose
def GetFunctionList():
    funclist = []
    for func in FUNCTIONS:
        funclist.append( func[0] )
    return funclist

TRIGGER_BUTTON = 26
trigger = Button( TRIGGER_BUTTON, False )
trigger.when_pressed = PullTrigger

if __name__ == "__main__":
    while True:
        pass
