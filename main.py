"""
Main Entry Point - Complete Data Analytics Pipeline
Real-World Dataset Analysis Capstone Project
"""

import os
from pathlib import Path
from data_loader import DataLoader
from data_cleaning import DataCleaner
from exploratory_analysis import ExploratoryAnalysis
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

def setup_environment():
    """Setup project directories"""
    Path('data').mkdir(exist_ok=True)
    Path('plots').mkdir(exist_ok=True)
    Path('models').mkdir(exist_ok=True)
    print("✓ Project directories initialized")

def main():
    print("=" * 60)
    print("🎯 CAPSTONE PROJECT: Real-World Dataset Analysis")
    print("=" * 60)
    
    # Step 1: Setup
    setup_environment()
    
    # Step 2: Load Data
    print("\n📥 STEP 1: Loading Data...")
    loader = DataLoader('data/')
    
    # Example: Load your dataset (replace 'your_dataset.csv' with actual filename)
    # df = loader.load_csv('your_dataset.csv')
    
    # For demonstration, create sample data
    print("\n⚠️  Sample data created for demonstration")
    print("   Replace with your actual dataset in 'data/' folder\n")
    
    # Create sample dataset
    df = pd.DataFrame({
        'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70] * 10,
        'Income': [30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000] * 10,
        'Experience': [2, 5, 8, 10, 15, 18, 20, 22, 25, 28] * 10,
        'Department': ['Sales', 'IT', 'HR', 'Finance', 'Marketing'] * 20,
        'Performance': [3.5, 4.0, 3.8, 4.2, 3.9, 4.1, 3.7, 4.3, 4.0, 3.6] * 10,
    })
    
    loader.validate_data(df)
    
    # Step 3: Data Cleaning
    print("\n🧹 STEP 2: Data Cleaning & Transformation...")
    cleaner = DataCleaner(df)
    
    # Apply cleaning operations
    cleaned_df = cleaner.handle_missing_values('mean') \
                        .remove_duplicates() \
                        .encode_categorical(['Department']) \
                        .get_cleaned_data()
    
    print(f"✓ Cleaned dataset shape: {cleaned_df.shape}")
    
    # Step 4: Exploratory Analysis
    print("\n🔍 STEP 3: Exploratory Data Analysis...")
    eda = ExploratoryAnalysis(cleaned_df)
    
    # Statistical summary
    eda.statistical_summary()
    
    # Distribution analysis
    numeric_cols = ['Age', 'Income', 'Experience', 'Performance']
    eda.analyze_distributions(numeric_cols)
    
    # Correlation analysis
    eda.correlation_analysis()
    
    # Pattern analysis
    eda.identify_patterns('Experience', 'Income')
    
    # Missing data visualization
    eda.missing_data_visualization()
    
    # Step 5: Insights & Recommendations
    print("\n💡 STEP 4: Key Insights & Recommendations...")
    generate_insights(cleaned_df)
    
    # Step 6: Save Results
    print("\n💾 STEP 5: Saving Results...")
    cleaned_df.to_csv('data/cleaned_dataset.csv', index=False)
    
    # Create summary report
    with open('reports/analysis_report.txt', 'w') as f:
        f.write("=" * 60 + "\n")
        f.write("DATA ANALYSIS REPORT\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Dataset Shape: {cleaned_df.shape}\n\n")
        f.write("Statistical Summary:\n")
        f.write(str(cleaned_df.describe()))
        f.write("\n\nCorrelation Matrix:\n")
        f.write(str(cleaned_df.corr()))
    
    print("✓ Results saved to 'reports/' and 'data/' folders")
    print("\n" + "=" * 60)
    print("✅ Analysis Complete!")
    print("=" * 60)

def generate_insights(df):
    """Generate actionable insights from the data"""
    
    insights = []
    
    # Example insights
    if 'Income' in df.columns and 'Experience' in df.columns:
        correlation = df['Income'].corr(df['Experience'])
        insights.append(f"• Experience & Income correlation: {correlation:.2f}")
    
    if 'Age' in df.columns:
        avg_age = df['Age'].mean()
        insights.append(f"• Average Age: {avg_age:.1f} years")
    
    if 'Performance' in df.columns:
        avg_performance = df['Performance'].mean()
        insights.append(f"• Average Performance: {avg_performance:.2f}/5.0")
    
    print("\n📊 Key Findings:")
    for insight in insights:
        print(insight)
    
    print("\n💼 Recommendations:")
    print("• Focus on employee development programs")
    print("• Analyze performance vs. compensation")
    print("• Implement departmental benchmarking")
    print("• Create predictive models for retention")

if __name__ == "__main__":
    main()
