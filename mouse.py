from gpiozero import MCP3008, Button as GPIOButton
from pynput.mouse import Button, Controller

BUTTON_PIN = 13
mouse = Controller()
click = GPIOButton( BUTTON_PIN )
click.when_pressed = lambda: mouse.click( Button.left )

y = MCP3008( channel = 0 )
x = MCP3008( channel = 1 )

def AdjustMouseInput( x, y ):
	x = round( x, 1 )
	y = round( y, 1 )
	if x == 0.5 and y == 0.5:
		x = 0
		y = 0
	else:
		x *= x < 0.5 and -10 or 10
		y *= y < 0.5 and -10 or 10
	return x, y

if __name__ == "__main__":
	while True:
		xCord, yCord = AdjustMouseInput( x.value, y.value )
		mouse.move( xCord, yCord )
