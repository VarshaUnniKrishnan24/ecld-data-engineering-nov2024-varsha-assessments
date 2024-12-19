# Python Data Engineering Coding Exercises

#Exercise 3: ETL Pipeline for E-commerce Analytics


import pandas as pd


df=pd.read_json('/content/sample_data/sample-dataset-3.json')

df

# Printing first values in each column
for col in df.columns:
  print(col)
  print(df[col][0])  

# Function to Flatten nested JSON structures
def flatten_json(y):
	out = {}
	def flatten(x, name=''):
		# If the Nested key-value pair is of dict type
		if type(x) is dict:
			for a in x:
				flatten(x[a], name + a + '_')
		# If the Nested key-value pair is of list type
		elif type(x) is list:
			i = 0
			for a in x:
				flatten(a, name + str(i) + '_')
				i += 1
		else:
			out[name[:-1]] = x
	flatten(y)
	return out

# Driver code
print(flatten_json(df))

# total transactions
df['transaction_id'].count()


# Extract unique product categories using map() and set()
unique_categories = set(map(lambda x: x['category'], df['items']))
print(unique_categories)

# function that transforms raw transaction data
def transform_data(df):
  # Flatten nested JSON structures using lambda functions
  df['items'] = df['items'].apply(lambda x: flatten_json(x))

  # Calculate total transaction values
  df['total_value'] = df['items'].apply(lambda x: sum(item['quantity'] for item in x['items']))

  # Extract unique product categories using map() and set()
  df['unique_categories'] = df['items'].apply(lambda x: set(item['category'] for item in x['items']))

  return df

transform_data(df)


# Analysis function
def analysis_function(df):
   
   # Group transactions by region and calculate regional sales
   region_sales = df.groupby('customer_region')['total_value'].sum()
   print(region_sales)

   # Find top-selling products using sorted() with custom key
   top_selling_products_list = sorted(df['items'], key=lambda x: x['quantity'], reverse=True)
   print(top_selling_products_list)

   # Calculate average transaction value by payment method
   avg_transaction_value = df.groupby('payment_method')['total_value'].mean()
   print(avg_transaction_value)

analysis_function(df)


# Report generation function
def report_generation(df):

  # Filters completed transactions using filter()
  completed_transactions = list(filter(lambda x: x['status'] == 'completed', df))
  print(completed_transactions)

  # Filters completed transactions using filter()
  completed_transactions = list(filter(lambda x: x['status'] == 'completed', df))
  print(completed_transactions)

  report_generation(df)