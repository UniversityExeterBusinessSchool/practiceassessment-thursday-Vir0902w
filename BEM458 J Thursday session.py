#######################################################################################################################################################
# 
# Name:Yuan Wang
# SID:740028611
# Exam Date:27/3/2025
# Module: BEMM458
# Github link for this assignment: https://github.com/UniversityExeterBusinessSchool/practiceassessment-thursday-Vir0902w.git 
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 

customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# Write your search code here and provide comments. 

# Initialize an empty list to store (start, end) positions

my_list = []

#For through value in key_comments dictionary
for comment in key_comments.values():
    #find the start position in Customer_feedback
    start =customer_feedback.find(comment)
    if start != -1:  #  If found,calculate end position
        end =start + len(comment)
        my_list.append((start,end))#add the (start, end) to List
print(my_list) # Print result

# OUTPUT[(38, 50), (12, 17), (114, 120), (88, 94), (142, 150), (99, 109), (18, 28), (129, 136), (51, 58), (82, 87)]
# Variables in the code: customer_feedback, key_comments, my_list, comment, start, end









##########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.


# Assume the first two digits of the ID number are 23, and the last two digits are 45.
first_two_digits = 23
last_two_digits = 45

# Function to calculate Operating Profit Margin
def operating_profit_margin(operating_profit, revenue):
    return(operating_profit /revenue) * 100

# Function to calculate Revenue per Customer
def revenue_per_customer(total_revenue, num_customers):
    return total_revenue / num_customers

# Function to calculate Customer Churn Rate
def customer_churn_rate(churned_customers, total_customers):
    return (churned_customers / total_customers) * 100

# Function to calculate Average Order Value

def average_order_value(total_revenue, num_orders):
    return total_revenue / num_orders

# Call the functions with the assumed ID number digits

rpc= revenue_per_customer(last_two_digits, first_two_digits)

aov= average_order_value(last_two_digits, first_two_digits)

# Print

print(f"Revenue per Customer: {rpc}")

print(f"Average Order Value: {aov}")

# OUTPUT (23,45)
# Revenue per Customer: 1.9565217391304348
# Average Order Value: 1.9565217391304348








##########################################################################################################################################################

# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""

# Write your code here:

#Using linear regression to analyze
import numpy as np
from sklearn.linear_model import LinearRegression

# data for price and demands
prices= np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]).reshape(-1, 1)
Demands =np.array([300, 280, 260, 240, 210, 190, 160, 140, 120, 100, 85])
#Linear regression Model
Model=LinearRegression()
Model.fit(prices, Demands)
# Predict demand for price £52.
predicted_demand=Model.predict([[52]])
#find the price that maximizes revenue
revenues =prices.flatten()* Demands
max_revenue_index= np.argmax(revenues)
optimal_price =prices[max_revenue_index][0]
#  Print results  
print("Predicted demand at £52:", predicted_demand[0])
print("optimal Price for Maximum Revenue:", optimal_price)

#OUTPUT:
#Predicted demand at £52: 158.17272727272726
#  optimal Price for Maximum Revenue: 45
# Variables: prices, demands, model, predicted_demand, revenues, optimal_price
##########################################################################################################################################################

# Question 4 - Debugging; Plotting and data visualization chart



# The code below generates random numbers and plots them in a line chart.

import random
import matplotlib.pyplot as plt
#generate 100 random numbers between 1 and student ID number
max_value =int(input("Enter your Student ID: "))
random_numbers= [random.randint(1, max_value) for i in range(100)]
#plotting the numbers in a line chart
plt.plot(random_numbers, marker='o', markerfacecolor='green', markeredgecolor='red', linestyle='--', label='Random Numbers', color='blue')
plt.title("Line Chart of 100 Random Numbers")  #add title
plt.xlabel("Index")  # Add X-axis label
plt.ylabel("Random Number")     # Add Y-axis label
plt.legend()   #add legend
plt.grid(True)  # Add grid
plt.show()
# OUTPUT: A line chart with 100 random numbers plotted.