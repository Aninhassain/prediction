import csv
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import pickle
import json

def train_improved_model():
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
                    
                    # Better outlier removal - more realistic constraints
                    sqft_per_bhk = total_sqft / bhk
                    if sqft_per_bhk >= 200 and sqft_per_bhk <= 3000:  # More reasonable range
                        if price > 0 and price < 1000:  # Reasonable price range
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
    
    # Scale features for better model performance
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Train model
    print("Training improved model...")
    model = LinearRegression()
    model.fit(X_scaled, y)
    
    # Evaluate model
    score = model.score(X_scaled, y)
    print(f"R² Score: {score:.4f}")
    
    # Save model and artifacts
    print("Saving improved model and artifacts...")
    
    # Save model and scaler
    with open('artifacts/banglore_home_prices_model.pickle', 'wb') as f:
        pickle.dump((model, scaler), f)
    
    # Save columns info
    data_columns = ['total_sqft', 'bath', 'bhk'] + locations
    
    with open('artifacts/columns.json', 'w') as f:
        json.dump({'data_columns': data_columns}, f)
    
    print("Improved model training completed!")
    print(f"Number of locations: {len(locations)}")
    
    # Test some predictions
    print("\nTesting predictions:")
    test_cases = [
        ('Electronic City', 1000, 2, 2),
        ('Whitefield', 1500, 3, 2),
        ('1st Block HBR Layout', 800, 2, 2),  # More reasonable area
        ('1st Block HBR Layout', 163, 1, 1),  # Small studio
    ]
    
    for location, sqft, bhk, bath in test_cases:
        if location in locations:
            # Create feature vector
            features = [sqft, bath, bhk]
            location_features = [1 if location == loc else 0 for loc in locations]
            features.extend(location_features)
            
            # Scale and predict
            features_scaled = scaler.transform([features])
            prediction = model.predict(features_scaled)[0]
            print(f"{location}: {sqft} sqft, {bhk} BHK, {bath} bath -> {prediction:.2f} Lakh")

if __name__ == "__main__":
    train_improved_model()
