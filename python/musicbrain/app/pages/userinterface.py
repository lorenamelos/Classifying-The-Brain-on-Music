
import streamlit as st
import joblib
import numpy as np




#pipeline = build_pipeline()

# Load the trained model
pipeline = joblib.load('OnevsRest.pkl')

# Define the user interface
st.title('Music Genre Classification')
st.write('Enter vectorized data to classify its music genre:')

# Input fields for user to enter data
input_data = st.text_area("Enter vectorized data (comma-separated)", height=100)

# Button to trigger prediction
if st.button('Predict'):
    # Convert input string to numpy array
    input_array = np.fromstring(input_data, sep=',')
    input_array = input_array.reshape(1, -1)  # Reshape to match the expected shape for prediction

    # Make prediction using the model
    prediction = pipeline.predict(input_array)

    st.write('Predicted Music Genre:', prediction[0])
