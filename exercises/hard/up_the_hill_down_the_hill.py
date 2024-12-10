

'''Up the Hill, Down the Hill
If a person traveled up a hill for 18mins at 20mph and then 
traveled back down the same path at 60mph then their average speed 
traveled was 30mph.

Write a function that returns the average speed traveled given an 
uphill time, uphill rate and a downhill rate. Uphill time is given 
in minutes. Return the rate as an integer (mph). No rounding is 
necessary.'''


def ave_spd(up_time, up_spd, down_spd):
    
    uptime = up_time / 60
    updistance = up_spd * uptime
    downdistance = updistance
    downtime = downdistance / down_spd

    total_dist = updistance + downdistance
    total_time = uptime + downtime

    return int(total_dist / total_time)

try:
    up_time = int(input("Enter uphill time in minutes: "))
    up_spd = float(input("Enter uphill speed in mph: "))
    down_spd = float(input("Enter downhill speed in mph: "))
    if up_time <= 0 or up_spd <= 0 or down_spd <= 0:
            print( "Error: All input values must be greater than 0.")
    else:
            avg_speed = ave_spd(up_time, up_spd, down_spd)
            print(f"The average speed traveled is: {avg_speed} mph")
except ValueError:
    print("Error: Invalid input. Please enter numeric values only.")

# print(ave_spd(18, 20, 60)) # 30 
# print(ave_spd(30, 10, 30)) # 15 
# print(ave_spd(30, 8, 24)) # 12
# print(ave_spd(30, "asd", 24))  #  Invalid input
# print(ave_spd(30, 15))  # Invalid input