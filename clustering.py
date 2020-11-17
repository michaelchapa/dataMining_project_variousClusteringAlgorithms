import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

########################## calculate_kMeans ##################################
# Purpose:
#   Calculate k-means using 2-d Euclidian objective function on 2-d
# Parameters:
#   I       Numpy Array     dPoints         2-d numerical
#   I       Int             k               # of clusters desired
#   I       Tuple Array     randClust       coordinates for initial clusters   
# Returns:
#   O       DataFrame       dataOut     Each row is a cluster. 
# Notes:
#   None
def calculate_kMeans(dPoints, k, randClust):
    for xPoint, yPoint in dPoints:
        distances = []
        for xClust, yClust in randClust:
            distance = np.sqrt(pow((xClust - xPoint), 2) \
                               + pow((yClust - yPoint), 2))
            distances.append((round(distance, 3), (xClust, yClust)))
        
        print("(", xPoint, ",", yPoint, ")", ":", distances, "\n")
        
def main():
    data = [[2, 10], [2, 5], [8, 4], [5, 8], [7, 5], [6, 4], [1, 2], [4, 9]]
    initClusterPoints = [(2, 5), (5, 8), (1, 2)]
    calculate_kMeans(data, 3, initClusterPoints)

# Context the file is running in is __main__ 
if __name__ == "__main__":
    main()