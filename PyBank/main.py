# -*- coding: UTF-8 -*-
""" python-challenge: PyBank
    Zachary Hooks                """

# Dependencies
import csv
import os

# Files to load and output 
file_to_load = os.path.join("PyBank","Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("PyBank","analysis", "budget_analysis.txt")  # Output file path

# Defining variables to track the financial data
total_months = 0
total_net = 0
prev_profit = None
changes = []
greatest_increase = {"date": None, "amount": float('-inf')}
greatest_decrease = {"date": None, "amount": float('inf')}

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip header row
    header = next(reader)

    # Loop through each row of data
    for row in reader:
        # Extract date and profit/losses
        date = row[0]
        profit = int(row[1])

        # Track total number of months
        total_months += 1

        # Track net total of "Profit/Losses"
        total_net += profit

        # Calculate changes in "Profit/Losses" and track them
        if prev_profit is not None:
            change = profit - prev_profit
            changes.append(change)

            # Calculate greatest increase in profits 
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = change

            # Calculate greatest decrease in profits 
            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = change

        # Set previous profit to the current one for the next iteration
        prev_profit = profit

# Calculate average change across the months
average_change = sum(changes) / len(changes) if changes else 0

# Generate financial analysis summary
output_summary = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']:.2f})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']:.2f})\n"
)

# Print output summary to the terminal
print(output_summary)

# Write the financial analysis to the text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output_summary)