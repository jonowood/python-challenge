# import OS and CSV module
import os
import csv

# set path for budget_data.csv
csvpath = os.path.join('Resources', 'election_data.csv')

# open CSV file
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
# read and store the csv header
    csv_header = next(csvfile)

# The total number of votes cast
    votes = []
    candidates = []

    for v in csv_reader:
        votes.append(v[0])
        candidates.append(v[2])

 # A complete list of candidates who received votes

 
total_votes = len(votes)
unique_candidates = set(candidates)

print(total_votes)
print(unique_candidates)



# PyPoll Instructions
# In this Challenge, you are tasked with helping a small, rural U.S. town modernise its vote-counting process.

# three columns: "Voter ID", "County", and "Candidate"



# A complete list of candidates who received votes

# The percentage of votes each candidate won

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
