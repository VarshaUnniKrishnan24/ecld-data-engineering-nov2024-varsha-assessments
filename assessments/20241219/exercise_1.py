# Python Data Engineering Coding Exercises

# Exercise 1: Log File Analysis System


# import libraries
import pandas as pd


# Load the data
input_df = pd.read_json('/content/sample-dataset-1.json')

# input_df

# input_df.columns

# input_df['metrics']

# high-priority warnings using filter() and lambda
def high_priority_warnings(input_df):
  result = list(filter(lambda x: x['priority'] == 'high', input_df))
  return result
high_priority_warnings(input_df)


input_df[input_df['priority']=='high']

# Servers with CPU usage above 80% using list comprehension
def cpu_usage(input_df):
  result = [x for x in input_df if input_df['matrix']['cpu_usage'] > 80]
  return result
cpu_usage(input_df)

# Function that extracts unique server IDs using map() and set()
def unique_server_id(input_df):
  result = set(map(lambda x: x['server_id'], input_df))
  return result
unique_server_id(input_df)


# Timestamp and priority based sorting
input_df['timestamp']=pd.to_datetime(input_df['timestamp'])
def timestamp(input_df):
  result=sorted(input_df, key=lambda x: (x['timestamp'], x['priority']))
  return result
timestamp(input_df)

input_df.sort_values(by=["timestamp","priority"])



# Function that generates a summary report
def summary_report(input_df):
  # Count of events by priority
  events_by_priority = input_df.groupby('priority').size() 
  # List of unique event types
  unique_event_types = input_df['event_type'].unique()
  # Average CPU usage across all servers
  average_cpu_usage = input_df['metrics']['cpu_usage'].mean()
  return events_by_priority, unique_event_types, average_cpu_usage
summary_report(input_df)


input_df.groupby('priority').size() 

input_df['event_type'].unique()