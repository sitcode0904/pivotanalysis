import pandas as pd
import numpy as np

np.random.seed(50)

# Parameters for larger dataset
regions = ['North', 'South', 'East', 'West', 'Central']
products = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
sales_channels = ['Online', 'Retail', 'Wholesale']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
num_records = 5000

# Create the larger dataset
data = {
    'Region': np.random.choice(regions, num_records),
    'Product': np.random.choice(products, num_records),
    'Sales_Channel': np.random.choice(sales_channels, num_records),
    'Month': np.random.choice(months, num_records),
    'Sales_Amount': np.random.randint(500, 10000, num_records),
    'Quantity_Sold': np.random.randint(1, 100, num_records),
    'Discount': np.random.randint(0, 30, num_records),  # Percentage discount
    'Profit': np.random.randint(100, 5000, num_records),
    'Customer_Satisfaction': np.random.randint(1, 5, num_records)  # Rating from 1 to 5
}

# Convert to DataFrame
large_df = pd.DataFrame(data)

# Save the larger dataset to a CSV file
large_csv_file_path = 'C:/Users/KIIT/Downloads/pivot/LargeSales.csv'
large_df.to_csv(large_csv_file_path, index=False)

print(f"CSV file saved as {large_csv_file_path}")
