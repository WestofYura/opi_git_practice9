import os
import math

DISCOUNT_RATE = 0.10


def CalcOrderTotal(items, userType, debug=False):
    total = 0
    for item in items:
        total = total + item["price"] * item["qty"]
    if userType == "student":
        total = total - total * DISCOUNT_RATE
    elif userType == "teacher":
        total = total - total * DISCOUNT_RATE
    if debug == True:
        print("Calculated total:", total)
    return total


def unused_helper(data):
    value = data
    return value
