import datetime

def add(moment):
    d = datetime.timedelta(seconds=1000000000)
    result = moment+d
    return result
