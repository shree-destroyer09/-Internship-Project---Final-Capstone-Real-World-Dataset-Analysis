"""
Data Cleaning Module
Clean, transform, and preprocess data
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder

class DataCleaner:
    def __init__(self, df):
        self.df = df.copy()
        self.original_df = df.copy()
    
    def handle_missing_values(self, method='drop'):
        """
        Handle missing values
        method: 'drop', 'mean', 'median', 'forward_fill'
        """
        print("🔧 Handling missing values...")
        
        if method == 'drop':
            self.df = self.df.dropna()
        elif method == 'mean':
            numeric_cols = self.df.select_dtypes(include=[np.number]).columns
            self.df[numeric_cols] = self.df[numeric_cols].fillna(self.df[numeric_cols].mean())
        elif method == 'median':
            numeric_cols = self.df.select_dtypes(include=[np.number]).columns
            self.df[numeric_cols] = self.df[numeric_cols].fillna(self.df[numeric_cols].median())
        elif method == 'forward_fill':
            self.df = self.df.fillna(method='ffill')
        
        print(f"✓ Missing values handled. Remaining: {self.df.isnull().sum().sum()}")
        return self
    
    def remove_duplicates(self):
        """Remove duplicate rows"""
        print("🔧 Removing duplicates...")
        initial_rows = len(self.df)
        self.df = self.df.drop_duplicates()
        removed = initial_rows - len(self.df)
        print(f"✓ Removed {removed} duplicate rows")
        return self
    
    def remove_outliers(self, columns, method='iqr'):
        """
        Remove outliers
        method: 'iqr' or 'zscore'
        """
        print("🔧 Removing outliers...")
        
        if method == 'iqr':
            for col in columns:
                Q1 = self.df[col].quantile(0.25)
                Q3 = self.df[col].quantile(0.75)
                IQR = Q3 - Q1
                self.df = self.df[(self.df[col] >= Q1 - 1.5 * IQR) & 
                                   (self.df[col] <= Q3 + 1.5 * IQR)]
        
        print(f"✓ Outliers removed")
        return self
    
    def encode_categorical(self, columns):
        """Encode categorical variables"""
        print("🔧 Encoding categorical variables...")
        
        for col in columns:
            le = LabelEncoder()
            self.df[col] = le.fit_transform(self.df[col].astype(str))
        
        print(f"✓ {len(columns)} columns encoded")
        return self
    
    def normalize_features(self, columns):
        """Normalize numerical features"""
        print("🔧 Normalizing features...")
        
        scaler = StandardScaler()
        self.df[columns] = scaler.fit_transform(self.df[columns])
        
        print(f"✓ {len(columns)} columns normalized")
        return self
    
    def get_cleaned_data(self):
        """Return cleaned dataframe"""
        return self.df
