# These are the minimal variables and functions required for a tool.
# The file name of your tool must start with "tool_" for it to be recognized by the program.

# Name of the tool that gets displayed in the tool list
NAME = "Base Tool"

# HTML code used in the file page. Ideally this should contain calls to pywebview.api.SendData
HTML = """<p style="color:red; text-align:center">Nothing to see here...</p>"""

# Optional. Gets called immediately after the tool is selected
def Open():
	pass

# Optional. Gets called immediately before the tool is unloaded and a new one is selected
def Close():
	pass

# Optional. Data that you pass through the Javascript pywebview.api.SendData function will be sent here
def SendData( data ):
	pass

# Required. Gets called when the trigger button is pressed
def PullTrigger():
	pass
