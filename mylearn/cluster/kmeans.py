import numpy as np
import random

class KMeans:
    def __init__(self,n_clusters=2, max_iter = 100):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.centroids = None

    def fit_predict(self,X):

        # select random indexes as the numberr of cluster for centroids
        random_index = random.sample(range(0,X.shape[0]),self.n_clusters)
        self.centroids = X[random_index]

        for i in range(self.max_iter):
            # assign clusters
            cluster_group = self.assign_clusters(X)
            old_centroids = self.centroids
            # move centroids

            self.centroids = self.move_centroids(X,cluster_group)
            
            #check finish
            if (old_centroids == self.centroids).all():
                break

        return cluster_group
    
    def assign_clusters(self,X):

        ''' Example : 
        X = [[1,2,3],[2,3,4],[5,6,7]]
        - in loop row => [1,2,3]
        - By Eucledian distance formula[ root((x2-x1)^2 + (y2-y1)^2)] (here using vector operation) 
        - - We calculate distance between the point and all the centroids
        - - The min. distance o the centroid is the corresponding cluster

        '''
        cluster_group = []
        distances = []
        for row in X : 
            for centroid in self.centroids:
                distances.append(np.sqrt(np.dot(row-centroid,row-centroid)))
            min_distance = min(distances)
            min_index = distances.index(min_distance)
            cluster_group.append(min_index)
            distances.clear()

        return np.array(cluster_group)
    
    def move_centroids(self,X,cluster_group):

        '''
        To calculate the new centroids we find the mean of the points that are corresponding
        to the centroids
        New centroid C1:
        For points assigned to C1: If the points are (1, 2), (2, 3), and (3, 2),
        the new centroid C1 will be calculated as:
        C1 = ((1 + 2 + 3) / 3, (2 + 3 + 2) / 3) = (2, 2.33)


        '''

        new_centroids = []
        cluster_type = np.unique(cluster_group)

        for type in cluster_type:
            new_centroids.append(X[cluster_group == type].mean(axis=0))

        return np.array(new_centroids)




