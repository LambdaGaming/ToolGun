from gpiozero import MCP3008, Button as GPIOButton
from pynput.mouse import Button, Controller
import time

BUTTON_PIN = 13
mouse = Controller()
click = GPIOButton( BUTTON_PIN )
click.when_pressed = lambda: mouse.click( Button.left )

y = MCP3008( channel = 0 )
x = MCP3008( channel = 1 )

def AdjustMouseInput( x, y ):
    x = round( x, 1 )
    y = round( y, 1 )
    if x == 0.5 and y == 0.5: # Center
        x = 0
        y = 0
    elif x == 0 and y == 0.5: # Up
        x = 1
        y = 0
    elif x == 1 and y == 0.5: # Down
        x = -1
        y = 0
    elif x == 0.5 and y == 1: # Left
        x = 0
        y = -1
    elif x == 0.5 and y == 0: # Right
        x = 0
        y = 1
    return x, y

if __name__ == "__main__":
    while True:
        xCord, yCord = AdjustMouseInput( x.value, y.value )
        mouse.move( xCord, yCord )
        #time.sleep(1)
