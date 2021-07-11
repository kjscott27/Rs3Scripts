import random


def __main__(start, end, decimal_point):
    delay = round(random.uniform(start, end), decimal_point)
    return delay
