# -*- coding: UTF-8 -*-
""" python-challenge: PyPoll
    Zachary Hooks                """

# Import necessary modules
import csv
import os

# Files to load and output 
file_to_load = os.path.join("PyPoll","Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("PyPoll","analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
candidate_votes = {}  # Dictionary to store vote counts for each candidate

# Open CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        # Increment total vote count for each row
        total_votes += 1

        # Get candidate's name from the row
        candidate = row[2]

        # If candidate is not already in the candidate list, add them
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0

        # Add a vote to the candidate's count
        candidate_votes[candidate] += 1

# Determine winner based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Calculate vote percentages for each candidate
candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Generate election results summary
output_summary = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)
for candidate, votes in candidate_votes.items():
    percentage = candidate_percentages[candidate]
    output_summary += f"{candidate}: {percentage:.3f}% ({votes})\n"
output_summary += (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)

# Print output summary to the terminal
print(output_summary)

# Write the election analysis to the text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output_summary)