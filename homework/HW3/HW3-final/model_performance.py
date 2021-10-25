from sklearn import datasets
from sklearn.model_selection import train_test_split
import Regression as reg
import numpy as np
from matplotlib import pyplot as plt


dataset = datasets.fetch_california_housing()
X_train, X_test, y_train, y_test = train_test_split(dataset['data'], 
                                                    dataset['target'], 
                                                    test_size=0.2, 
                                                    random_state=42)

# Ridge regression
alpha_count = 50
alpha = [i for i in np.logspace(-2,1,num = alpha_count)]
ridge_rg = reg.RidgeRegression()
scores_ridge = []

for i in alpha:
    ridge_rg.set_params(alpha=i)
    ridge_rg.fit(X_train, y_train)
    scores_ridge.append(ridge_rg.score(X_test, y_test))


# Linear Regression
linear_rg = reg.LinearRegression()
linear_rg.fit(X_train, y_train)
scores_lreg = linear_rg.score(X_test, y_test)
scores_lreg = alpha_count * [scores_lreg]


# Plotting
fig,ax = plt.subplots()
ax.plot(alpha, scores_lreg, label = 'Linear Regression')
ax.plot(alpha, scores_ridge, label = 'Ridge Regression')
ax.set_title('$R^2$ for Linear and Ridge Regression for different values of $\\alpha$')
ax.set_xlabel('$\\alpha$')
ax.set_ylabel('$R^2$')
ax.legend(loc = 'best')
fig.savefig('P2F.png')