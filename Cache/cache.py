# Implement a cache

import datetime

MAX_CACHE_SIZE = 10

def init():
    """
    Initialize the cache, out of the box it will be empty
    """
    global _cache
    _cache = {} # {key: (value, expiration_time)}

def set(key, value):
    """
    Set the value of a key in the cache. 
    Input: key, value ==> string, int
    Output: True if successful, False otherwise
    """
    global _cache
    if key not in _cache:
        if len(_cache) >= MAX_CACHE_SIZE:
            _cache.popitem()
        _cache[key] = (value, datetime.datetime.now())

def get(key):
    global _cache
    if key in _cache:
        _cache[key][1] = datetime.datetime.now()
        return _cache[key][1]
    else:
        return None

def contains(key):
    global _cache
    return key in _cache

def size():
    global _cache
    return len(_cache)
