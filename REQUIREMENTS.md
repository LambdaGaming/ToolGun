# Requirements
If you want to build a complete tool gun, these are all of the hardware requirements you will need. Once you have everything, you can follow [these instructions](SETUP.md) for assembling and configuring them.  
Please note that all hardware purchased for this project was available in the US at the time of purchase, but I cannot guarantee these items are available outside of the US or that they will remain in stock. If an item goes out of stock, let me know and I will replace it with a similar one if possible.  

# [3D Printed Gun Body](https://www.thingiverse.com/thing:4872305)
All of the parts for the main gun body were made by CPomeroy on Thingiverse. Everything except the grip was printed with black 1.75mm PLA filament at fine quality with 20% infill. The grip was printed with 1% infill with slightly thicker than normal walls. My original plan was to hide some electronic components in the grip but I ended up not doing that. Despite being nearly hollow it still holds up quite nicely. A wooden grip would be ideal, though.

# [Extra 3D Printed Parts](https://www.thingiverse.com/thing:5449959)
These are parts I made to go along with the main parts. They include a mount for the screen to fit into, a mount for the Pi, a rod to keep the cylinder in place, a cylinder to act as a fake A23 battery, and a pin to hold the trigger in place. Everything but the fake battery was printed with black 1.75mm PLA filament at normal quality with 100% infill. The fake battery was printed with silver 1.75mm PLA filament at normal quality with 20% infill, although the color doesn't really matter since you can't really see it once the decal is on it.

# [3D Printed Battery Holder](https://www.thingiverse.com/thing:4787641)
Holds the fake battery on the side of the gun. Made by sstoyanoff on Thingiverse. Printed with black 1.75mm PLA filament at fine quality with 20% infill.

# [Raspberry Pi](https://www.raspberrypi.com/products/)
Controls pretty much everything on the tool gun. For the best performance I recommend the Pi 4 or newer. I'm currently using a Pi 2 with 1 GB of RAM and it's pretty slow, especially when first starting up the program, but it does work. Just be aware if you do use a Pi 2, it does not have onboard WiFi so you will need a USB WiFi dongle to go with it.  
Raspberry Pi OS is the required operating system. Most Pis (if bought new) come with a microSD card with it installed, so you won't have to do much there. Just make sure you have sudo access since you will be installing a lot of things.  
I also recommend a having a wireless keyboard and mouse handy so you can still use the Pi normally once everything is assembled.

# [3.5" 480x320 Touch Screen Display](https://www.amazon.com/gp/product/B085PYS8P2/)
This is the screen used for the tool gun. It's not 100% accurate, but it's the closest I could find that isn't too big, too small, or incompatible with the Pi. Needs plugged into the Pi via GPIO for power and touch functionality, and HDMI for video. See the [wiring diagram](graphics/wiring.svg) for details.
## [Male to Female Breadboard Jumper Wires](https://www.amazon.com/gp/product/B01EV70C78/)
Colored wires used to connect the GPIO pins on the screen to the GPIO pins on the Pi, commonly found in Raspberry Pi and Arduino starter kits.
## HDMI Cable
The specific connectors depend on which model Pi you end up using. The Pi 4 and 5 use a micro HDMI to HDMI cable, while all other models use a regular HDMI cable. Some Raspberry Pi kits come with a cable but they are usually too long. If you want as little slack as possible I would get a 1 ft cable.

# [ESP32 Microcontroller](https://www.amazon.com/gp/product/B0718T232Z/)
Cheap but powerful microcontroller used to transmit IR data for tools that use it. Communicates with the Pi via WiFi. Other WiFi-enabled, Arduino-compatible microcontrollers should work, but I chose the ESP32 because of its small form factor and low price. It's possible to control IR directly through the Pi, but it's much more complicated compared to Arduino.
## Micro USB Male to USB Type A Male Cable
Simple 1 ft cable to connect the ESP32 to the Pi. Only used for power so data pins are not necessary unless you plan on making a tool that uses serial communication.

# Paper Decals
There are 3 paper decals I'm currently using. The decals for the battery and "flux capacitor" were taken from [Thingiverse.](https://www.thingiverse.com/thing:4872305) The schematic decal was taken from the game textures. The battery decal was measured to wrap around an A23 battery, and the "flux capacitor" decal was measured to wrap around a 9V battery. The schematic decal is 32x32mm.

# Copper Wire
I used a small amount of copper wire to wrap around the cylinder. Ideally it should be covering the whole thing but that's what I had lying around.

# Infrared Transmitter LED
Standard 5mm infrared transmitter LED. Make sure what you get is a transmitter and not a receiver. Transmitters can be clear or have a blueish tint. Receivers can be black or clear.

# Mini Pushbutton
Small 5mm pushbutton. The one I used was salvaged from an unused circuit board, but there are plenty of places you can buy them. The size __MUST__ be 5mm or smaller. Anything larger will not fit in the slot behind the trigger.

# Tape
I used 5 different kinds of tape for various applications. Packaging tape and electrical tape are used the most. I also used cloth tape and masking tape for the grip, and clear tape for the schematic decal. I recommend strapping/filament tape instead of packaging tape if you are trying to make it look as close to the original as possible.

# Screws & Nuts
3mm screws were used for the Pi mount and the base of the screen mount. 3 nuts were also used on the screws that hold the Pi to its mount.

# Glue
I used superglue and hot glue for assembly. Any brand should be fine for both.
