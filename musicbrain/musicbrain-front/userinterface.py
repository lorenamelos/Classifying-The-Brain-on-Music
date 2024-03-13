
import streamlit as st
from joblib import load
import pandas as pd
import numpy as np



# Load the trained model
pipeline = load('OnevsRest.joblib')

# Define the user interface
st.title('Music Genre Classification')
st.write('Upload a CSV file containing vectorized data to classify its music genre:')

# Upload CSV file
uploaded_file = st.file_uploader("Choose a CSV file...", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file as a pandas DataFrame
    df = pd.read_csv(uploaded_file)

    # Display the head of the uploaded data
    st.write('Head of Uploaded Data:')
    st.write(df.head())

    # Extract vectorized data from the DataFrame
    input_data = df.values

    # Button to trigger prediction
    if st.button('Predict'):
        # Add a progress bar
        progress_bar = st.progress(0)

        # Function to make prediction
        def make_prediction(input_data):
            prediction = pipeline.predict(input_data)
            return prediction

        # Make prediction using the model
        prediction = make_prediction(input_data)

        # Update progress bar
        progress_bar.progress(100)

        # Create a DataFrame with prediction results
        prediction_df = pd.DataFrame({
                        'prediction': prediction
        })


        # Display the prediction results DataFrame
        st.write('Prediction Results:')
        st.dataframe(prediction_df, height=200, width=300)  # Set the height and width for the prediction results DataFrame
