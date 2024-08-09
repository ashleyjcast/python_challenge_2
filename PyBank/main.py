# Create Path
import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

# Define Variables
total_months = 0
total_profit_loss = 0
profit_loss = []
profit_change = []
date = []
dates = []

# Read CSV File
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader) 

# Process each row
# The Total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
    for row in csvreader:
        total_months += 1
        total_profit_loss += int(row[1])
        profit_loss.append(int(row[1]))
        date.append(row [0])

# The changes in "Profit/Losses" over the entire period and then the average of those changes
for i , profit in enumerate(profit_loss):
    if i < total_months - 1:
        change = profit_loss [i + 1] - profit
        profit_change.append(change)
        dates.append(date [i + 1])

# Calculate average change
average_change = round(sum(profit_change) / (total_months -1), 2)

# The greatest increase in profits (date and amount) over the entire period
greatest_increase = max(profit_change)
greatest_increase_date = dates[profit_change.index(greatest_increase)]

# The greatest decrease in profits (Date and amount) over the entire period
greatest_decrease = min(profit_change)
greatest_decrease_date = dates[profit_change.index(greatest_decrease)]

# Print Results: 
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

# Create a text file of the results to add to analysis folder
output_path = os.path.join('analysis', 'financial_analysis.txt')
with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_loss}\n")
    file.write(f"Average Change: ${average_change}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
