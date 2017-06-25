import sys
import numpy as np
from cPickle import *
from sklearn import cluster

k = 2
kmeans = cluster.KMeans(n_clusters=k)
data = load(open('trainData.p','rb'))
#_bin = [1,2,3,4,5]
#_bin = [{'1':6,'2':7,'3':8,'4':9}]
#lst = np.array([_bin,_bin,_bin])
#data = {"SNP": lst}

kmeans.fit()
# And to get the locations of the centroids and the label of the owning cluster for each observation in the data set:
labels = kmeans.labels_
print labels
centroids = kmeans.cluster_centers_
print centroids

