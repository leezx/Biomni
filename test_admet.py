#!/usr/bin/env python3
"""
Test script for the simplified ADMET prediction function
"""

# Test the simple ADMET function
from biomni.tool.pharmacology import predict_admet_properties_simple

def test_admet_function():
    """Test the ADMET function with the compound from the user's query"""
    
    # The compound from the user's query
    smiles = "CC(C)CC1=CC=C(C=C1)C(C)C(=O)O"
    
    print("🧪 Testing ADMET Prediction Function")
    print("=" * 50)
    print(f"Compound: {smiles}")
    print("=" * 50)
    
    try:
        # Test the simple function
        result = predict_admet_properties_simple([smiles])
        print("\n✅ Function executed successfully!")
        print("\n📊 Results:")
        print(result)
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_admet_function()
