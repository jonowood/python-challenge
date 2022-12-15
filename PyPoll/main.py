# import OS and CSV module
import os
import csv
from collections import Counter

# set path for budget_data.csv
csvpath = os.path.join('Resources', 'election_data.csv')

# open CSV file
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
# read and store the csv header
    csv_header = next(csvfile)

# create lists to store data, loop to capture
    votes = []
    candidates = []
    unique_candidates = list(set(candidates))

    for v in csv_reader:
        votes.append(v[0])
        candidates.append(v[2])

# tally the votes for each candidate
candidate_count = Counter(candidates)

total_votes = len(votes)
print(total_votes)
print(unique_candidates)
print(candidate_count)

# sort the candidates and vote counts by winner
sorted_candidate_count = sorted(candidate_count.items(), key=lambda x:x[1], reverse=True)
sorted_candidate_dict = dict(sorted_candidate_count)

# split dictionary into keys and values
keys = []
values = []
for i in sorted_candidate_dict:
    keys.append(i)
    values.append(sorted_candidate_dict[i])

print("keys : ", str(keys))
print("values : ", str(values))


# store the candidate results into variables
winning_candidate = keys[0]
winning_votes = values[0]
second_place = keys[1]
second_votes = values[1]
third_place = keys[2]
third_votes = values[2]

winning_percent = (winning_votes / total_votes) * 100
print(f"{winning_percent:.2f}%")
second_percent = (second_votes / total_votes) * 100
print(f"{second_percent:.2f}%")
third_percent = (third_votes / total_votes) * 100
print(f"{third_percent:.2f}%")

# A complete list of candidates who received votes

# The total number of votes cast

# The percentage of votes each candidate won

# PyPoll Instructions
# In this Challenge, you are tasked with helping a small, rural U.S. town modernise its vote-counting process.
# three columns: "Voter ID", "County", and "Candidate"

print(winning_candidate)
print(winning_votes)







# The total number of votes each candidate won

# The winner of the election based on popular vote

# Your analysis should align with the following results:

# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------

# Print Output
print("Election Results")
print("----------------------------")
print(f"Total Votes {total_votes}")
print("----------------------------")
print(f'{winning_candidate} : {format(winning_percent,".3f")}% ({winning_votes})')
print(f'{second_place} : {format(second_percent,".3f")}% ({second_votes})')
print(f'{third_place} : {format(third_percent,".3f")}% ({third_votes})')
# print(f"Total: ${total_profits}")
# print(f"Average Change: ${rounded_average}")
# print(f"Greatest Increase in Profits: {month_increase} (${greatest_increase})")
# print(f"Greatest Decrease in Profits: {month_decrease} (${greatest_decrease})")

# # Set export path for output txt file
# export_path = os.path.join('Output', 'budget_data_analysis.txt')

# # Open the file using Write mode. Print output to file
# with open(export_path, 'w', encoding='utf-8') as txt:
#     txt.write("Financial Analysis")
#     txt.write('\n')
#     txt.write("----------------------------")
#     txt.write('\n')
#     txt.write(f"Total Months: {month_total}")
#     txt.write('\n')
#     txt.write(f"Total: ${total_profits}")
#     txt.write('\n')
#     txt.write(f"Average Change: ${rounded_average}")
#     txt.write('\n')
#     txt.write(f"Greatest Increase in Profits: {month_increase} (${greatest_increase})")
#     txt.write('\n')
#     txt.write(f"Greatest Decrease in Profits: {month_decrease} (${greatest_decrease})")
