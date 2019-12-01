# ADM-HW4

- Lorenzo Ceccomancini - Omid Ghamiloo
- Dario Russo - russo.1714011@studenti.uniroma1.it
- Omid Ghamiloo - omid.ghamiloo@gmail.com


## File used

- For exercise 1 we used the files in the data folder (passwords1.txt, passwords2.txt).
- For exercise 3 we used the data in the wines.data file and the information in the wines.names file.

## Lib used:

### hashing_lib.py
choose_size_and_hash: to calculate the parameter of the Bloom Filter
hash1 to hash7: to create the hash functions
bloom_indexes: returns all the hashes in a list
CreateFilter: to create the bloom filter
CheckPass: to check if the passwords of the seconda file are in the first one

### sorting_lib.py
There are three sorting functions in the following order: the first for integers, the second for letters and the third for words.

### clustering_lib.py
There are the functions used to perform the Kmeans.
The function to normalize the data, the function to generate the centroids, the main function of the kmeans,
the cost function to see the ideal number of k and the scaling function in 2 dimensions for plotting with the PCA.

### theoretical_lib.py
We call some functions from the clustering_lib.py (Normalize, gen_random_centroids and Kmeans), the other functions are used to easily calculate some values to plot or to analyze.

distances_cumulative_sum: returns the sum of all distances between clusters and their belonging points
test_centroids: it allows to run for n times for a given k (numbe of centroids) the kmeans with always different starting centroids and return a nasted list, in which eac element contains the cost function for the correspindonig starting centroids and the centroids.

## Main.ipynb
In the main we explain the implementation choices and run our libraries showing the various plots and the results obtained, for each exercise there is its own "main".
