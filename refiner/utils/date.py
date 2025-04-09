
from datetime import datetime


def parse_timestamp(timestamp):
    """Parse a timestamp to a datetime object."""
    if isinstance(timestamp, int):
        return datetime.fromtimestamp(timestamp / 1000.0)
    return datetime.fromisoformat(timestamp.replace("Z", "+00:00"))


def format_datetime_utc(dt):
    """Format a datetime object to UTC string."""
    if isinstance(dt, str):
        return dt
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
