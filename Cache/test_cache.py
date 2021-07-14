import random
import string
import cache

def random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

cache.init()

for n in range(100):
    while True:
        key = random_string(10)
        if cache.contains(key):
            continue
        else:
            break
    value = random_string(10)
    cache.set(key, value)
    print("After {} itreations, cache contains {} entires".format(n+1, cache.contains(key)))