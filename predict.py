import joblib

model = joblib.load("model.pkl")

sample = [[30, 65, 12, 1013]]
prediction = model.predict(sample)

print("Prediction:", prediction)
