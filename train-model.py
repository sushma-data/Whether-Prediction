import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Correct file path
data = pd.read_csv( "C:\Users\Shruthi\Downloads\weather_prediction_picnic_labels.csv")


X = data[['BASEL_picnic_weather', 'BUDAPEST_picnic_weather', 'DE_picnic_weather', 'DRESDEN_picnic_weather'],'DUSSELDORF_picnic_weather','HEATHROW_picnic_weather','KASSEL_picnic_weather','LJUBLJANA_picnic_weather','MAASTRICHT_picnic_weather','MALMO_picnic_weather','MONTELIMAR_picnic_weather','MUENCHEN_picnic_weather','PERPIGNAN_picnic_weather','SONNBLICK_picnic_weather']

y = data['rain']

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

joblib.dump(model, "model.pkl")
print("Model trained and saved successfully")
