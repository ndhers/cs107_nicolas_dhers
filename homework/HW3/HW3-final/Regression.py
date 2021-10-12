import numpy as np

class Regression():
    def __init__(self):
        self.params = {}

    def get_params(self):
        return self.params

    def set_params(self, **kwargs):
        for i in kwargs:
            self.params[i] = kwargs[i]

    def fit(self, X, y):
        raise NotImplementedError

    def predict(self, X):
        y_pred = np.dot(X, self.params['coefficients']) + self.params['intercept']
        return y_pred

    def score(self, X, y):
        y_pred = self.predict(X)
        return 1 - (np.sum((y-y_pred)**2))/(np.sum((y-np.mean(y))**2))


class LinearRegression(Regression):
    def fit(self, X, y):
        X = np.append(X, np.ones((X.shape[0], 1)), axis=1)
        beta = np.dot(np.linalg.pinv(np.dot(X.T, X)), np.dot(X.T, y))
        self.params['intercept'] = beta[-1]
        self.params['coefficients'] = beta[0:-1]

class RidgeRegression(LinearRegression):
    def fit(self, X, y):
        Xmean = np.mean(X, axis=0)
        scale = 1 / np.sqrt(np.sum((X - Xmean)**2, axis=0))
        Xs = X * scale
        X1 = np.append(np.ones((Xs.shape[0], 1)), Xs, axis=1)
        gamma = self.params['alpha']*np.identity(X1.shape[1])
        gamma[0,0] = 0
        beta = np.linalg.pinv(X1.T.dot(X1) + gamma.T.dot(gamma)).dot(X1.T).dot(y)
        intercept = beta[0]
        beta = beta[1:] * scale
        self.params['intercept'] = intercept
        self.params['coefficients'] = beta
        