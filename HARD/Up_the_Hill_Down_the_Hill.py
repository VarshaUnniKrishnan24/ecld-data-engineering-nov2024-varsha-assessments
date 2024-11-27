# Up the Hill, Down the Hill
# If a person traveled up a hill for 18mins at 20mph and then 
# traveled back down the same path at 60mph then their average speed 
# traveled was 30mph.

# Write a function that returns the average speed traveled given an 
# uphill time, uphill rate and a downhill rate. Uphill time is given 
# in minutes. Return the rate as an integer (mph). No rounding is 
# necessary.

def ave_spd(up_time=None, up_spd=None, down_spd=None):
    
    if (
        not up_time or not up_spd or not down_spd or
        not all(isinstance(i, (int, float)) for i in [up_time, up_spd, down_spd]) or
        any(i <= 0 for i in [up_time, up_spd, down_spd])
    ):
        return "Invalid input."

    uptime = up_time / 60
    updistance = up_spd * uptime
    downdistance = updistance
    downtime = downdistance / down_spd

    total_dist = updistance + downdistance
    total_time = uptime + downtime

    return int(total_dist / total_time)

	
print(ave_spd(18, 20, 60)) # 30 
print(ave_spd(30, 10, 30)) # 15 
print(ave_spd(30, 8, 24)) # 12
print(ave_spd(30, "asd", 24))  #  Invalid input
print(ave_spd(30, 15))  # Invalid input