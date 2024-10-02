from flask import Flask, request, render_template
import joblib
import numpy as np
import pandas as pd
from datetime import datetime

# Load the saved model
model = joblib.load('model.joblib')

# Initialize the Flask app
app = Flask(__name__)


# Define the home route
@app.route('/')
def index():
    categories = enumerate(['Beauty', 'Clothing', 'Electronics'])
    return render_template('index.html', categories=categories)


# Define the predict route to handle form submission
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get input values from the form
            demand_elasticity = float(request.form['demand_elasticity'])
            competitor_pricing = float(request.form['competitor_pricing'])
            customer_preferences = float(request.form['customer_preferences'])
            quantity = float(request.form['quantity'])
            age = float(request.form['age'])
            date = datetime.strptime(request.form['date'], '%Y-%m-%d')
            month = int(date.month)
            day_of_week = int(date.day)
            
            # Prepare the input data for prediction
            input_features = np.array([[age, customer_preferences, quantity, demand_elasticity, competitor_pricing, month, day_of_week]])
            
            # Make prediction
            predicted_price = model.predict(input_features)[0]
            
            categories = enumerate(['Beauty', 'Clothing', 'Electronics'])

            # Return the result to the user
            return render_template('index.html', categories=categories, prediction_text=f'Predicted Price per Unit: ${predicted_price:.2f}')
        except Exception as e:
            return render_template('index.html', categories=categories, prediction_text=f'Error occurred: {e}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
