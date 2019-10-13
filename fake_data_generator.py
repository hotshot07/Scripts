# script to generate timestamped (fake) data from IoT device sensors
from datetime import date, time, datetime, timedelta
import random
from contextlib import contextmanager


@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()


# starting date
# YYYY MM DD
d = date(2019, 1, 1)

# starting time
# HH MM SS
t = time(00, 00, 00)

# interval of activity of the sensor
delta = timedelta(hours=6)

# 4 observations a day so its approx a month
size_of_data = 120

# starting datetime
x = datetime.combine(d, t)

i = 0

# Adjust the range in string_format variable
# Temperature range from -1 to 15
# AQI range from 20 to 50
# Humidity range from 0 to 100
# UV Index 0.0 to 8.0,use round(random.uniform(0.0, 6.0), 2))
file = 'enter_file_name.txt'

with managed_file(file) as f:
    while i < size_of_data:
        string_format = str(x.isoformat(timespec='minutes') + ' ' + str(random.randint(-1, 15)))
        f.write(string_format)
        f.write('\n')
        # adding 6 hours
        x = x + delta
        i = i + 1
