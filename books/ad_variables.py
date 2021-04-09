from datetime import datetime, timedelta, timezone

def convert_timedelta(durations):
    list = []
    for duration in durations:
        days, seconds = duration.days, duration.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = (seconds % 60)
        time = (str(days) + 'days, ' +str(hours) + 'hrs, ' + str(minutes) + 'min, ' + str(seconds) + 'secs')
        list.append(time) 
    return list