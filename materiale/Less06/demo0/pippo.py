import pandas as pd
from prophet import Prophet
import joblib

url ="https://frenzy86.s3.eu-west-2.amazonaws.com/timeseries/Data/airline_passengers.csv"
modelpath = "model_prophet.pkl"


df = pd.read_csv(url)
df.columns = ['ds','y']
df['ds'] = pd.to_datetime(df['ds'])

#model = Prophet()
#model.fit(df)

#joblib.dump(model,modelpath)  # Save model
new_model = joblib.load(modelpath)  # Load model
future = new_model.make_future_dataframe(50, freq='MS')

#prediction
forecast = new_model.predict(future)
print(forecast)