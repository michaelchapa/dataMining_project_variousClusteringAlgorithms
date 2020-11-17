import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

########################## calculate_kMeans ##################################
# Purpose:
#   Calculate k-means using 2-d Euclidian objective function on 2-D
#   coordinates.
# Parameters:
#   I       dPoints         Numpy Array     2-d numerical
#   I       k               Int             # of clusters desired
#   I       randClust       Tuple Array     coordinates for initial clusters
#   I       verbose         Boolean         Prints intermediate data to stdout
# Returns:
#   O       dataOut         DataFrame       Each row is a cluster. 
# Notes:
#   None
def calculate_kMeans(dPoints, k, randClust, verbose):
    for xPoint, yPoint in dPoints:
        distances = []
        for xClust, yClust in randClust:
            distance = np.sqrt(pow((xClust - xPoint), 2) \
                               + pow((yClust - yPoint), 2))
            distances.append((round(distance, 3), (xClust, yClust)))
        
        if(verbose):
            print("(%d, %d):" %(xPoint, yPoint))
            print("\t", distances)
            
        minDistances = getShortestDistance(distances, k)
        
        
########################## getShortestDistance ###############################
# Purpose:
#   A helper fxn for subRoutine calculate_kMeans, will determine the minimum
#   distance rom the list of distances and return the cluster.
# Parameters:
#   I   distances   Array(tuple(s))     tuple(distance, clusterCoordinates)
#   I   k           Int                 # of clusters
# Returns:
#   O   minimums    Dictionary          Key = Cluster coordinate, 
#                                       Value = list(closest coordinates)
# Notes:
#   None
def getShortestDistance(distances, k):
    minDistances = dict()
    count = 0
    coordinates = []
    
    for distance in distances:
        if count == k:
            print(coordinates)
            # do the comparison
            # add the minimum coordinate to the cluster
            # set the count to 0
            count = 0
            # reset the list
            coordinates = []

        # append to the list
        coordinates.append(distance)
        # increment the count
        count += 1
        
    return distances



def main():
    data = [[2, 10], [2, 5], [8, 4], [5, 8], [7, 5], [6, 4], [1, 2], [4, 9]]
    initClusterPoints = [(2, 5), (5, 8), (1, 2)]
    calculate_kMeans(data, 3, initClusterPoints, 0)

# Context the file is running in is __main__ 
if __name__ == "__main__":
    main()