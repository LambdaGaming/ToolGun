# Setup
This guide lists everything I used to make the tool gun, and explains what configurations need to be made to them, if any, for them to work properly with this setup.  
Please note that all hardware used in this project was available in the US at the time of purchase, but I cannot guarantee these items are available outside of the US or will remain in stock. If an item goes out of stock, let me know and I will replace it with a similar one if possible.  
If you have little to no experience with Linux, the Raspberry Pi, and/or electronic circuits, I HIGHLY recommend you learn the basics before attempting to make this. I will not provide support for issues that can be resolved with a simple google search.

# [Raspberry Pi 4 B](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)
Controls pretty much everything on the tool gun. I personally recommend the Pi 4 with at least 4 GB of RAM for the best performance. I did test this on a Pi 2 with 1 GB of RAM and it worked, but it was VERY slow, especially when first starting the program, so I would recommend that as the bare minimum.  
Raspberry Pi OS is the required operating system. Most Pis (if bought new) come with a microSD card with it installed, so you don't have to do much there. Just make sure you have sudo access since you will be installing a lot of things.
The Pi is screwed to a [plate](https://www.thingiverse.com/thing:5449959), and the plate is screwed to the tool gun body, in front of the screen mount.

# [3.5" 480x320 Touch Screen Display](https://www.amazon.com/gp/product/B085PYS8P2/)
This is the screen used for the tool gun. It's not 100% accurate, but it's the closest I could find that isn't too big, too small, or incompatible with the Pi. For power and touch functionality, the screen needs plugged into the Pi's GPIO ports. See the wiring diagram for details. An HDMI cable also needs plugged into the screen and the Pi for video output.  
The Pi cannot detect the screen as a display device by default, so you will have to follow the instructions the manufacturer provides to download and install the driver. If you want the screen to display as portrait instead of landscape, there are a few more steps that need to be taken:  
1. In the terminal, type `sudo nano /boot/config.txt`.
2. At the bottom of the file, enter these two lines:
	```
		display_rotate=3
		gpu_mem=128
	```
	Save the file and exit nano. The remaining steps below aren't required if your screen automatically recalibrates its touch feature for different orientations.
3. Back in the terminal, type `sudo nano /usr/share/X11/xorg.conf.d/99-calibration.conf`.
4. On line 4, reverse the last two numbers of the `Calibration` option.
5. On line 5, change the value of the `SwapAxes` option from 1 to 0.  
6. Your config file should look something like this
	```
	Section "InputClass"
			Identifier      "calibration"
			MatchProduct    "ADS7846 Touchscreen"
			Option  "Calibration"   "170 3926 220 3917 "
			Option  "SwapAxes"      "0"
	EndSection
	```
	Save the file and exit nano.

# [ESP32 Microcontroller](https://www.amazon.com/gp/product/B0718T232Z/)
Cheap but powerful microcontroller used to transmit IR data for tools that use it. Communicates with the Pi via Wi-Fi and hosts a local server with the domain `toolgunremote.local`. Any Wi-Fi-enabled microcontroller capable of running Arduino code will theoretically work, but I chose the ESP32 because of its small form factor and low price. Eventually I hope to make the ESP32 communicate with the Pi via USB or GPIO to remove the network requirement.  
The ir_transmitter program will need uploaded to the ESP32 via the Arduino IDE or some other Arduino-compatible IDE. Make sure you include your Wifi details in the code before compiling. The only thing that gets wired to the ESP32 besides USB for power are the infrared and cyan LEDs.

# Main Program
The main program can be downloaded by opening the terminal and entering `git clone https://github.com/lambdagaming/toolgun`. You can also manually download it from GitHub in your web browser if you wish. Once you have it downloaded, simply navigate to the directory it was saved in and type `python main.py` in the terminal. 

# Python
The main program requires at least Python 3.7. Raspberry Pi OS comes with Python 3.7 by default, so you won't have to do anything there except install the required libraries, which you can do by opening the terminal, navigating to the tool gun directory, and entering `pip install -r requirements.txt`.

# Chromium Browser
Chromium comes with the OS by default. If you want to install a different web browser, you can, just make sure you leave Chromium installed, as it is required to run the tool gun's UI.

# 3D Printed Parts
Most of the tool gun is 3D printed using [models created by CPomeroy.](https://www.thingiverse.com/thing:4872305) I used black PLA with a 20% infill for everything and it holds up nicely. The grip should technically be made out of wood but I didn't feel like doing that for various reasons.  
All of the 3D printed parts are superglued together, except for the Pi and screen mounts, which are screwed to the main body. The top of the screen is hot glued to the mounting bracket that sits on top of the main body. I recommend using a low temperature hot glue gun to avoid damaging the screen.  

# LEDs
Five total LEDs are used on the tool gun. Two red and one green are used for the light box above the trigger. One infrared and one cyan are used for the IR transmitter and are located at the end of the barrel.

# Trigger
The trigger is held in place with a 3D printed pin 

# Decorative Parts
## Batteries
I decided to power the Pi from the wall for now, so the battery with the red decal is just a silver 3D printed block with same dimensions as an A23 battery. It's glued into a [holder created by sstoyanoff.](https://www.thingiverse.com/thing:4787641) The 9V battery decal hides the ESP32.

## Center Coil
I just wrapped some old copper wire around the cylinder, nothing fancy. The cylinder moves in game when the gun is fired but I decided to not add this function, at least for now.

## [Male to Female Breadboard Jumper Wires](https://www.amazon.com/gp/product/B01EV70C78/)
Colored wires used to connect the GPIO pins on the screen to the GPIO pins on the Pi, commonly found in Raspberry Pi and Arduino starter kits. They usually come stuck together so you shouldn't have to use glue or anything as long as you don't take them apart.  
I know they're not technically decorative since they serve a functional purpose but I'm including them here anyway since you don't *have* to use these specific wires, but they do very closely match the game model.

## Tape
Five different kinds of tape are used on the tool gun. The specific types are mostly irrelevant unless you're trying to be as authentic as possible.
### Packaging Tape
Strapping tape would have looked better but packaging tape was all I could find locally. It's used to hold the fake battery, ESP32, and the base of the screen bracket in place. It's also wrapped around part of the barrel just behind the sight.
### Cloth Tape
Wrapped around the grip.
### Masking Tape
Placed vertically on both sides of the grip, along the cloth tape.
### Electrical Tape
Single strip wrapped around the Pi and the barrel.
### Clear Tape
Not part of the game model but it's what I decided to use to hold the schematic in place on the screen since it looks like it's being held on by a magnet on the game model, which isn't possible with this setup.

## Light Box
Contains 3 LEDs that all serve different purposes. The bottom two are connected to the TX and RX pins on the Pi, and the top one is simply a power on indicator.
