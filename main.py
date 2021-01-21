from sklearn.tree import DecisionTreeClassifier

import pandas as pd
import Features

data = pd.read_csv('Dataset.csv',delimiter=',',header=0)
X = data.iloc[:,:-1].values
Y = data.iloc[:,-1].values
clf = DecisionTreeClassifier()
clf = clf.fit(X,Y)
#input url
url = input("Enter the URL:")

#checking and predicting
checkprediction = Features.main(url)
prediction = clf.predict(checkprediction)
if (prediction == [1]):
    print("Phishing")
else:
    print("Legitimate")
