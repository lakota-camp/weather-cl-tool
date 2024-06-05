import pytz
from datetime import datetime

def k_to_f(k):
    """Converts kelvin to fahrenheit

    Args:
        k (float): Kelvin
    """
    return (k - 273.15) * 1.8 + 32

def timestamp_convert(timestamp, timezone):
    """Converts UTC timestamp to local timezone

    Args:
        timestamp (float): UTC timestamp
        timezone (String): Time zone e.g. 'America/Los_Angeles'

    Returns:
        _type_: _description_
    """
    utc_time = datetime.utcfromtimestamp(timestamp)
    
    local_timezone = pytz.timezone(timezone)
    local_time = utc_time.replace(tzinfo=pytz.utc).astimezone(local_timezone)
    
    time_local_formatted = local_time.strftime('%Y-%m-%d %I:%M:%S %p')
    
    return time_local_formatted