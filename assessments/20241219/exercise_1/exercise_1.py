# Python Data Engineering Coding Exercises

# Exercise 1: Log File Analysis System

import json

''' Load the JSON dataset
'''
log_data=json.load(open('sample-dataset-1.json','r'))

''' Function that filters log entries to find:
        All high-priority warnings using filter() and lambda
        Servers with CPU usage above 80% using list comprehension
'''       
def log_filter(log_data):
    high_priority_warnings = list(filter(lambda data:data.get('priority')=='high' and data.get('status')=='warning',log_data))
    servers_above_80_cpu_usage = [ data for data in log_data if data['metrics']['cpu_usage'] > 80 ]
    return high_priority_warnings, servers_above_80_cpu_usage

''' Function that extracts unique server IDs using map() and set()
'''
def unique_server_ids(log_data):
    unique_server_ids = set(map(lambda data:data['server_id'],log_data))
    return unique_server_ids

''' Function that sorts the log entries by:
        Timestamp (primary key)
        Priority (secondary key) Using the sorted() function with a lambda key
'''
def sort_log_entries(log_data):
    sorted_log_entries = sorted(log_data,key=lambda data: (data['timestamp'], data['priority']))
    return sorted_log_entries

''' Function that generates a summary report showing:
        Count of events by priority
        List of unique event types
        Average CPU usage across all servers
'''
def log_summary_report(log_data):

    high,medium,low = 0,0,0
    for event in log_data:
        if event['priority'] == 'high':
            high+=1
        elif event['priority'] == 'medium':
            medium+=1
        elif event['priority'] == 'low':
            low+=1
    print(f"Count of events based on Priority : \n High = {high}, Medium = {medium}, Low = {low}")

    unique_event_types= set(map(lambda data : data["event_type"],log_data))
    print(f"\n Unique event Types : {unique_event_types}")
    
    cpu_usage_list = [data['metrics']['cpu_usage'] for data in log_data]
    average = sum(cpu_usage_list)/len(cpu_usage_list)
    print(f"\n Average CPU usage across all servers : {average:.2f}")
    
''' Call the functions '''
high_priority_warnings, servers_above_80_cpu_usage = log_filter(log_data)
unique_ids = unique_server_ids(log_data)
sorted_entries = sort_log_entries(log_data)

''' Print results '''
print("High-priority warnings :")
for warning in high_priority_warnings:
    print(warning)
print("\nServers with CPU usage above 80% :")
for server in servers_above_80_cpu_usage:
    print(server)
print("\nUnique server IDs:")
for server_id in unique_ids:
    print(server_id)
print("\nSorted log entries based on timestamp and priority :")
for entry in sorted_entries:
    print(entry)
print("\nSummary Report:")
log_summary_report(log_data)