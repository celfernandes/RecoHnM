#This .py constructs a KMeans clustering of this dataframe into N clusters

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

def clustering_customers(number_of_clusters):
    # Configuring the parameters of the clustering algorithm
    customers = pd.read_csv('../data/customers_feature_engineered.csv')

    #remove the index, as it would bias the clustering
    customers_no_id = customers.drop('customer_id',1)

    # Define the clustering algorithm
    KMeans_cluster = KMeans(n_clusters=number_of_clusters)
    # Fitting the clustering algorithm
    KMeans_cluster.fit(customers_no_id)
    # Adding the results to a new column in the dataframe
    customers["cluster_KNN"] = KMeans_cluster.labels_

def customers_with_clusters(number_of_clusters):
    clustering_customers(number_of_clusters)
    return customers[['article_id','cluster_KNN']]
