'''K-means: Implementation of a basic Kmeans algorithm.'''

import random
import sys
import numpy as np
import pandas as pd


def err_case(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)


class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        if not isinstance(max_iter, int) or max_iter < 1:
            raise ValueError("Invalid value for max_iter")
        if not isinstance(ncentroid, int) or ncentroid < 1:
            raise ValueError("Invalid value for ncentroid")
        self.ncentroid = ncentroid  # number of centroids
        self.max_iter = max_iter  # number of max iterations to update the centroids
        self.centroids = []  # values of the centroids

    def _distance(self, vec1: np.ndarray, vec2: np.ndarray):
        return (((vec1 - vec2) ** 2).sum()) ** 0.5

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        -----
        @Args:
        X: has to be an numpy.ndarray, a matrice of dimension m * n.

        @Return:
        None.
        -------
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(X, np.ndarray):
            return None

        # select random centroids to start
        dataset_size = X.shape[0] - 1
        already_picked = []
        for _ in range(0, self.ncentroid):
            pick = random.randint(0, dataset_size)
            while pick in already_picked:
                pick = random.randint(0, dataset_size)
            self.centroids.append(X[pick])
            already_picked.append(pick)

        self.clusters = dict()
        for index, centroid in enumerate(self.centroids):
            self.clusters[index] = []

        # run the kmeans algorithm

        for _ in range(0, self.max_iter):
            # distribute the entities in the clusters
            for entity in X:
                distances = np.array(list((index, self._distance(
                    centroid, entity)) for index, centroid in enumerate(self.centroids)))
                distances = distances[distances[:, 1].argsort()]
                self.clusters[distances[0][0]].append(entity)
            break

            # compute the new

        for cluster in self.clusters.items():
            print(
                f'Centroid number {cluster[0]}: {X[cluster[0]]}. Associated region: ?')
            print(f'Population size: {len(cluster[1])}\n')

    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        -------
        This function should not raise any Exception.
        """
        pass


if __name__ == "__main__":
    arguments = list(sys.argv)
    arguments.pop(0)

    if len(arguments) != 3:
        sys.exit(
            "usage: python3 Kmeans.py <filepath='XX'> <max_iter='N'> <ncentroid='M'>")

    # parse the arguments

    filepath = arguments[0].split('=')
    if len(filepath) != 2 or filepath[0] != 'filepath':
        err_case("Wrong format for argument 'filepath'")
    filepath = filepath[1]

    ncentroid = arguments[1].split('=')
    if len(ncentroid) != 2 or ncentroid[0] != 'ncentroid':
        err_case("Wrong format for argument 'ncentroid'")
    try:
        ncentroid = int(ncentroid[1])
        if ncentroid < 1:
            raise Exception
    except:
        err_case("Wrong format for argument 'ncentroid'")

    max_iter = arguments[2].split('=')
    if len(max_iter) != 2 or max_iter[0] != 'max_iter':
        err_case("Wrong format for argument 'max_iter'")
    try:
        max_iter = int(max_iter[1])
        if max_iter < 1:
            raise Exception
    except:
        err_case("Wrong format for argument 'max_iter'")

    # read the dataset

    try:
        dataset = pd.read_csv('solar_system_census.csv', sep=',')
    except:
        err_case("Error while opening dataset file (filepath)")
    dataset = np.array(dataset.values)
    dataset = np.delete(dataset, [0], axis=1)

    # fit the dataset

    kc = KmeansClustering(max_iter=20, ncentroid=4)
    kc.fit(dataset)
