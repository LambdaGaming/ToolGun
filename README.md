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

# Setup
If you want to make a tool gun yourself, I layed out everything you need in [SETUP.md](SETUP.md).
