# These are the minimal variables and functions required for a tool. Please note that even if you don't use all of the functions, they must remain in the code!

NAME = "Base Tool" # Name of the tool that gets displayed in the UI

DATA = [
    ["Example Name", "Example data"] # The name needs to be a string, but the data can be anything you'd like as it's only used by this script
]

# Gets called immediately after the script loads
def Open():
	pass

# Gets called immediately before the script is terminated
def Close():
	pass

# Gets called when the trigger button is pressed
def PullTrigger():
    pass

# Gets called when the current data changes; The index parameter is the index of the selected value in the data array
def ChangeData( index ):
    pass

# Main function that keeps the script alive so that its functions can be called
if __name__ == "__main__":
    while True:
        pass
