#In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. 
#You will be given a financial dataset called `budget_data.csv`. The dataset is composed of two columns: "Date" and "Profit/Losses".
#* The total number of months included in the dataset

#* The net total amount of "Profit/Losses" over the entire period
#* The changes in "Profit/Losses" over the entire period, and then the average of those changes
#* The greatest increase in profits (date and amount) over the entire period
#* The greatest decrease in profits (date and amount) over the entire period
import os
import csv

budget_csv = os.path.join(os.path.dirname(__file__), "Resources", "budget_data.csv")

total_months = 0
total_profit_losses = 0
previous_profit_loss = 0
profit_loss_changes = []
months = []

with open(budget_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    next(csv_reader)

    for row in csv_reader:
        total_months += 1

        total_profit_losses += int(row[1])

        if total_months > 1:
            profit_loss_change = int(row[1]) - previous_profit_loss
            profit_loss_changes.append(profit_loss_change)
            months.append(row[0])

        previous_profit_loss = int(row[1])

average_change = sum(profit_loss_changes) / len(profit_loss_changes)

greatest_increase = max(profit_loss_changes)
greatest_increase_month = months[profit_loss_changes.index(greatest_increase)]

greatest_decrease = min(profit_loss_changes)
greatest_decrease_month = months[profit_loss_changes.index(greatest_decrease)]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

text_file = "financial_analysis.txt"
with open(text_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_losses}\n")
    file.write(f"Average Change: ${round(average_change, 2)}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")

print(f"Results exported to {text_file}")

#Your analysis should align with the following results:

#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $22564198
#Average Change: $-8311.11
#Greatest Increase in Profits: Aug-16 ($1862002)
#Greatest Decrease in Profits: Feb-14 ($-1825558)
#```

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.