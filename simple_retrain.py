import csv
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import pickle
import json

def train_model():
    print("Loading dataset...")
    
    # Load data manually
    data = []
    with open('Bengaluru_House_Data.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['total_sqft'] and row['bath'] and row['size'] and row['price'] and row['location']:
                try:
                    # Extract BHK from size
                    bhk = int(str(row['size']).split(' ')[0])
                    
                    # Handle total_sqft ranges
                    sqft_str = str(row['total_sqft'])
                    if '-' in sqft_str:
                        parts = sqft_str.split('-')
                        total_sqft = (float(parts[0]) + float(parts[1])) / 2
                    else:
                        total_sqft = float(sqft_str)
                    
                    bath = int(row['bath'])
                    price = float(row['price'])
                    location = row['location']
                    
                    # Basic outlier removal
                    if total_sqft / bhk >= 300 and total_sqft / bhk <= 2000:
                        data.append({
                            'total_sqft': total_sqft,
                            'bath': bath,
                            'bhk': bhk,
                            'price': price,
                            'location': location
                        })
                except:
                    continue
    
    print(f"Loaded {len(data)} valid records")
    
    # Prepare features
    locations = list(set([row['location'] for row in data]))
    locations.sort()
    
    # Create feature matrix
    X = []
    y = []
    
    for row in data:
        features = [row['total_sqft'], row['bath'], row['bhk']]
        # One-hot encode location
        location_features = [1 if row['location'] == loc else 0 for loc in locations]
        features.extend(location_features)
        
        X.append(features)
        y.append(row['price'])
    
    X = np.array(X)
    y = np.array(y)
    
    # Train model
    print("Training model...")
    model = LinearRegression()
    model.fit(X, y)
    
    # Evaluate model
    score = model.score(X, y)
    print(f"R² Score: {score:.4f}")
    
    # Save model and artifacts
    print("Saving model and artifacts...")
    
    # Save model
    with open('artifacts/banglore_home_prices_model.pickle', 'wb') as f:
        pickle.dump(model, f)
    
    # Save columns info
    data_columns = ['total_sqft', 'bath', 'bhk'] + locations
    
    with open('artifacts/columns.json', 'w') as f:
        json.dump({'data_columns': data_columns}, f)
    
    print("Model training completed!")
    print(f"Number of locations: {len(locations)}")
    print("Sample locations:", locations[:5])

if __name__ == "__main__":
    train_model()
