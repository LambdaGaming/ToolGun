# ToolGun
Fully working Garry's Mod toolgun using a Raspberry Pi.

# Features
## UI
 The UI is nearly identical to the one seen in-game. The biggest differences are that this one is actually interactive and includes more than one menu. Below is a complete list of UI features.
- 24-hour clock
- Audio mute status
- Scrolling text that displays the title of currently selected tool
- CPU and RAM usage stat
- CPU temperature stat
- Currently selected tool data
- File menu - Displays system and tool-specific data options
- Open menu - Displays list of tools
- Quit button

## Tools
Unfortunately, this tool gun is incapable of defying the laws of physics, but there are still lots of things to do with it. The main functionality of the tool gun comes from separate Python programs called tools, which are found in the Open menu. Every tool is designed to perform a single function, but the data that gets input into the function can be changed via the File menu. For example, the TV remote tool can only transmit IR codes and nothing else, but the specific code that gets sent can be configured. Much like the game, activating the tool with the selected data is done by pulling the trigger, which in this case is a simple GPIO button. By default, the tool gun only comes with a few tools, but you can easily create your own using the base provided.

### Current List of Tools
- Smart TV Remote
  - Sends signals to an ESP32 running a server that outputs the selected data as an IR signal for Samsung smart TVs

## Hardware
An extra Python program is included that allows you to use a joystick like a mouse, and a rotary encoder like a scroll wheel. More info about where they get mounted and how they are wired can be found in the requirements section below.

# Requirements
## Basic Functionality
These are required for basic functionality of the menu and main program.
- Raspberry Pi running Raspberry Pi OS or similar distribution (Works on the 400, other versions haven't been tested but should also work)
- Python 3.7+
- The following Python modules: eel, gpiozero, psutil, pynput
- Chromium Browser (For eel module)

## Extra Functionality
These are also required if you want to use the program as intended with default tools and extra hardware functionality.
- The following Python modules: requests
- ESP32 (Used for infrared function, any other WiFi-enabled microcontroller capable of running Arduino code should work too as long as you make the proper adjustments to the code)
- The following Arduino libraries: ESPAsyncWebServer, IRremote, WiFi
- Various electronic componenents for trigger, IR transmitter, joystick mouse, and rotary encoder scroll wheel (Specific part list and diagrams coming soon)
