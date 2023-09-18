# Setup
This guide explains how to assemble and configure the tool gun. This is not a step-by-step guide. I only explain what I did using the parts I had. The steps you take might be different depending on the parts that are available to you and the methods you choose.  
I am not an engineer by any means, so expect weird methods of doing things, especially on the hardware side. If you have a better way of doing something, let me know and I'll update the guide.  
I also ended up omitting certain components either to reduce the complexity of the build, or because they physically wouldn't fit with the parts I have, so not everything seen on the original tool gun is included here.

# Software Setup
## [Main Program](https://github.com/lambdagaming/toolgun)
The main tool gun program can be downloaded by typing `git clone https://github.com/lambdagaming/toolgun` in the terminal. Once you have it downloaded, navigate to the directory it was saved in and type `python toolgun/main.py` in the terminal, or alternatively make the ToolGun.sh file 
executable and run it.

## Python 3.7+
The main program requires at least Python 3.7, which comes with Raspberry Pi OS by default, so you won't have to do anything there except install the required libraries, which you can do by opening the terminal, navigating to the tool gun directory, and entering `pip install -r requirements.txt`.

## Chromium Browser
Chromium also comes with the OS by default. You can install a different web browser if you'd like, just make sure you leave Chromium installed, as it is required to run the main program's UI.

## Screen
The Pi might detect the screen, but the touch feature will not work and the resolution will not set properly, so you will have to follow the instructions the manufacturer provides to download and install the driver. If you want the screen to display as portrait instead of landscape, there are a few more steps that need to be taken. You must add these AFTER the screen driver is installed, otherwise they will be overwritten:  
1. In the terminal, type `sudo nano /boot/config.txt`.
2. At the bottom of the file, enter these two lines:
	```
	display_rotate=3
	gpu_mem=128
	```
	Save the file and exit nano. The remaining steps below aren't required if your screen automatically recalibrates its touch feature for different orientations.
3. Back in the terminal, type `sudo nano /usr/share/X11/xorg.conf.d/99-calibration.conf`.
4. On line 4, swap the last two numbers of the `Calibration` option.
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
	Save the file, exit nano, and reboot your Pi to apply the changes.

## IR Transmitter Program
Located in the same repository as the main program, this program is used with the ESP32 to run the infrared circuit. You'll need to [install the ESP32 board](https://randomnerdtutorials.com/installing-the-esp32-board-in-arduino-ide-windows-instructions/), as well as the ESPAsyncWebServer, AsyncTCP, and IRremote libraries in the Arduino IDE for the program to compile and upload.


# Barrel
The front sight is superglued into the slot at the end of the barrel. Hot glue might work too. The larger end of the sight faces closest to the end of the barrel. The barrel also has packaging tape around it just before the sight. This tape is purely decorative and doesn't hold anything in place. The barrel itself is superglued to the main body.
## ESP32
The ESP32 is taped with packaging tape to the left side of the barrel, with the pins facing toward the barrel. The top pins sit on top of the barrel in such a way that allow breadboard wires to still be connected. It's powered by the Pi via USB, and also has a flux capacitor decal taped on top of it.
## Infrared Transmitter LED
The IR LED is inside the barrel with breadboard wires soldered to it. The positive wire is connected to pin 32 on the ESP32, and the negative wire is connected to a ground pin on the ESP32. Both wires are fed through a small hole that was drilled in the main body prior to assembly, and come out right behind the cylinder. Since the LED is being powered by the ESP32, its range isn't great, but it doesn't require a resistor. I might eventually change the circuit to give it more range, but for now it seems to work fine as long as the LED has direct line of sight of the sensor from less than 10 feet away.

# Main Body
This is the central part that mostly everything gets attached to. Aside from the parts discussed below, the main body also has a 3D printed battery terminal superglued to it. The fake battery, which is one of the extra parts, sits inside the terminal and is held in place by packaging tape. The fake battery also has a battery decal wrapped around and taped onto it.

## Cylinder
The cylinder has copper wire wrapped around it for decoration. Like I said in the requirements doc, the entire cylinder should be wrapped in a tight spool of thin wire, but a small amount of thick wire was what I had lying around. The cylinder is held in place with a 3D printed rod, which is one of the extra parts I made. The rod is held in place by the 3D printed dial, which was hot glued to both the rod and the main body.

## Pi Mount
The Pi mount, which is one of the extra parts, is screwed to the main body from the hole closest to the center. There is no screw hole on top of the main body, so one will need to be drilled. The size of the hole is 2.6mm. I ended up drilling through both the top of the body and the mount, and using a larger screw. I didn't use a nut because of the tight clearances, and so far is seems to be fairly stable. When drilling, make sure the mount is up against the screen mount.  
I covered the top of the screw with electrical tape to prevent exposing it to the circuitry on the bottom of the Pi. When mounting the Pi, I only used 3 out of the 4 holes since one of them is blocked by the ESP32. If you use nuts for the Pi screws make sure you __DO NOT__ over-tighten them. The Pi is not flat on the bottom so it will sit a little crooked on the mount. Over-tightening could risk breaking something on the board, or the board itself. The nuts only need to be tightened enough for them to not come loose when you gently shake the gun.

## Screen Mount
The base of the screen mount was superglued, screwed, and taped into place. The tape is more for decoration since the screw and superglue are more than capable of holding the base down on their own. The mount that the screen fits into is one of the extra parts. The screen is hot glued to the top of the mount, where the bottom of the screen's circuit board is flat and contains no electronics. When hot gluing, apply the glue to the mount and gently press the screen into the glue. I don't recommend applying glue directly to the screen as the heat from the tip could cause damage. Superglue can also cause damage, especially if you ever attempt to remove the screen, so I don't recommend that either.

## Trigger
The 3D printed trigger is held in place by a 3D printed pin, which is another one of the extra parts I made. The pin is kept in place by a small piece of electrical tape. The pushbutton for the trigger is pressed into a slot behind the trigger and hot glued to keep it in place. The button is wired to the Pi, with positive going to pin 3 and negative going to ground.

# Grip
The grip is superglued to the main body. I wrapped cloth tape around it 4 times and put 2 strips of masking tape vertically along the cloth tape on each side to match the original model.
