import random


def create_delay(start, end, decimal_point):
    delay = round(random.uniform(start, end), decimal_point)
    return delay
