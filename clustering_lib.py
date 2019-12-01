import pandas as pd
import numpy as np
from collections import defaultdict
from sklearn.decomposition import PCA

# Function to normalize the data:

def Normalize(db):
    return (db - db.mean()) / db.std()

# Scale the data for the representation:
    
def Scale(db):
    db_scaling = PCA(n_components = 2).fit_transform(db)
    return pd.DataFrame(db_scaling)
        

# Function to generate the starting centroids:
    
def gen_random_centroids(db,k):
    
    list_max = list(db.max()) # It gives the max of each column
    list_min = list(db.min()) # It gives the min of each column
    list_tot = list(zip(list_min,list_max)) # It creates a list of tuple made of min, max for each column
    
    centroids = [] # list of centroids
    
    for i in range(k): # for the numbe of centroids we have choose
        
        centroid = [] # List with all cordinates of the centroid
        for val in list_tot: # Each cordinate is generated between the min and max value of each column
            coord = np.random.uniform(low = val[0] , high = val[1]) 
            centroid.append(coord)
        centroids.append(centroid)
        
    return np.array(centroids)

# The KMeans function:
    
def Kmeans(k, db_normalize, centroids):
    
    matr_wines = db_normalize.to_numpy() # Transform the DF in a matrix
    
    while True:
        
        # Let's create a dictioanry in which we can store  the distances between points and centroids:
        
        d = defaultdict(list) # a dict with as keys the number of the centroid and as value
        
        for i in range(1,k+1): # First centroid is centroid 1 and so on (no centroid 0)
            d[i]
            
        # Let's calculate the Euclidean distance for each point with all the centroids
        # and associate the point to the nearest centroid:
        
        for a in matr_wines:
            lst2 = [] # It contains the distances between the point an d each centroid
            for b in centroids:
                dist = np.sqrt(((a-b)**2).sum()) # Euclidean distance
                lst2.append(dist)
            mn = np.argmin(lst2) + 1 # get the lowest distance index (and add 1 to know the centroid (because tehsy start to 1 and not 0)
            d[mn].append(a) # Associate to the closest centroid the point 
            
        # Save the the centroids (before replace them with the new ones):
        
        old_centroids = np.zeros((k, db_normalize.shape[1])) # Inizialitze an empty array with k rows and the same number of columns of the df
        old_centroids = old_centroids + centroids # Create the matrix with all centroids
       
        # Let's calculate the new centroids as the average of the coordinates of the points associated with it,

        
        for i in range(1,k+1):
            x = d[i] # Points belong to centroid i
            if x: # If there is any points associated with that centroid
                mean = np.mean(x,axis = 0) # Crete the centroid as the mean of each coridnate of all ponts
                centroids[i-1] = mean # Add it to the array
                
        # Let's check if centroids have changed (old vs new ones):
        
        if (np.sqrt(((centroids-old_centroids)**2).sum()) == 0):
            break
        
    return [d, centroids] # d is the dictionary in which to each centroid is associated the belonging points and centroids is the matrix with all centroids

# Cost Function:
    
def cost(kMax, db_normalize):
    
    list_all_distances = []
    for i in range(1,kMax+1): # for any natural number of centorids (starting to 1 to the the max we want)
        centroids = gen_random_centroids(db_normalize, i)
        result_Kmeans = Kmeans(i, db_normalize, centroids) # do the kmeans
        dict_points = result_Kmeans[0] # It is the dictionary with all points
        matr_centroids = result_Kmeans[1] # This is the matrix with the centroids
        
        dist_all_points_in_all_cluster = 0
        for j in range(i): # for each centroid
            points = dict_points[j+1] # get the points belonging to the centroid j
            centr = matr_centroids[j] # Get the centroid j
            
            dist_all_points_in_cluster = 0 # sum all distances of points belonging to centroid j and the centorid
            for point in points: # for each point belongs to the centroid j
                dist_point = np.sqrt(((point-centr)**2).sum()) # Calculate the distance between that point and the corresponding centroid
                dist_all_points_in_cluster += dist_point # sum this distance to the previous ones
            
            dist_all_points_in_all_cluster += dist_all_points_in_cluster # sum the distance of all points and the cluster j and the distance between points and cluster j+1
            
        list_all_distances.append(dist_all_points_in_all_cluster) # Append the sum of all distances for k cluster to the list
    
    return list_all_distances

