#module for reading csv files

import os
import csv

#set path for Files
csvpath = os.path.join("resources", "budget_data.csv")

#Declare Variables
total_months = []
total_profits = []
profit_changes = 0
monthly_changes = []
previous_value = 0

# open CSV File
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimter = ",")

    #skip the header otherwise it will count as another month
    csv_reader = next(csvreader)

    for row in csvreader:

# Total of months & profits/losses
        total_months.append(row[0])
        total_profits.append(row[1])
        print(len(total_months))

# The net total amount of "Profit/Losses" over the entire period

    total_profits=[int(x) for x in total_profits] 
    total_profits_sum=sum(total_profits) 
    print (total_profits_sum) 



#Changes in "Profit/Losses" over the entire period
#Take the diffference between two months and append to monthly profit change


    for i in range(len(total_profits)-1):
        monthly_changes.append(total_profits[i+1]-total_profits[i])

 