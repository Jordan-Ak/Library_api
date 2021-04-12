#Admin variables can be customizable by anyone incase settings don't fit
from datetime import datetime, timedelta, timezone

def convert_timedelta(duration):  #Code that changes the format of the time
    days, seconds = duration.days, duration.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    time = (str(days) + 'days, ' +str(hours) + 'hrs, ' + str(minutes) + 'min')
    return time

days_to_return = 14
rating_number_max = 5

results_return_per_page = 4
pagination_max_limit = 10