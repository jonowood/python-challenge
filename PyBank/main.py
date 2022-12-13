# import OS and CSV module
import os
import csv

# set path for budget_data.csv
csvpath = os.path.join('Resources', 'budget_data.csv')

# open CSV file
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    print(csv_reader)

# read and store the csv header
    csv_header = next(csvfile)

# Set lists to store results

# * The total number of months included in the dataset
    months = []
# * The net total amount of "Profit/Losses" over the entire period
    profits = []

# Loop to add data to lists

    for x in csv_reader:
        months.append(x[0])
        profits.append(int(x[1]))

# Find total months, and sum of profits/loss'
        month_total = len(months)
        total_profits = sum(profits)



print(month_total)
print(total_profits)

# * The changes in "Profit/Losses" over the entire period, and then the average of those changes
changes = []

for i in range(1, len(profits)):
    changes.append(profits[i] - profits[i-1])
    
average_changes = sum(changes) / (month_total-1)
rounded_average = round(average_changes, 2)

print(rounded_average)

# * The greatest increase in profits (date and amount) over the entire period
greatest_increase = max(changes)


# * The greatest decrease in profits (date and amount) over the entire period
greatest_decrease = min(changes)

print(greatest_decrease)
print(greatest_increase)

# Your analysis should look similar to the following:

#   ```text
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_total}")
print(f"Total: ${total_profits}")
print(f"Average Change: ${rounded_average}")
#   Greatest Increase in Profits: Aug-16 ($1862002)
#   Greatest Decrease in Profits: Feb-14 ($-1825558)
#   ```

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.