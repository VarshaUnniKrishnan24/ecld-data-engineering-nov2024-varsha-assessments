import math

def end_corona(recovers, new_cases, active_cases):
    # daily_net_decrease = recovers - new_cases
    # days_needed = math.ceil(active_cases / daily_net_decrease)
    # return days_needed
    return math.ceil(active_cases/(recovers-new_cases))

# Test examples
print(end_corona(4000, 2000, 77000))  # 39
print(end_corona(3000, 2000, 50699))  # 51
print(end_corona(30000, 25000, 390205))  # 79
