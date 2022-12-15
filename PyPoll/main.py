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
# print(total_votes)
# print(unique_candidates)
# print(candidate_count)

# sort the candidates and vote counts by winner
sorted_candidate_count = sorted(candidate_count.items(), key=lambda x:x[1], reverse=True)
sorted_candidate_dict = dict(sorted_candidate_count)

# split dictionary into keys and values
keys = []
values = []
for i in sorted_candidate_dict:
    keys.append(i)
    values.append(sorted_candidate_dict[i])

# print("keys : ", str(keys))
# print("values : ", str(values))


# store the candidate results into variables
winning_candidate = keys[0]
winning_votes = values[0]
second_place = keys[1]
second_votes = values[1]
third_place = keys[2]
third_votes = values[2]

# calculate the percentage of votes recieved per candidate
winning_percent = (winning_votes / total_votes) * 100
second_percent = (second_votes / total_votes) * 100
third_percent = (third_votes / total_votes) * 100

# Print Output
print("Election Results")
print("----------------------------")
print(f"Total Votes {total_votes}")
print("----------------------------")
print(f'{winning_candidate} : {format(winning_percent,".3f")}% ({winning_votes})')
print(f'{second_place} : {format(second_percent,".3f")}% ({second_votes})')
print(f'{third_place} : {format(third_percent,".3f")}% ({third_votes})')
print("----------------------------")
print("Winner: ", winning_candidate)
print("----------------------------")

# Set export path for output txt file
export_path = os.path.join('Output', 'election_analysis.txt')

# # Open the file using Write mode. Print output to file
with open(export_path, 'w', encoding='utf-8') as txt:
    txt.write("Election Results")
    txt.write('\n')
    txt.write("----------------------------")
    txt.write('\n')
    txt.write(f"Total Votes {total_votes}")
    txt.write('\n')
    txt.write("----------------------------")
    txt.write('\n')
    txt.write(f'{winning_candidate} : {format(winning_percent,".3f")}% ({winning_votes})')
    txt.write('\n')
    txt.write(f'{second_place} : {format(second_percent,".3f")}% ({second_votes})')
    txt.write('\n')
    txt.write(f'{third_place} : {format(third_percent,".3f")}% ({third_votes})')
    txt.write('\n')
    txt.write("----------------------------")
    txt.write('\n')
    txt.write(f'"Winner: " {winning_candidate}')
    txt.write('\n')
    txt.write("----------------------------")