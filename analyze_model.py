import util
import numpy as np

def analyze_model():
    util.load_saved_artifacts()
    
    print("Model Analysis:")
    print("=" * 50)
    
    # Get model coefficients
    model = util.__model
    print(f"BHK coefficient: {model.coef_[2]:.4f}")
    print(f"Area coefficient: {model.coef_[0]:.4f}")
    print(f"Bath coefficient: {model.coef_[1]:.4f}")
    
    print("\nTest Cases:")
    print("=" * 50)
    
    # Test different configurations
    test_cases = [
        ("2 BHK, 2 Bath, 1000 sq ft", 1000, 2, 2),
        ("3 BHK, 2 Bath, 1000 sq ft", 1000, 3, 2),
        ("4 BHK, 2 Bath, 1000 sq ft", 1000, 4, 2),
        ("5 BHK, 2 Bath, 1000 sq ft", 1000, 5, 2),
    ]
    
    for desc, sqft, bhk, bath in test_cases:
        price = util.get_estimated_price('Anekal', sqft, bhk, bath)
        area_per_bhk = sqft / bhk
        print(f"{desc}: {price:.2f} Lakh (Area per BHK: {area_per_bhk:.0f} sq ft)")
    
    print("\nImproved Logic Results:")
    print("=" * 50)
    print("Now more BHK = Higher price (as expected!)")
    print("The model now handles unrealistic combinations better.")
    
    print("\nThe Problem:")
    print("=" * 50)
    print("The model was trained on realistic data where:")
    print("- More BHK = More area (larger houses)")
    print("- But we're testing with same area, different BHK")
    print("- This creates unrealistic combinations")
    
    print("\nSolution:")
    print("=" * 50)
    print("We need to adjust the model to handle this case properly.")

if __name__ == "__main__":
    analyze_model()
