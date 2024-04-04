# 🧠 Classifying The Brain on Music: Le Wagon AI Bootcamp Final Project

This repository contains the final project for the Le Wagon Data Science & AI Bootcamp. The project demonstrates the application of AI and machine learning techniques to solve a real-world problem related to **multi-classification** problem. 

## Project Description

### General Description
The training data (train.csv) consist of 160 event-related brain images (trials), corresponding to twenty 6-second music clips, four clips in each of the five genres, repeated in-order eight times (runs). The labels (labels.csv) correspond to the correct musical genres, listed above, for each of the 160 trials.

There are 22036 features in each brain image, corresponding to blood-oxygenation levels at each 2mm-cubed 3D location within a section of the auditory cortex. In human brain imaging, there are often many more features (brain sites) than samples (trials), thus making the task a relatively challenging multiway classification problem.

The testing data (test.csv) consists of 40 event-related brain images corresponding to novel 6-second music clips in the five genres. The test data is in randomized order with no labels. You must predict, using only the given brain images, the correct genre labels (0-4) for the 40 test trials.

For more details regarding the tasks, including the dataset download, please refer to the information provided in this [Google Colab Link](https://colab.research.google.com/drive/1tbP5miE-5DXXZ5507Rh9eMlLDCWi5L2y?usp=sharing)

### Summary about development

Under the project development we did some experimentations with **PCA, XGBoost and OneVsRest**, but at the end the **logistic regression** model was the best one for our dataset. 

## Dataset

The testing data (test.csv) consists of 40 event-related brain images corresponding to novel 6-second music clips in the five genres. The test data is in randomized order with no labels. You must predict, using only the given brain images, the correct genre labels (0-4) for the 40 test trials.

There are 22036 features in each brain image, corresponding to blood-oxygenation levels at each 2mm-cubed 3D location within a section of the auditory cortex. In human brain imaging, there are often many more features (brain sites) than samples (trials), thus making the task a relatively challenging multiway classification problem.

## Deployed app:

You can check the final deployment of our project on te link below: 

🤖  Streamlit APP:  https://lewagon-final-project-jahknaubjpaybbvxcfy3uz.streamlit.app/

## Collaborators

- Jonathan [@Jojoooo1](https://github.com/Jojoooo1)

- Lorena Melo [@lorenamelos](https://github.com/lorenamelos)



