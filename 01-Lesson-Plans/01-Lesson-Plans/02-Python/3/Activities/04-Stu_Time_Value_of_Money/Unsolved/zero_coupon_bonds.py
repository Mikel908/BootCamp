# -*- coding: utf-8 -*-
"""
Zero-Coupon Bond Valuation.

This script will calculate the present value of zero-coupon bonds, compare the present value to the price of the bond, and determine the corresponding action (buy, not buy, neutral).
"""

# @TODO: Create a function to calculate present value

















# Intialize the zero-coupon bond parameters, assume compounding period is equal to 1
from re import X

price = 700
future_value = 1000
discount_rate = .1
compounding_periods = 1
years = 5
calculate_present_value = 0
# @TODO: Call the calculate_present_value() function and assign to a variables



# @TODO: Determine if the bond is worth it

def 

present_value = future_value * (1+ discount_rate) ** years
    if price <= present_value
        print("Buy The Bond")
    elif print("Do Not Buy")