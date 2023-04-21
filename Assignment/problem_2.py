#importing libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

#reading the data
data = pd.read_csv('kepler_data.csv')

#pre-processing the data
X = data.iloc[:,:-1]
y = data.iloc[:,-1]

#encoding the target variable
le = LabelEncoder()
y = le.fit_transform(y)

#splitting the data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#building the model
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

#prediction
y_pred = clf.predict(X_test)

#accuracy
accuracy = clf.score(X_test, y_test)
print("Accuracy: ", accuracy)