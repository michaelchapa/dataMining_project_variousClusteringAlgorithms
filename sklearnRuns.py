from sklearn.cluster import KMeans
from sklearn.cluster import MeanShift
from sklearn_extra.cluster import KMedoids
import numpy as np
import pandas as pd

########################### sklearn_kMeans ###################################
# Purpose: 
#   Runs a Scikit-Learn version of the k-means clustering algorithm
# Parameters:
#   I   data    2-D numpy array         data points to cluster
#   I   k       Integer                 # of cluster centers
# Returns:
#   None
# Notes:
#   None
def sklearn_kMeans(data, k):
    kmeans = KMeans(n_clusters = k, random_state = 0).fit(data)
    print(kmeans.cluster_centers_)
    

######################### sklearn_meanShift ##################################
# Purpose: 
#   Runs a Scikit-Learn version of the Mean Shift clustering algorithm
# Parameters:
#   I   data          2-D numpy array      data points to cluster
#   I   bandwidth     Integer              The radius around a cluster center
# Returns:
#   None
# Notes:
#   None
def sklearn_meanShift(data, bandwidth):
    clustering = MeanShift(bandwidth = bandwidth).fit(data)
    zipped = zip(clustering.labels_, data)
    df = pd.DataFrame(zipped, columns = ["cluster", "coordinate"])
    grouped = df.groupby(["cluster"])
    
    for x, y in grouped:
        print("Cluster %d:" % (x))
        print("\t", y, "\n")
 
    
########################## sklearn_PAM #######################################
# Purpose:
#   Uses the imported sklearn KMedoids function to cluster data with the
#   PAM algorithm.
# Parameters:
#   I       dPoints             Numpy array     2D numerical
#   I       k                   int             number of clusters
# Returns:
#   O       kmedoids.labels_    int array       cluster label for each point
# Notes:
#   n/a
def sklearn_PAM(dPoints, k):
    kmedoids = KMedoids(n_clusters=k).fit(dPoints)
    return kmedoids.labels_


# Context the file is running in is __main__ 
if __name__ == "__main__":
    data = [[2, 10], [2, 5], [8, 4], [5, 8], 
            [7, 5], [6, 4], [1, 2], [4, 9]]
    initClusterPoints = [[8, 4], [5, 8], [1, 2]]
    initClusterPoints = np.array(initClusterPoints)
    # sklearn_kMeans(data, 3, initClusterPoints)
    # sklearn_meanShift(data, 3)