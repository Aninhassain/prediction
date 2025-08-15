import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import pickle
import json

def train_model():
    print("Loading dataset...")
    df = pd.read_csv('Bengaluru_House_Data.csv')
    
    print("Data preprocessing...")
    # Handle missing values
    df = df.dropna()
    
    # Extract BHK from size column
    df['bhk'] = df['size'].apply(lambda x: int(str(x).split(' ')[0]))
    
    # Clean total_sqft column (handle ranges like "1000 - 1500")
    def convert_sqft_to_num(x):
        tokens = str(x).split('-')
        if len(tokens) == 2:
            return (float(tokens[0]) + float(tokens[1])) / 2
        try:
            return float(x)
        except:
            return None
    
    df['total_sqft'] = df['total_sqft'].apply(convert_sqft_to_num)
    df = df.dropna()
    
    # Remove outliers
    df = df[df['total_sqft'] / df['bhk'] >= 300]
    df = df[df['total_sqft'] / df['bhk'] <= 2000]
    
    # Prepare features
    X = df[['total_sqft', 'bath', 'bhk']]
    
    # Encode location
    le = LabelEncoder()
    df['location_encoded'] = le.fit_transform(df['location'])
    X['location'] = df['location_encoded']
    
    y = df['price']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    print("Training model...")
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Evaluate model
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)
    print(f"Train R² Score: {train_score:.4f}")
    print(f"Test R² Score: {test_score:.4f}")
    
    # Save model and artifacts
    print("Saving model and artifacts...")
    
    # Save model
    with open('artifacts/banglore_home_prices_model.pickle', 'wb') as f:
        pickle.dump(model, f)
    
    # Save columns info
    locations = le.classes_.tolist()
    data_columns = ['total_sqft', 'bath', 'bhk'] + locations
    
    with open('artifacts/columns.json', 'w') as f:
        json.dump({'data_columns': data_columns}, f)
    
    print("Model training completed!")
    print(f"Number of locations: {len(locations)}")
    print("Sample locations:", locations[:5])

if __name__ == "__main__":
    train_model()
