from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
data = pd.read_csv('feature_analysis_test.csv',header=0)
classifier = KNeighborsClassifier()

x = data.iloc[:, 1:]
y = data.iloc[:,:1]

le = preprocessing.LabelEncoder()
le.fit(y)
aaaa=le.transform(y)
np.asarray(aaaa)
classifier =KNeighborsClassifier()

X_train, X_test, y_train, y_test = train_test_split(x, aaaa, test_size=0.3, random_state=4)

classifier.fit(X_train, y_train)
#print(X_test)
anum=classifier.predict(X_test)
print("Accuracy score is :   ")
print(accuracy_score(y_test,anum)*100)
import pickle as pp

try_1=pp.dump(classifier,open('model.p','wb'))
try_2=pp.dump(le,open('model_1.p','wb'))

