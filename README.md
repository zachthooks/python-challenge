# python-challenge

Overview

This repository contains two Python scripts that solve real-world data analysis problems using Python scripting skills. These scripts, PyBank and PyPoll, help automate data analysis tasks for financial records and election data, respectively. The solutions leverage basic Python concepts such as loops, conditionals, file handling, and list operations to achieve the desired outcomes.
Repository Structure

The repository is organized as follows:

bash

python-challenge/
│
├── PyBank/
│   ├── main.py              # The main Python script for PyBank analysis
│   ├── Resources/
│   │   └── budget_data.csv   # The financial dataset used in PyBank
│   └── analysis/
│       └── financial_analysis.txt  # The exported text file with the analysis results
│
├── PyPoll/
│   ├── main.py              # The main Python script for PyPoll analysis
│   ├── Resources/
│   │   └── election_data.csv # The election dataset used in PyPoll
│   └── analysis/
│       └── election_results.txt   # The exported text file with the analysis results
│
└── README.md                # This file explaining the project

PyBank

Objective: Analyze financial data to provide insights into profit/loss trends.
Dataset

The dataset budget_data.csv contains two columns:

    Date: The date of the financial record (month-year format)
    Profit/Losses: The net amount of profit or loss for the given month

Script Functionality

The main.py script reads the financial data from the CSV file and performs the following calculations:

    Total Months: Counts the total number of months in the dataset.
    Net Total of Profit/Losses: Calculates the net total amount of profit/loss over the entire period.
    Average Change: Computes the average change in profit/loss between consecutive months.
    Greatest Increase in Profits: Identifies the date and amount of the largest increase in profits.
    Greatest Decrease in Profits: Identifies the date and amount of the largest decrease in profits.

Output

    Terminal Output: The script prints the analysis results directly to the terminal.
    Text File: The results are also exported to a text file named financial_analysis.txt in the analysis/ folder.

Example Output

yaml

Financial Analysis
----------------------------
Total Months: 86
Total: $22,564,198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1,862,002)
Greatest Decrease in Profits: Feb-14 ($-1,825,558)

PyPoll

Objective: Analyze election data to determine key voting results.
Dataset

The dataset election_data.csv contains three columns:

    Voter ID: A unique identifier for each voter.
    County: The county where the vote was cast.
    Candidate: The candidate that the vote was cast for.

Script Functionality

The main.py script reads the election data from the CSV file and performs the following calculations:

    Total Votes: Counts the total number of votes cast.
    Candidate List: Creates a complete list of candidates who received votes.
    Vote Percentage: Calculates the percentage of total votes each candidate received.
    Vote Count: Tallies the total number of votes each candidate received.
    Election Winner: Determines the candidate with the highest number of votes.

Output

    Terminal Output: The script prints the election results directly to the terminal.
    Text File: The results are also exported to a text file named election_results.txt in the analysis/ folder.

Example Output

markdown

Election Results
-------------------------
Total Votes: 369,711
-------------------------
Charles Casper Stockham: 23.049% (85,213)
Diana DeGette: 73.812% (272,892)
Raymon Anthony Doane: 3.139% (11,606)
-------------------------
Winner: Diana DeGette

How to Run

To run the scripts:

    Clone this repository to your local machine.

    Navigate to the PyBank or PyPoll folder.

    Ensure the required CSV files are located in the Resources folder.

    Execute the Python script (main.py) using the following command:

    bash

    python main.py

Both scripts will print the analysis to the terminal and save the results in a text file within the analysis folder.

Dependencies

    Python 3.x
    CSV module (included in Python standard library)

Conclusion

These Python scripts demonstrate how to use basic programming techniques to automate the analysis of real-world datasets. By completing this project, I learned how to efficiently read large datasets, manipulate data, and extract key insights using Python, offering a scalable solution beyond the capabilities of Excel.
