from sklearn.linear_model import LogisticRegression
import joblib

X = [
    [20, 100],
    [25, 150],
    [30, 200],
    [35, 250],
    [40, 300],
    [45, 350],
]

y = [0, 0, 0, 1, 1, 1]


model=LogisticRegression()
model.fit(X,y)
joblib.dump(model,"models/model.pkl")
print("Model trained and saved")
