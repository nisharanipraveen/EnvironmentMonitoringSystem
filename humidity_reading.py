import time

from datetime import datetime

from .Humidity import Humidity


humidity = Humidity(0, datetime.now())
def read_humidity():
    # Add code to read humidity from the sensor and return a Humidity object
    return humidity