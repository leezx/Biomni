#!/usr/bin/env python3
"""
Very simple test to verify the ADMET function works
"""

print("🧪 Simple ADMET Function Test")
print("=" * 40)

try:
    # Import the function
    print("1. Importing function...")
    from biomni.tool.pharmacology import predict_admet_properties_simple
    print("✅ Import successful!")
    
    # Test with a simple SMILES
    print("\n2. Testing function...")
    smiles = "CC(C)CC1=CC=C(C=C1)C(C)C(=O)O"
    print(f"   SMILES: {smiles}")
    
    result = predict_admet_properties_simple([smiles])
    print("✅ Function executed successfully!")
    
    print("\n3. Results:")
    print("-" * 40)
    print(result)
    print("-" * 40)
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

print("\n🎯 Test complete!")
