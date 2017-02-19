from fastdtw import fastdtw
from sklearn.neighbors import KNeighborsClassifier




class knndtw(object):
    
    def __init__(self, n_neighbors=5, n_weights = 'uniform'):
        self.n_neighbors = n_neighbors
        self.n_weights = n_weights
        self.knn = KNeighborsClassifier(self.n_neighbors, metric = self.dtw, weights = self.n_weights, n_jobs = -1)
    
    def fit(self, X, y):
        self.X = X
        self.y = y
        self.knn.fit(X, y)
    
    def dtw(self, t1, t2):
        return fastdtw(t1,t2)[0]
    
    def predict(self, X):
        return self.knn.predict(X) 
        
