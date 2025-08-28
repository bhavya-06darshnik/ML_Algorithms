import numpy as np
from collections import Counter



def euclidean_distance(x1, x2):
    dis=np.sqrt(np.sum(np.square(x1-x2)))
    return dis


class KNN:
    def __init__(self,k):
        self.k=k

    def fit(self, X, y):
        self.X_train=X
        self.y_train=y

    def predict(self, X):
        prediction=[self._helper(x) for x in X]
        return prediction


    def _helper(self,x):
        distance=[euclidean_distance(x,x_train) for x_train in self.X_train]

        k_indices=np.argsort(distance)[:self.k]
        k_nearest=[self.y_train[i] for i in k_indices]


        most_common=Counter(k_nearest).most_common()

        return most_common[0][0]
