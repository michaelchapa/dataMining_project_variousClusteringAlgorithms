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
    # TODO: calculate if k == len(randClust), throw error if no match.
    for xPoint, yPoint in dPoints:
        distances = []
        for xClust, yClust in randClust:
            distance = np.sqrt(pow((xClust - xPoint), 2) \
                               + pow((yClust - yPoint), 2))
            distances.append((round(distance, 3), (xClust, yClust)))
        
        if(verbose):
            print("(%d, %d):" %(xPoint, yPoint))
            print("\t", distances)
            
        minDistances = getShortestDistance(distances, k, 0)
        updateClusters(minDistances, (xPoint, yPoint), 1)
        
        
########################## getShortestDistance ###############################
# Purpose:
#   A helper fxn for subRoutine calculate_kMeans, will determine the minimum
#   distance rom the list of distances and return the cluster.
# Parameters:
#   I   distances   Array(tuple(s))     tuple(distance, clusterCoordinates)
#   I   k           Int                 # of clusters
#   I   verbose     Boolean             Prints intermediate data to stdout
# Returns:
#   O   minimums    Dictionary          Key = Cluster coordinate, 
#                                       Value = list(closest coordinates)
# Notes:
#   None
def getShortestDistance(distances, k, verbose):
    coordinates = dict() # keys = cluster points, values = dataPoints
    minimums = list()
    for dist, coord in distances:
        coordinates.update({coord: list()})
        
    minDist = distances[0][0]
    minCoord = distances[0][1]
    for dist, coord in distances:
        if dist < minDist:
            minDist = dist
            minCoord = coord
            minimums = list() # clears the list, new minimum found
        elif dist == minDist:
            minimums.append(coord)
    
    if(verbose):
        print("minimums:", minimums)
        print("\t", minCoord, minDist, "\n")
    
    if(len(minimums) != 0):
        return minimums
    else:
        print("************ minCoord: ", type(minCoord))
        return minCoord
    
########################### updateClusters ###################################
# Purpose: 
#   None
# Parameters:
#   None
# Returns:
#   None
# Notes:
#   None
def updateClusters(minDistances, dPoint, verbose):
    clusters = dict()
    print("###### minDistances: ", type(minDistances))
    for item in minDistances:
        print(dPoint, ":")
        print(type(item), item)
        # clusters.setdefault(clstrPoint, []).append(dist)
    print()

def main():
    data = [[2, 10], [2, 5], [8, 4], [5, 8], [7, 5], [6, 4], [1, 2], [4, 9]]
    initClusterPoints = [(2, 5), (5, 8), (1, 2)]
    calculate_kMeans(data, 3, initClusterPoints, 0)

# Context the file is running in is __main__ 
if __name__ == "__main__":
    main()