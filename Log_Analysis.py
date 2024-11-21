import pandas as pd

def parse_log_line(line):
    parts = line.split(',')
    if len(parts) == 4:
        timestamp, ip, status_code, endpoint = parts
        return timestamp, ip, status_code, endpoint
    else:
        return None  

def get_unique_visitors(logs):
    unique_ips = set()
    for log_entry in logs:
        if log_entry:
            unique_ips.add(log_entry[1])
    return len(unique_ips)

def get_popular_endpoints(logs, top_n=5):
    endpoint_counts = {}
    for log_entry in logs:
        if log_entry:
            endpoint = log_entry[3]
            endpoint_counts[endpoint] = endpoint_counts.get(endpoint, 0) + 1
    sorted_endpoints = sorted(endpoint_counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_endpoints[:top_n]

def get_error_rate(logs):
    error_count = 0
    total_count = 0
    for log_entry in logs:
        if log_entry:
            status_code = int(log_entry[2])
            total_count += 1
            if 400 <= status_code < 600:
                error_count += 1
    if total_count == 0:
        return 0.0
    return (error_count / total_count) * 100


def generate_report(filename):
    logs = []
    print("Parsed data:timestamp, IP address, status_code")
    with open(filename, 'r') as file:
        for line in file:
            parsed_line = parse_log_line(line.strip())
            if parsed_line:
                logs.append(parsed_line)
                print(parsed_line)
        
        unique_visitors = get_unique_visitors(logs)
        popular_endpoints = get_popular_endpoints(logs)
        error_rate = get_error_rate(logs)
        
        print("\n\n Log File Report:")
        print(f"\n\n Unique Visitors: {unique_visitors}")
        print("\n\n Popular Endpoints:")
        for endpoint, count in popular_endpoints:
            print(f"- {endpoint}: {count}")
        print(f"\n\n Error Rate: {error_rate:.2f}%")

generate_report("sample-log.txt")