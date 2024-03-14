
# Import necessary libraries
import json
import streamlit as st
import requests
import pandas as pd
import numpy as np
import plotly.express as px
import time



# Define the URL of your Fast API

API_URL = "http://127.0.0.1:8000/predict/csv"


# Create the Streamlit app
def main():
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

        # Button to trigger prediction
        if st.button('Predict'):
            # Add a progress bar
            progress_bar = st.progress(0)

            # Function to make prediction using the API
            def make_prediction(input_data):

                start_time = time.time()  # Record the start time

                # Send the request with JSON serializable data
                response = requests.request("POST", API_URL,files={"file" : uploaded_file.getvalue()})

                # Calculate the time taken for prediction
                end_time = time.time()
                prediction_time = end_time - start_time

                #response = requests.post(API_URL, json={'data': input_data})
                if response.status_code == 200:
                    return response.json(), prediction_time
                else:
                    return None, prediction_time

            # Make prediction using the API
            #prediction = make_prediction(uploaded_file)
            prediction, time_taken = make_prediction(uploaded_file)

            # Display the time taken for prediction
            st.write(f"Time taken for prediction: {time_taken:.2f} seconds")

            # Update progress bar
            progress_bar.progress(100)

            # Create a DataFrame with prediction results
            if prediction:
                # Extract the list of predictions
                predictions_list = prediction['music_labels']

                prediction_df = pd.DataFrame({'prediction': predictions_list}, index=range(1, len(predictions_list) + 1))

                # Add an index to the DataFrame
                prediction_df.index = range(1, len(prediction_df) + 1)

                # Display the prediction results DataFrame
                st.title('Prediction Results:')
                st.table(prediction_df)  # Set the height and width for the prediction results DataFrame

            # Function to plot bar chart with custom colors
            def plot_genre_counts(prediction_df):
                # Count the number of predictions for each genre
                genre_counts = prediction_df['prediction'].value_counts()

                # Create a DataFrame from genre counts
                df = pd.DataFrame({'Genre': genre_counts.index, 'Count': genre_counts.values})

                # Plot bar chart with Plotly
                fig = px.bar(df, x='Genre', y='Count', color='Genre', labels={'Count': 'Number of Predictions'},
                            title='Genre Distribution')

                # Display the plot
                st.plotly_chart(fig)

            # Call the function to plot the bar chart
            plot_genre_counts(prediction_df)

if __name__ == '__main__':
    main()
