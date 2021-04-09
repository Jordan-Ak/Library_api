from datetime import datetime, timedelta, timezone

def convert_timedelta(duration):
    days, seconds = duration.days, duration.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    time = (str(days) + 'days, ' +str(hours) + 'hrs, ' + str(minutes) + 'min')
    return time

days_to_return = 14
rating_number_max = 5