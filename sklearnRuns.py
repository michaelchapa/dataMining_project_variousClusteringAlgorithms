from sklearn.cluster import KMeans
from sklearn.cluster import MeanShift
import numpy as np
import pandas as pd


########################### sklearn_kMeans ###################################
# Purpose: 
#   None
# Parameters:
#   None
# Returns:
#   None
# Notes:
#   None
def sklearn_kMeans(data, k, initClusterPoints):
    kmeans = KMeans(n_clusters = k, random_state = 0).fit(data)
    print(kmeans.cluster_centers_)
    

######################### sklearn_meanShift ##################################
# Purpose: 
#   None
# Parameters:
#   None
# Returns:
#   None
# Notes:
#   None
def sklearn_meanShift(data, radius):
    clustering = MeanShift(bandwidth = radius).fit(data)
    zipped = zip(clustering.labels_, data)
    df = pd.DataFrame(zipped, columns = ["cluster", "coordinate"])
    grouped = df.groupby(["cluster"])
    
    for x, y in grouped:
        print("Cluster %d:" % (x))
        print("\t", y, "\n")
    

# Context the file is running in is __main__ 
if __name__ == "__main__":
    data = [[2, 10], [2, 5], [8, 4], [5, 8], 
            [7, 5], [6, 4], [1, 2], [4, 9]]
    initClusterPoints = [[8, 4], [5, 8], [1, 2]]
    initClusterPoints = np.array(initClusterPoints)
    # sklearn_kMeans(data, 3, initClusterPoints)
    sklearn_meanShift(data, 3)
    
    