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

# create lists to store data, loop to capture
    votes = []
    candidates = []
    candidate_count = {}
    candidate_votes = 0
    unique_candidates = list(set(candidates))

    for v in csv_reader:
        votes.append(v[0])
        # candidates.append(v[2])
        if v[2] not in candidates:
            candidates.append(v[2])
            candidate_votes = 1
        else:
            candidate_votes = candidate_votes + 1





# A complete list of candidates who received votes



# up to here ##################################  



 
# The total number of votes cast
total_votes = len(votes)


print(total_votes)
print(candidate_votes)

# The percentage of votes each candidate won


# PyPoll Instructions
# In this Challenge, you are tasked with helping a small, rural U.S. town modernise its vote-counting process.

# three columns: "Voter ID", "County", and "Candidate"







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
