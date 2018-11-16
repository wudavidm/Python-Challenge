# Operating System
import os

# import file
import csv

csvpath = os.path.join("..", "PyBank", "budgetdata.csv")

# set variables
month = []
pnl = []
total = []
totalprofit = []
priorrow = 0
change = 0
avg = 0
changelist = []


# Open the CSV
with open('budgetdata.csv') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")


    # Loop and read lines in CSV
    for row in csvreader:
        # Create list for dates
        month.append(row['Date'])
        # Create list for P&L
        pnl.append(row['Profit/Losses'])
        # Change list of string to integer
        total = (map(int, pnl))
        # Calculating change of every month and add to list
        change = pnl - priorrow
        changelist.append(change)
        # Add next row P&L value to a list
        priorrow.append(row['Profit/Losses'])
        # Calculation for avg change
        avg = float(sum(changelist))/len(changelist)


# Print results
print('Total Months:', len(month))
print('Total: $', sum(total))
print('Average Change: $', float(sum(changelist))/len(changelist))
print('Greatest Increase in Profits:', max(changelist)) # Note: not sure how to get the corresponding month
print('Greatest Decrease in Profits:', min(changelist)) # Note: not sure how to get the corresponding month