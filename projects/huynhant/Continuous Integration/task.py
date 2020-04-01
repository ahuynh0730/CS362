import math


def firstrun():
    return "success"


def circlearea(radius):
    return math.pi * math.pow(radius, 2)


def ends_of_list(list):
    return list[0], list[len(list) - 1]


def date_difference(date1, date2):
    delta = abs(date2 - date1)
    return delta.days
