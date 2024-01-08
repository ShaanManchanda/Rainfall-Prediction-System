# Rainfall Prediction System

## Overview
This Rainfall Prediction System is designed to enhance and improve upon previous rainfall prediction systems. Leveraging machine learning techniques, it provides accurate predictions of rainfall in various locations across Australia. The model is built on a dataset spanning a decade, offering a comprehensive understanding of weather patterns and facilitating more reliable predictions.

## Dataset
The dataset, named 'weatherAUS.csv,' provides a comprehensive set of features including temperature, humidity, wind speed, and other meteorological parameters. This dataset is valuable for training a machine learning model to predict the likelihood of rainfall on the following day.

## Model Improvement
The key enhancements in this project include:
1. **Data Preprocessing:**
    - Handling missing data using the most frequent value for both features and the target variable.
    - Encoding categorical variables using LabelEncoder.
    - Standardizing features through StandardScaler to ensure consistent scale and better model performance.
2. **Model Selection:**
    - Utilizing a RandomForestClassifier for training the model due to its ability to handle complex relationships in data and provide robust predictions.
3. **Evaluation:**
    - Calculating the accuracy of the model on the test set using the accuracy_score function from scikit-learn.

## Model Accuracy
The trained model achieved an accuracy of approximately 85.22% on the test set, showcasing its effectiveness in predicting rainfall.

## How to Run the Model
To run the model, follow these steps:
1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd <Rainfall-Prediction-System>
2. **Install Dependencies:**
Ensure that you have the required Python libraries installed. You can use the following command:
   ```bash
   pip install numpy pandas scikit-learn
3. **Run the Jupyter Notebook:**
Open the Jupyter Notebook in your preferred environment and run each cell sequentially. Ensure that the 'weatherAUS.csv' dataset is in the same directory as the notebook.
4. **Interpret Results:**
After running the notebook, you will see the model's accuracy on the test set and a DataFrame containing the actual and predicted rainfall labels.

## Conclusion
This project enhances rainfall prediction by leveraging machine learning techniques and a comprehensive dataset. The RandomForestClassifier demonstrates its capability in capturing complex patterns within the data, resulting in improved accuracy compared to previous rainfall prediction systems.
