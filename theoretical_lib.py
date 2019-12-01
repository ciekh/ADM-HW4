import numpy as np
from clustering_lib import gen_random_centroids
from clustering_lib import Kmeans


# To calculate the total distance between the centroids and their belonging points:

def distances_cumulative_sum(k, db_normalize, centroids):
    
    distances = 0
    c = 0 # To move in parallel with the keys of the dict (they start to one, but in this case it dosen't matter)
    kmeans_result = Kmeans(k, db_normalize, centroids)
    for points_lst in kmeans_result[0].values(): # For all points belonging to a cluster (each key of the dict is a cluster)
        
        centroid = kmeans_result[1][c] # get the correct centroid
        
        for point in points_lst: # for each point
            
            dist = np.sqrt(((centroid-point)**2).sum()) # Calculate the Euclidean distance
            distances += dist # sum it to the previou ones
        
        c += 1 # Go to the next centroid
    
    return distances # It returns the total distance

# A function that returns a list made by list of [cumulative distance, starting centroids],it is useful to find cases in which the kmeans fail

def test_centroids(rep, k, db_normalize):
    
    centroid_lst = []
    
    for _ in range(rep):
        
        centroids = gen_random_centroids(db_normalize, k) # generate random centroids
        dist = distances_cumulative_sum(k, db_normalize, centroids) # Calculate the distances for this centroids
        centroid_lst.append([dist, centroids]) 
    
    return centroid_lst
        
