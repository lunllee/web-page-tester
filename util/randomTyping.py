from time import sleep
from random import uniform


def random_typing(target_object, text, min_time, max_time):
    for char in text:
        target_object.send_keys(char)
        sleep(uniform(min_time, max_time))
