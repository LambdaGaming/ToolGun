# These are the minimal variables and functions required for a ToolGun program.

FUNCTIONS = [
    ["Example Name", "Example data"] # Note that both the name and data must be a string
]

# Gets called when the trigger button is pressed
def PullTrigger():
    pass

# Gets called when the current function changes
def ChangeFunction( func ):
    pass

# Main function that keeps the script alive so that its functions can be called
if __name__ == "__main__":
    while True:
        pass
