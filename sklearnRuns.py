from sklearn.cluster import KMeans
from sklearn.cluster import MeanShift


########################### sklearn_kMeans ###################################
# Purpose: 
#   None
# Parameters:
#   None
# Returns:
#   None
# Notes:
#   None
def sklearn_kMeans(data, k):
    print(k, data)
    

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
    print(radius, data)
    

# Context the file is running in is __main__ 
if __name__ == "__main__":
    print("Hola")