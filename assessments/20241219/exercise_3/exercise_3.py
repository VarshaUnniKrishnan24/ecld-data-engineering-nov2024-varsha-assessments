import pandas as pd

raw_data = pd.read_json('assessments\20241219\sample-dataset-3.json')

'''Function that transforms raw transaction data:
      Flatten nested JSON structures using lambda functions
      Calculate total transaction values
      Extract unique product categories using map() and set()
'''
def transform_transaction_data(df):
    # Flatten nested JSON structures
    flattened_df = pd.json_normalize(df.to_dict(orient='records'))
    items_exploded = flattened_df.explode('items').reset_index(drop=True)
    items_normalized = pd.json_normalize(items_exploded['items'])
    items_normalized.columns = [f'items.{col}' for col in items_normalized.columns]
    final_df = pd.concat([items_exploded.drop(columns=['items']), items_normalized], axis=1)

    # Calculate total transaction values
    final_df['total_value'] = (final_df['items.price'] * final_df['items.quantity']) - final_df['items.discount']

    # Extract unique product categories
    unique_product_categories = set(map(lambda x: x, final_df['items.category']))

    return final_df, unique_product_categories

'''Analysis function that:
      Group transactions by region and calculate regional sales
      Find top-selling products using sorted() 
      Calculate average transaction value by payment method
'''
def analyze_transaction_data(df):
    # Group transactions by region and calculate regional sales
    sales_by_region = df.groupby('customer.region')['total_value'].sum()

    # Find top-selling products
    top_selling_products = sorted(df.to_dict(orient='records'), key=lambda record: record['items.quantity'], reverse=True)[:5]

    # Calculate average transaction value by payment method
    avg_transaction_value = df.groupby('payment_method')['total_value'].mean()

    return sales_by_region, top_selling_products, avg_transaction_value

'''Report generation function that:
      Filters completed transactions
      Sorts data by multiple criteria using lambda
      Generates summary statistics for different time periods
'''
def generate_transaction_reports(df):
    # Filter completed transactions
    completed_transactions = df[df['status'] == 'completed']

    # Sort data by timestamp and total value
    sorted_transactions = completed_transactions.sort_values(by=['timestamp', 'total_value'],ascending=[True, False], key=lambda x: x)

    # Generate summary statistics for different time periods
    sorted_transactions['date'] = sorted_transactions['timestamp'].dt.date
    daily_summary = sorted_transactions.groupby('date')['total_value'].agg(['sum', 'mean', 'count']).reset_index()
    monthly_summary = sorted_transactions.groupby(pd.Grouper(key='timestamp', freq='M'))['total_value'].agg(['sum', 'mean', 'count'])

    return daily_summary, monthly_summary

# Calling the functions
transformed_data, product_categories = transform_transaction_data(raw_data)
print(transformed_data.head())
print(f"\nUnique Product Categories:\n{product_categories}")

sales_by_region, top_selling_products, avg_transaction_value = analyze_transaction_data(transformed_data)
print(f"\nRegional Sales:\n{sales_by_region}")
print(f"\nTop Selling Products:\n{top_selling_products}")
print(f"\nAverage Transaction Value by Payment Method:\n{avg_transaction_value}")

daily_stats, monthly_stats = generate_transaction_reports(transformed_data)
print(f"\nDaily Summary Statistics:\n{daily_stats}")
print(f"\nMonthly Summary Statistics:\n{monthly_stats}")
