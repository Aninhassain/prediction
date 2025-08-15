import util

def test_pricing():
    util.load_saved_artifacts()
    
    print("Testing Improved Pricing Logic:")
    print("=" * 50)
    
    test_cases = [
        (1000, 2, 2, "2 BHK"),
        (1000, 3, 2, "3 BHK"), 
        (1000, 4, 2, "4 BHK"),
        (1000, 5, 2, "5 BHK"),
    ]
    
    for sqft, bhk, bath, desc in test_cases:
        price = util.get_estimated_price('Anekal', sqft, bhk, bath)
        area_per_bhk = sqft / bhk
        print(f"{desc}: {price:.2f} Lakh (Area per BHK: {area_per_bhk:.0f} sq ft)")
    
    print("\nExpected Behavior:")
    print("- More BHK should generally cost more")
    print("- But very cramped spaces (low area per BHK) should be discounted")

if __name__ == "__main__":
    test_pricing()
