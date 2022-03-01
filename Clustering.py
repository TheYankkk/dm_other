from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing

X=[[1,2],[2,1],[3,5],[5,3],[6,1]]


#question 2
kmeans = KMeans(init="k-means++",n_clusters=2,n_init=100,max_iter=10000).fit(X)
print(kmeans.labels_)
SSE=kmeans.inertia_
print(SSE)



