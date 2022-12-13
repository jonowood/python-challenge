# import OS and CSV module
import os
import csv

# set path for budget_data.csv
csvpath = os.path.join('Resources', 'budget_data.csv')

# open CSV file
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")


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


# * The changes in "Profit/Losses" over the entire period, and then the average of those changes
changes = []

for i in range(1, len(profits)):
    changes.append(profits[i] - profits[i-1])
    
average_changes = sum(changes) / (month_total-1)
rounded_average = round(average_changes, 2)

# * The greatest increase in profits (date and amount) over the entire period
greatest_increase = max(changes)
month_increase = months[changes.index(greatest_increase)+1]


# * The greatest decrease in profits (date and amount) over the entire period
greatest_decrease = min(changes)
month_decrease = months[changes.index(greatest_decrease)+1]

# Print Output
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_total}")
print(f"Total: ${total_profits}")
print(f"Average Change: ${rounded_average}")
print(f"Greatest Increase in Profits: {month_increase} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {month_decrease} (${greatest_decrease})")

# Set export path for output txt file
export_path = os.path.join('Output', 'budget_data_analysis.txt')

# Open the file using Write mode. Print output to file
with open(export_path, 'w', encoding='utf-8') as txt:
    txt.write("Financial Analysis")
    txt.write('\n')
    txt.write("----------------------------")
    txt.write('\n')
    txt.write(f"Total Months: {month_total}")
    txt.write('\n')
    txt.write(f"Total: ${total_profits}")
    txt.write('\n')
    txt.write(f"Average Change: ${rounded_average}")
    txt.write('\n')
    txt.write(f"Greatest Increase in Profits: {month_increase} (${greatest_increase})")
    txt.write('\n')
    txt.write(f"Greatest Decrease in Profits: {month_decrease} (${greatest_decrease})")


