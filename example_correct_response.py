#!/usr/bin/env python3
"""
Example of the correct response format the AI should generate
"""

# This is what the AI should generate for the ADMET prediction task:

example_response = '''
I need to predict ADMET properties for this compound. Let me analyze the SMILES string and use the appropriate tools.

<execute>
from biomni.tool.pharmacology import predict_admet_properties_simple

# The compound SMILES: CC(C)CC1=CC=C(C=C1)C(C)C(=O)O
# This appears to be a carboxylic acid derivative with a benzene ring

print("Starting ADMET prediction...")
print("Compound SMILES:", "CC(C)CC1=CC=C(C=C1)C(C)C(=O)O")

# Use the simple, reliable ADMET prediction function
result = predict_admet_properties_simple(
    smiles_list=["CC(C)CC1=CC=C(C=C1)C(C)C(=O)O"],
    ADMET_model_type="MPNN"
)

print("\nADMET Prediction Results:")
print("=" * 50)
print(result)
print("=" * 50)

print("\nAnalysis complete!")
</execute>
'''

print("✅ Example of correct AI response format:")
print(example_response)
