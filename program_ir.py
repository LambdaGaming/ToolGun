from gpiozero import Button

TRIGGER_BUTTON = 26
trigger = Button( TRIGGER_BUTTON, False )
trigger.when_pressed = lambda: print( "Pressed" )

if __name__ == "__main__":
    while True:
        pass
