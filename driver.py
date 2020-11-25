import sys
from clustering import *
from sklearnRuns import *

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
    kMeans, meanShift, PAM, runSklearn, cancel  = 0, 1, 2, 3, 4
    test, big = 0, 1
    bigData = pd.DataFrame('https://raw.githubusercontent.com/Davin-U/csv_files/master/hwk09.csv').to_numpy()
    testData = [[2, 10], [2, 5], [8, 4], [5, 8], 
            [7, 5], [6, 4], [1, 2], [4, 9]]
    
    
    while(1):
        selection = int(input("[0] K-Means\n[1] Mean Shift\n" +
                    "[2] PAM\n[3] Run Sklearn\n[4] Cancel\n"))
        
        dataChoice = int(input("[0] Test Data (8 points)\n" +
                            "[1] Big Data (1500 points)\n"))
        if dataChoice == test:
            dataSet = testData
            initClusterPoints = [(8, 4), (5, 8), (1, 2)]
        if dataChoice == big:
            dataSet = bigData
            initClusterPoint = [bigData[0], bigData[501], bigData[1001]]
        if selection == kMeans:
            print("K-Means run: ")
            calculate_kMeans(dataSet, initClusterPoints, 0)
        if selection == meanShift: 
            print("Mean Shift run: ")
            bandwidth = int(input("Enter bandwidth integer value:\n"))
            calculate_meanShift(dataSet, bandwidth, 1)
        if selection == PAM:
            print("PAM run: ")
            clusters = calculate_PAM(dataSet, 3)
            color_plot(dataSet, clusters)
        if selection == runSklearn:
            getSklearnInput()
        if selection == cancel:
            print("Closing...")
            break


############################## getSklearnInput ###############################
# Purpose:
#   This is a Launcher for all the Scikit Learn clustering sub-routines. 
#   It accepts input Integers to select and run each algorithm. 
# Parameters:
#   None
# Returns:
#   None
# Notes:
#   Infinite loop only ends with the selection of the 'cancel' option.    
def getSklearnInput():
    kMeans, meanShift, PAM, cancel = 0, 1, 2, 3
    data = [[2, 10], [2, 5], [8, 4], [5, 8], 
            [7, 5], [6, 4], [1, 2], [4, 9]]
    
    while(1):
        selection = int(input("[0] Sklearn K-Means\n[1] Sklearn Mean Shift\n" +
                    "[2] Sklearn PAM\n[3] Cancel\n"))
        print()
    
        if selection == kMeans:
            initClusterPoints = [[8, 4], [5, 8], [1, 2]]
            initClusterPoints = np.array(initClusterPoints)
            print("sklearn K-Means run: ")
            k = int(input("Enter k integer value:\n"))
            sklearn_kMeans(data, k)
        if selection == meanShift:
            bandwidth = int(input("Enter bandwidth integer value:\n"))
            sklearn_meanShift(data, bandwidth)
        if selection == PAM:
            print("sklearn PAM run: ")
            clusters = sklearn_PAM(data, k)
            color_plot(data, clusters)
        if selection == cancel:
            print("Exited Sklearn sub-menu...")
            break

    
# Context the file is running in is __main__ 
if __name__ == "__main__":
    getInput()
