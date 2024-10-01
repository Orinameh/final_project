from fastapi import FastAPI
import joblib
import pandas as pd

model = joblib.load('app/model.joblib')
data = pd.read_csv('./final_dataset.csv')


# function to predict optimal price
def predict_optimal_price(input: pd.DataFrame):
    predicted_price = model.predict(input)
    return predicted_price[0]

app = FastAPI()

# Landing page of the application
@app.get("/")
def root():
    return {'message': 'Price optimization model deployment'}

# Prediction page of the application
@app.get("/predictions")
def predictions():
    random = data[['Age', 'Product Category', 'Quantity', 'Demand Elasticity', 'Competitor Pricing', 'Month', 'Day of Week']].sample(n=1) 

    prediction = predict_optimal_price(random)

    return {"prediction": f"Optimal Price per Unit: {prediction: 2f}"}