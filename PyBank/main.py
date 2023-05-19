# Analyze the financial records in budget_data.csv financial dataset

#Dependencies
import os
import csv

#Set file for financial dataset
budget_data_csv = os.path.join("Resources", "budget_data.csv")


title = "Financial Analysis"

print(title)

print("-----------------------------------------")

# List variables to store data
date = []
profit = []
netchange = []

# Set initial value
netchange.append(0)


# Open and read csv
with open(budget_data_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    # Read the header row first
    csv_header = next(csv_file)
    for row in csvreader:
        # Create list of dates to calculate total number of months and list of profits
        date.append(row[0])
        profit.append(int(row[1]))

#Total number of months
total_months = len(date)

# Convert the integer months into a string and print
print("Total Months: " + str(total_months))

print("")
print(f'Total: ${sum(profit)}')

# Calculate the changes in Profit/Loss over the entire period and then the average of those changes
for i in range(len(profit)-1):
    netchange.append(int(profit[i+1])-int(profit[i]))

# Calculate the average
def average(netchange):
    length = len(profit)-1
    total = 0.0
    for x in netchange:
        total += x
    return round(total/length,2)  


print(f'Average Change: ${average(netchange)}')

# Calculate the greatest increase in profits over the entire period
maximum = max(netchange)
print(f'Greatest Increase in Profits: {date[netchange.index(maximum)]} (${maximum})')

# Calculate the greatest decrease in profits over the entire period
minimum = min(netchange)

print(f'Greatest Decrease in Profits: {date[netchange.index(minimum)]} (${minimum})')

# Specify the file to write to
output_path = os.path.join("Analysis","output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the rows
    csvwriter.writerow([title])
    csvwriter.writerow(["-----------------------------------------"])
    csvwriter.writerow([f'Total Months: {str(total_months)}'])
    csvwriter.writerow([f'Total: ${sum(profit)}'])
    csvwriter.writerow([f'Average Change: ${average(netchange)}'])
    csvwriter.writerow([f'Greatest Increase in Profits: {date[netchange.index(maximum)]} (${maximum})'])
    csvwriter.writerow([f'Greatest Decrease in Profits: {date[netchange.index(minimum)]} (${minimum})'])
    