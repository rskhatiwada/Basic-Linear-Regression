
import streamlit as st
import pickle
import numpy as np

# Load the pre-trained linear regression model
with open('linear_regression_model.pickle', 'rb') as file:
    model = pickle.load(file)

# Title and instructions
st.title("Simple Linear Regression Predictor")
st.write("Enter your feature values to get a prediction.")

# Input fields
sat_score = st.text_input('Enter your Class 12 score here:')

# Button for prediction with input validation and error handling
if st.button("Submit"):
    try:
        # Convert inputs to numeric, add error handling if input is invalid
        sat_score = float(sat_score)
        features = np.array([[sat_score]])

        # Prediction
        y_pred = model.predict(features)
        st.write(f"Predicted Output: {y_pred[0]}")

        # Optional: Visualize with a plot (requires training data for reference)
        # e.g., if x_train and y_train are available from the training data:
        # import matplotlib.pyplot as plt
        # fig, ax = plt.subplots()
        # ax.scatter(x_train, y_train, color='blue', label='Training data')
        # ax.plot(x_train, model.predict(x_train), color='red', label='Regression line')
        # ax.scatter([sat_score], y_pred, color='green', label='Prediction')
        # ax.legend()
        # st.pyplot(fig)

    except ValueError:
        st.error("Please enter a valid numerical value.")
