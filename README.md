Log Analysis Tool


Create a program that analyzes server access logs to generate useful statistics.

Input Format

Each line in log.txt contains: timestamp, IP address, status_code, endpoint 

Example:

2024-03-18 10:15:23,192.168.1.1,200,/home 

2024-03-18 10:15:25,192.168.1.2,404,/profile 

2024-03-18 10:15:30,192.168.1.1,200,/about

Required Functions

1. parse_log_line(line) :

Parse each line into components

Return tuple (timestamp, ip, status_code, endpoint)

2. get_unique_visitors(logs) :

Count unique IP addresses

Return total count

3. get_popular_endpoints(logs, top_n=5) :

Find most accessed endpoints

Return list of tuples (endpoint, count)

4. get_error_rate(logs) :

Calculate percentage of 4xx/5xx status codes

Return float percentage

5. generate_report(filename) :

Combine all above functions

Print formatted summary
