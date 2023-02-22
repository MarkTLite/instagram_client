import time

def create_unique_name(filename: str):
    """Returns a unique storage name for an uploaded file's name"""
    unique_prefix = str(int(time.time()*1000)) # using milliseconds_since_epoch
    return unique_prefix + '_' + filename