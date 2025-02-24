import pandas as pd
from rdkit import Chem
from mordred import Calculator, descriptors
import sys

# Example SMILES list
smiles_list = ["CCO", "C1=CC=CC=C1", "CC(=O)O"]  # Ethanol, Benzene, Acetic Acid

# Convert SMILES to RDKit molecules
molecules = [Chem.MolFromSmiles(smiles) for smiles in smiles_list]

# Initialize Mordred calculator
calc = Calculator(descriptors, ignore_3D=True)  # Ignore 3D descriptors if using 2D molecules

# Compute descriptors and store as Pandas DataFrame
desc_df = calc.pandas(molecules)

print(desc_df)

# Print the results to stdout
# print(desc_df.to_csv(index=False))

