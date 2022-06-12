# ToolGun
Fully working Garry's Mod toolgun using a Raspberry Pi.

# Features
- Web UI that is nearly identical to the one seen in the game
  - Top bar
    - 24-hour clock
    - Audio mute status
  - Scrolling text
    - Displays title of currently selected program
  - Stats
    - CPU and RAM usage
    - CPU temperature
    - Currently selected program function
  - Bottom bar
    - File - Displays system and program-specific functions
    - Open - Displays list of programs
    - Quit - Exits the program
- Programs
  - Act like tools from the game
  - Programs can be selected via the Open menu
  - Program functions can be selected via the File menu
  - Only one program and function can be selected at a time
  - Function will activate when the trigger is pulled
  - Currently comes with one program: Smart TV Remote
    - Sends signals to an ESP32 running a server that outputs the selected function as an IR signal
- Joystick mouse
  - Joystick intended to be mounted on toolgun handle is used for moving the mouse to navigate the menu
  - Pressing down simulates a left click
- Scroll dial
  - Rotary dial mounted below where the screen goes on the toolgun is used for scrolling
  - Not yet implemented

# Requirements
## Basic Functionality
These are required for basic functionality of the menu and main program.
- Raspberry Pi running Raspberry Pi OS (Works on the 400, other versions haven't been tested but should also work)
- Python 3.7+
- The following Python modules: eel, gpiozero, psutil
- Chromium Browser (For eel module)

## Extra Functionality
These are also required if you want to use the program as intended with extra programs and extra hardware functionality.
- The following Python modules: requests, pynput
- ESP32 (Used for infrared function, any other WiFi-enabled microcontroller capable of running Arduino code should work too as long as you make the proper adjustments to the code)
- The following Arduino libraries: ESPAsyncWebServer, IRremote, WiFi
- Various electronic componenents for trigger, IR transmitter, and joystick mouse (Specific part list and diagrams coming soon)
