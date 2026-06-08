"""
Interactive Analysis Notebook
Quick reference and common analysis patterns
"""

import pandas as pd
import numpy as np
from data_loader import DataLoader
from data_cleaning import DataCleaner
from exploratory_analysis import ExploratoryAnalysis

# ============================================================================
# QUICK START RECIPES
# ============================================================================

"""
1. BASIC ANALYSIS
"""
def basic_analysis():
    # Load data
    loader = DataLoader('data/')
    df = loader.load_csv('your_dataset.csv')
    loader.validate_data(df)
    
    # Basic statistics
    print(df.describe())
    print(df.info())
    print(df.head())

"""
2. HANDLE MISSING VALUES
"""
def handle_missing():
    loader = DataLoader('data/')
    df = loader.load_csv('your_dataset.csv')
    
    cleaner = DataCleaner(df)
    
    # Drop rows with missing values
    df_clean = cleaner.handle_missing_values('drop').get_cleaned_data()
    
    # Or fill with mean
    cleaner = DataCleaner(df)
    df_clean = cleaner.handle_missing_values('mean').get_cleaned_data()

"""
3. CORRELATION ANALYSIS
"""
def correlation_analysis():
    loader = DataLoader('data/')
    df = loader.load_csv('your_dataset.csv')
    
    eda = ExploratoryAnalysis(df)
    eda.correlation_analysis()

"""
4. DISTRIBUTION ANALYSIS
"""
def distribution_analysis():
    loader = DataLoader('data/')
    df = loader.load_csv('your_dataset.csv')
    
    eda = ExploratoryAnalysis(df)
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    eda.analyze_distributions(numeric_cols)

"""
5. CATEGORICAL ANALYSIS
"""
def categorical_analysis():
    loader = DataLoader('data/')
    df = loader.load_csv('your_dataset.csv')
    
    eda = ExploratoryAnalysis(df)
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    eda.categorical_analysis(categorical_cols)

"""
6. OUTLIER DETECTION
"""
def outlier_detection():
    loader = DataLoader('data/')
    df = loader.load_csv('your_dataset.csv')
    
    cleaner = DataCleaner(df)
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    df_clean = cleaner.remove_outliers(numeric_cols, method='iqr').get_cleaned_data()
    
    print(f"Original shape: {df.shape}")
    print(f"After outlier removal: {df_clean.shape}")

"""
7. COMPLETE PIPELINE
"""
def full_pipeline():
    # Load
    loader = DataLoader('data/')
    df = loader.load_csv('your_dataset.csv')
    loader.validate_data(df)
    
    # Clean
    cleaner = DataCleaner(df)
    df_clean = cleaner.handle_missing_values('mean') \
                      .remove_duplicates() \
                      .encode_categorical(['col1', 'col2']) \
                      .get_cleaned_data()
    
    # Analyze
    eda = ExploratoryAnalysis(df_clean)
    eda.statistical_summary()
    eda.correlation_analysis()
    
    # Get numeric columns for analysis
    numeric_cols = df_clean.select_dtypes(include=[np.number]).columns.tolist()
    if len(numeric_cols) >= 2:
        eda.analyze_distributions(numeric_cols[:3])
    
    # Save
    df_clean.to_csv('data/cleaned_dataset.csv', index=False)
    print("✓ Pipeline complete!")

# ============================================================================
# COMMON PATTERNS
# ============================================================================

"""
GROUP BY ANALYSIS
"""
def group_analysis(df, group_col, agg_col):
    """
    Analyze by groups
    group_analysis(df, 'Department', 'Salary')
    """
    return df.groupby(group_col)[agg_col].agg(['mean', 'median', 'std', 'count'])

"""
TIME SERIES ANALYSIS
"""
def time_series_summary(df, date_col, value_col):
    """
    Analyze time series data
    """
    df[date_col] = pd.to_datetime(df[date_col])
    df_sorted = df.sort_values(date_col)
    
    print(f"Date range: {df_sorted[date_col].min()} to {df_sorted[date_col].max()}")
    print(f"Value stats:\n{df_sorted[value_col].describe()}")
    
    return df_sorted

"""
COMPARE GROUPS
"""
def compare_groups(df, group_col, value_col):
    """
    Compare values across groups
    """
    comparison = df.groupby(group_col)[value_col].describe()
    return comparison

"""
PERCENTILE ANALYSIS
"""
def percentile_analysis(df, col):
    """
    Calculate percentiles for a column
    """
    percentiles = [10, 25, 50, 75, 90]
    result = {}
    for p in percentiles:
        result[f'{p}th percentile'] = np.percentile(df[col].dropna(), p)
    return result

# ============================================================================
# DATA QUALITY CHECKS
# ============================================================================

"""
CHECK DATA QUALITY
"""
def data_quality_report(df):
    """Generate data quality report"""
    
    report = {
        'Total Rows': len(df),
        'Total Columns': len(df.columns),
        'Duplicate Rows': df.duplicated().sum(),
        'Total Missing': df.isnull().sum().sum(),
        'Memory Usage': df.memory_usage(deep=True).sum() / 1024**2,  # MB
        'Numeric Columns': df.select_dtypes(include=[np.number]).shape[1],
        'Categorical Columns': df.select_dtypes(include=['object']).shape[1],
    }
    
    print("📊 DATA QUALITY REPORT")
    print("=" * 40)
    for key, value in report.items():
        if isinstance(value, float):
            print(f"{key}: {value:.2f}")
        else:
            print(f"{key}: {value}")
    
    return report

"""
IDENTIFY ANOMALIES
"""
def identify_anomalies(df, col, threshold=3):
    """
    Identify anomalies using Z-score
    threshold: standard deviations from mean
    """
    from scipy import stats
    
    z_scores = np.abs(stats.zscore(df[col].dropna()))
    anomalies = df[z_scores > threshold]
    
    print(f"Found {len(anomalies)} anomalies in {col}")
    return anomalies

# ============================================================================
# EXPORT UTILITIES
# ============================================================================

"""
SAVE ANALYSIS RESULTS
"""
def save_analysis(df, filename):
    """Save cleaned dataframe"""
    df.to_csv(f'data/{filename}', index=False)
    print(f"✓ Saved: {filename}")

def export_report(summary_stats, filename='analysis_report.txt'):
    """Export analysis report"""
    with open(f'reports/{filename}', 'w') as f:
        f.write("ANALYSIS REPORT\n")
        f.write("=" * 60 + "\n")
        f.write(str(summary_stats))
    print(f"✓ Report saved: {filename}")

# ============================================================================
# USAGE EXAMPLES
# ============================================================================

if __name__ == "__main__":
    print("📚 Analysis Notebook - Quick Reference")
    print("\nAvailable functions:")
    print("  • basic_analysis()")
    print("  • handle_missing()")
    print("  • correlation_analysis()")
    print("  • distribution_analysis()")
    print("  • categorical_analysis()")
    print("  • outlier_detection()")
    print("  • full_pipeline()")
    print("  • data_quality_report(df)")
    print("  • group_analysis(df, group_col, agg_col)")
    print("  • percentile_analysis(df, col)")
    print("\n💡 Import and use: from analysis_notebook import *")
