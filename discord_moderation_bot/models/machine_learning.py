# machine_learning.py

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class ContentFilteringModel:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.model = RandomForestClassifier()

    def preprocess_data(self, data):
        # Preprocess the text data for training
        processed_data = self.vectorizer.fit_transform(data)
        return processed_data

    def train_model(self, X, y):
        # Train the machine learning model
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        return acc

    def predict(self, new_data):
        # Predict the class of new data
        processed_data = self.vectorizer.transform(new_data)
        predictions = self.model.predict(processed_data)
        return predictions

# Instantiate the ContentFilteringModel
model = ContentFilteringModel()