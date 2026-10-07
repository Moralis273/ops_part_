import joblib

model=joblib.load("models/model.pkl")
    
def predict_probability(age,purchase_amount):
    features=[[age,purchase_amount]]
    probability=model.predict_proba(features)[0][1]
    return float(probability)