# -*- coding: utf-8 -*-
"""Student Do: E-Commerce Traffic.

This script will parse through a text file and sum the total
number of customers and the count of days in the text file to
calculate the daily average of customer traffic for an e-commerce
business.
"""

# @TODO: From the pathlib library, import the main class Path

from pathlib import Path

from numpy import number

##import conda

# @TODO: Check the current directory where the Python program is executing from

print(f"Current Working Directory is: {Path.cwd()}")

# @TODO: Set the path using Pathlib

filepath = Path("C:\Users\Notebook3\Rutgers\BootCamp\01-Lesson-Plans\01-Lesson-Plans\02-Python\3\Activities\08-Stu_File_IO\Resources\customer_traffic.txt")

# Initialize variables
customer_total = 0
day_count = 0

# @TODO: Open the file in "read" mode ('r') and store the contents in the variable 'file'
with open (filepath, "r") as file:
    # @TODO: Parse the file line by line
    for line in file:
        number = int(line)
        customer_total = 
        # @TODO: Convert the number in the text file from string to int (allows for numerical calculations)


        # @TODO: Sum the total and count of the numbers in the text file



# @TODO: Print out customer_total and day_count




# @TODO: Calculate the average

daily_ave = customer_total / day_count

# @TODO: Set output file name

output_path = "output.txt"
# @TODO: Open the output path as a file object
with open(output_path, "w") as file:
    # @TODO: Write daily_average to the output file, convert to string
