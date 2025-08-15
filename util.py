import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None


def get_estimated_price(location,sqft,bhk,bath):
    # Input validation
    if sqft <= 0 or bhk <= 0 or bath <= 0:
        return 0.0
    
    # Calculate area per BHK
    area_per_bhk = sqft / bhk
    
    # Check if the combination is realistic
    if area_per_bhk < 150:  # Very cramped
        return 0.0
    
    try:
        loc_index = __data_columns.index(location)
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    # Get base prediction
    base_prediction = __model.predict([x])[0]
    
    # Apply intelligent pricing logic for different BHK configurations
    # The model has a negative BHK coefficient, so we need to fix this
    if area_per_bhk < 400:  # Apply correction for most cases
        # For same area, more BHK should cost more (real estate logic)
        if bhk == 2:
            adjusted_prediction = base_prediction
        else:
            # For other BHK configurations, calculate based on 2 BHK price
            # More BHK should cost more, but with realistic constraints
            bhk_factor = 1 + (bhk - 2) * 0.25  # Each additional BHK adds 25% value
            adjusted_prediction = base_prediction * bhk_factor
    else:
        # For very spacious areas, use the model prediction as is
        adjusted_prediction = base_prediction
    
    # Ensure prediction is not negative
    adjusted_prediction = max(0, adjusted_prediction)
    
    return round(adjusted_prediction, 2)



def get_location_names():
    return __locations

def load_saved_artifacts():
    print("Loading Saved Artifacts....Start")
    global __data_columns
    global __locations

    with open("./artifacts/columns.json","r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    global __model
    with open("./artifacts/banglore_home_prices_model.pickle",'rb') as f:
        __model = pickle.load(f)
    print("Loading Artifacts done")

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))  # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location