import sys
from clustering import *

############################## getInput ######################################
# Purpose:
#   This is a Launcher for all the clustering sub-routines. It accepts input 
#   Integers to select and run each algorithm. 
# Parameters:
#   None
# Returns:
#   None
# Notes:
#   Infinite loop only ends with the selection of the 'cancel' option.
def getInput():
    kMeans, meanShift, PAM, cancel  = 0, 1, 2, 3
    
    data = [[2, 10], [2, 5], [8, 4], [5, 8], 
            [7, 5], [6, 4], [1, 2], [4, 9]]
    
    while(1):
        selection = int(input("[0] k-means\n[1]" +
                    " mean shift\n[2] PAM\n[3]Cancel\n"))
    
        if selection == kMeans:
            initClusterPoints = [(8, 4), (5, 8), (1, 2)]
            calculate_kMeans(data, 3, initClusterPoints, 0)
        if selection == meanShift: 
            calculate_meanShift(data, 2, 1)
        if selection == PAM:
            clusters = calculate_PAM(data, 3)
            #color_plot(data, clusters)
        if selection == cancel:
            print("Closing...")
            break
    
    
# Context the file is running in is __main__ 
if __name__ == "__main__":
    getInput()
