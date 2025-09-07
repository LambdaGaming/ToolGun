# Tool Gun
Fully working and customizable Garry's Mod tool gun using a Raspberry Pi (and many other components).  

RIP Dav0r

<img src="graphics/ref1.jpg" width="25%"/>
<img src="graphics/ref4.png"/>

# Features
## UI
 The UI is nearly identical to the one seen in-game. The biggest differences are that this one is actually interactive and includes more than one menu. Below is a complete list of UI features.
- 24-hour clock
- Audio mute button
- Scrolling text that displays the title of currently selected tool
- Stats that display CPU usage, RAM usage, CPU temperature, and system uptime
- File menu - Displays custom menu defined by each tool
- Open menu - Displays list of tools
- Quit button

## Tools
Unfortunately, this tool gun is incapable of defying the laws of physics, but you can still do some fun things with it. The main functionality of the tool gun comes from separate Python programs called tools, which are found in the Open menu. Every tool is designed to perform one main function by pulling the trigger, which in this case is a simple GPIO button. The behavior of this function, as well as other functions, can be modified through the File menu, which is customized for each tool. For example, the Samsung TV Remote tool can only transmit IR codes with the Samsung protocol and nothing else, but the specific code that gets sent can be configured. By default, the tool gun only comes with a few tools, but you can easily create your own using the [base provided](toolgun/tool_base.py).

### Current List of Tools
- Samsung TV Remote
  - Has presets for standard Samsung TV remotes. Uses the IR transmitter.
- BrizLabs Fairy String Remote
  - Has presets for the [BrizLabs Fairy String Lights.](https://brizlabs.com/products/brizlabs-color-changing-fairy-lights-usb-plugin-with-32-keys-remote) Uses the IR transmitter.
- LED Web Server Remote
  - Has preset colors for [my LED Web Server.](https://github.com/LambdaGaming/LEDWebServer) The server is an ESP32 hooked up to the data wire of a BrizLabs fairy light string. It allows individual LEDs to be set to any color via an HTTP POST request.
- Get Position
  - Prints user's general location based on their IP (Only works if program was launched in a terminal)

# Building Your Own
If you want to make a tool gun yourself, everything you need is listed [here.](REQUIREMENTS.md) Once you have the required items, you can follow the setup instructions [here.](SETUP.md).  
If you have little to no experience with Linux, the Raspberry Pi, Arduinos, and/or electronic circuits, I HIGHLY recommend you learn the basics of each before attempting to make this, as the guides assume you're already familiar with these things. I will not provide support for issues you may encounter that aren't directly related to this project.
