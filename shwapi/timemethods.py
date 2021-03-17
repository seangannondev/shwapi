from datetime import datetime as dt, time as ti 
import time as t

def get_midnight():
    midnight = dt.combine(dt.today(), ti.min)
    e = midnight.timestamp()
    e = int(e)
    return e

def get_current_time():
    ts = t.time()
    ts = int(ts)
    return ts

def get_top_of_hour():
    m = get_midnight()
    e = get_current_time()

    while (m + 3600) <= e:
        m += 3600

    return m

def get_year_start():
    return (get_current_time() - (86400 * 365))