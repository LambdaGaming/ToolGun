# These are the minimal variables and functions required for a tool.
# The file name of your tool must start with "tool_" for it to be recognized by the program.

# Name of the tool that gets displayed in the UI
NAME = "Base Tool"

# HTML code used in the file page. Ideally this should contain calls to JavaScript functions that link back to Python functions
HTML = """<p style="color:red; text-align:center">Nothing to see here...</p>"""

# Optional. Gets called immediately after the script loads
def Open():
	pass

# Optional. Gets called immediately before the script is terminated
def Close():
	pass

# Required. Gets called when the trigger button is pressed
def PullTrigger():
    pass

# You can also define your own functions and expose them to eel, so they can be called through JavaScript
