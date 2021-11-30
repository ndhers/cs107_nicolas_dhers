import sqlite3
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer



# Part A

db = sqlite3.connect('regression.sqlite')
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS model_params")
cursor.execute("DROP TABLE IF EXISTS model_coefs")
cursor.execute("DROP TABLE IF EXISTS model_results")

cursor.execute('''CREATE TABLE model_params (
               id INTEGER, 
               desc TEXT, 
               param_name TEXT, 
               value DECIMAL)''')

db.commit()

cursor.execute('''CREATE TABLE model_coefs (
          id INTEGER, 
          desc TEXT, 
          feature_name TEXT, 
          value DECIMAL)''')

db.commit()

cursor.execute('''CREATE TABLE model_results (
          id INTEGER, 
          desc TEXT, 
          train_score DECIMAL, 
          test_score DECIMAL)''')

db.commit()


# Part B

# Load data
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=87)
feature_names = data.feature_names

def save_to_database(model_id, model_desc, db, model, X_train, X_test, y_train, y_test):
	train_score = model.score(X_train, y_train)
	test_score = model.score(X_test, y_test)
	cursor = db.cursor()
	
	model_params = model.get_params()
	for name, val in model_params.items():
		input_ = (int(model_id), model_desc, name, val)
		cursor.execute('''INSERT INTO model_params 
				(id, desc, param_name, value)
				VALUES (?, ?, ?, ?)''', input_)

	for feat_name, val in zip(feature_names, model.coef_[0]):
		input_ = (int(model_id), model_desc, feat_name, val)
		cursor.execute('''INSERT INTO model_coefs 
				(id, desc, feature_name, value)
				VALUES (?, ?, ?, ?)''', input_)
	input_ = (int(model_id), model_desc, 'intercept', model.intercept_[0])
	cursor.execute('''INSERT INTO model_coefs 
			(id, desc, feature_name, value)
			VALUES (?, ?, ?, ?)''', input_)

	input_ = (int(model_id), model_desc, train_score, test_score)
	cursor.execute('''INSERT INTO model_results 
			(id, desc, train_score, test_score)
			VALUES (?, ?, ?, ?)''', input_)

	db.commit()	

# Fit model
baseline_model = LogisticRegression(solver='liblinear')
baseline_model.fit(X_train, y_train)
save_to_database(1, 'Baseline model', db, baseline_model, X_train, X_test, y_train, y_test)


# New reduced model
feature_cols = ['mean radius',
                'texture error',
                'worst radius',
                'worst compactness',
                'worst concavity']

X_train_reduced = X_train[feature_cols]
X_test_reduced = X_test[feature_cols]

reduced_model = LogisticRegression(solver='liblinear')
reduced_model.fit(X_train_reduced, y_train)
save_to_database(2, "Reduced model", db, reduced_model, X_train_reduced, X_test_reduced, y_train, y_test)

# L1 Model
penalized_model = LogisticRegression(solver='liblinear', penalty='l1', random_state=87, max_iter=150)
penalized_model.fit(X_train, y_train)
save_to_database(3, "L1 penalty model", db, penalized_model, X_train, X_test, y_train, y_test)    


# Part C

query = '''SELECT id, test_score FROM model_results WHERE test_score = (SELECT MAX(test_score) FROM model_results)'''
best_model = cursor.execute(query).fetchall()
print("\n")
print(f"Best model id: {best_model[0][0]}")
print(f"Best validation score: {best_model[0][1]}")
print("\n")

query = f'''SELECT feature_name, value FROM model_coefs where id == {best_model[0][0]}''' 
best_model_feat = cursor.execute(query).fetchall()
coef = []
for feature in best_model_feat:
	print(f"{feature[0]}: {feature[1]}")
	if feature[0] == 'intercept':
		intercept = feature[1]
	else:
		coef.append(feature[1])
print("\n")

test_model = LogisticRegression(solver='liblinear')
test_model.fit(X_train, y_train)

# Manually change fit parameters
test_model.coef_ = np.array([coef])
test_model.intercept_ = np.array([intercept])

test_score = test_model.score(X_test, y_test)
print(f'Reproduced best validation score: {test_score}')

db.close()
