import numpy as np
import pandas as pd

# Generate a larger dataset
np.random.seed(42)  # For reproducibility

# Parameters for dataset
regions = ['North', 'South', 'East', 'West']
products = ['A', 'B', 'C', 'D', 'E']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
num_records = 1000

# Create the dataset
data = {
    'Region': np.random.choice(regions, num_records),
    'Product': np.random.choice(products, num_records),
    'Month': np.random.choice(months, num_records),
    'Sales_Amount': np.random.randint(1000, 5000, num_records)
}

# Convert to DataFrame
large_df = pd.DataFrame(data)

# Save the larger dataset to a CSV file
large_csv_file_path = 'C:/Users/KIIT/Downloads/pivot/sales.csv'
large_df.to_csv(large_csv_file_path, index=False)

print(f"CSV file saved as {large_csv_file_path}")

