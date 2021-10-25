from sklearn import datasets
from sklearn.model_selection import train_test_split
import Regression as reg

dataset = datasets.fetch_california_housing()
X_train, X_test, y_train, y_test = train_test_split(dataset['data'], 
                                                    dataset['target'], 
                                                    test_size=0.2, 
                                                    random_state=42)

alpha = 0.1
ridge_rg = reg.RidgeRegression()
ridge_rg.set_params(alpha = alpha)
linear_rg = reg.LinearRegression()
models = [linear_rg, ridge_rg]
keys_list = ["linear_rg","ridge_rg"]
scores = dict.fromkeys(keys_list) # Dictionary for r2 scores
r2score = 0 # dummy variable

for i,model in enumerate(models):
    model.fit(X_train, y_train);
    scores[keys_list[i]] = model.score(X_test, y_test)
    print(f"For {keys_list[i]}, the testing R-squared is: {model.score(X_test, y_test)}.\n")
    if model.score(X_test, y_test) > r2score: # Best model has highest R2 score
        model_best = model
        model_best_str = keys_list[i]
        r2score = model.score(X_test, y_test)

print(f"The best model obtained was: {model_best_str}.\n\
And the corresponding parameters are: \n{model_best.get_params()}")

'''
Output:
For linear_rg, the testing R-squared is: 0.5757877060334111.

For ridge_rg, the testing R-squared is: 0.578392070440312.

The best model obtained was: ridge_rg.
And the corresponding parameters are: 
{'alpha': 0.1, 'intercept': -32.26420076980557, 'coefficients': array([ 4.43015612e-01,  1.05771603e-02, -1.09702884e-01,  6.91938080e-01,
        1.06777372e-06, -3.56285421e-03, -3.69189562e-01, -3.78988653e-01])}
'''
