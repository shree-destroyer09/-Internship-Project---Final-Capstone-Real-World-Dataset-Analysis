"""
Data Loading Module
Load and validate real-world datasets
"""

import pandas as pd
import numpy as np
import os
from pathlib import Path

class DataLoader:
    def __init__(self, data_path='data/'):
        self.data_path = Path(data_path)
        self.data_path.mkdir(exist_ok=True)
    
    def load_csv(self, filename):
        """Load CSV file"""
        filepath = self.data_path / filename
        try:
            data = pd.read_csv(filepath)
            print(f"✓ Loaded {filename}: {data.shape[0]} rows, {data.shape[1]} columns")
            return data
        except FileNotFoundError:
            print(f"✗ File not found: {filepath}")
            return None
    
    def validate_data(self, df):
        """Validate dataset structure"""
        print(f"\n📊 Dataset Info:")
        print(f"  • Shape: {df.shape}")
        print(f"  • Missing values:\n{df.isnull().sum()}")
        print(f"  • Data types:\n{df.dtypes}")
        return df
    
    def get_summary(self, df):
        """Get statistical summary"""
        return df.describe()
