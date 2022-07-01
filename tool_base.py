# These are the minimal variables and functions required for a tool.

DATA = [
    ["Example Name", "Example data"] # The name MUST be a string, but the data can be anything you'd like as it's only used by the tool itself
]

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
