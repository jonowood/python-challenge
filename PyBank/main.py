# import OS and CSV module
import os
import csv

# set path for budget_data.csv
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    print(csv_reader)

# Read and store the csv header
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

        month_total = len(months)
        total_profits = sum(profits)


print(month_total)
print(total_profits)



# * The changes in "Profit/Losses" over the entire period, and then the average of those changes

# * The greatest increase in profits (date and amount) over the entire period

# * The greatest decrease in profits (date and amount) over the entire period

# Your analysis should look similar to the following:

#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $22564198
#   Average Change: $-8311.11
#   Greatest Increase in Profits: Aug-16 ($1862002)
#   Greatest Decrease in Profits: Feb-14 ($-1825558)
#   ```

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.