import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load your dataset
df1 = pd.read_csv("data/parkinson.csv")

# Define the features and target variable
X = df1.drop("target", axis=1)
y = df1["target"]

# Create and train the model
model = DecisionTreeClassifier()
model.fit(X, y)

# Create a function to make predictions
def predict_parkinsons(features):
    pred = model.predict([features])
    return pred[0]
