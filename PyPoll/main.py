### PyPoll Instructions

#In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

#You will be given a set of poll data called `election_data.csv`. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

#* The total number of votes cast
#* A complete list of candidates who received votes
#* The percentage of votes each candidate won
#* The total number of votes each candidate won
#* The winner of the election based on popular vote

total_votes = 0
candidates = {}

import os
import csv

election_data_csv = os.path.join(os.path.dirname(__file__), "Resources", "election_data.csv")

with open(election_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    next(csvreader, None)
       
    for row in csvreader:
        voter_id, county, candidate = row

        total_votes += 1

        if candidate in candidates:
            candidates[candidate]["votes"] += 1
        else:
            candidates[candidate] = {"votes": 1}


winner_name = max(candidates, key=lambda x: candidates[x]["votes"])
winner_votes = candidates[winner_name]["votes"]


print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, data in candidates.items():
    percentage = (data["votes"] / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({data['votes']})")
print("-------------------------")
print(f"Winner: {winner_name}")
print("-------------------------")

output_file_path = "election_results.txt"
with open(output_file_path, "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
    for candidate, data in candidates.items():
        percentage = (data["votes"] / total_votes) * 100
        output_file.write(f"{candidate}: {percentage:.3f}% ({data['votes']})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner_name}\n")
    output_file.write("-------------------------\n")

print(f"Election results have been printed to the terminal and saved to '{output_file_path}'.")

#Your analysis should align with the following results:

#```text
#Election Results
#-------------------------
#Total Votes: 369711
#-------------------------
#Charles Casper Stockham: 23.049% (85213)
#Diana DeGette: 73.812% (272892)
#Raymon Anthony Doane: 3.139% (11606)
#-------------------------
#Winner: Diana DeGette
#-------------------------
#```

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.