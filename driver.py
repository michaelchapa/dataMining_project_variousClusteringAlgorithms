import sys
from clustering import *

def getInput():
    selection = int(input("[0] k-means\n[1] mean shift\n[2] PAM\n"))
    
    assert type(selection) is int, \
        "Input either integer: 0, 1, 2, 3; Press ENTER;"
    
    if selection == 0:
        main()
    if selection == 1: 
        print("Mean Shift")
    if selection == 2:
        print("PAM")
    
    
def launcher():
    getInput()
    
    
# Context the file is running in is __main__ 
if __name__ == "__main__":
    launcher()