# UW23-python-challenge

PyBank and PyPoll

a) PyBank

Task - to analyze the company financial records

Files:

budget_data.csv - financial records with "Date" and "Profit/Losses" data
main.py - python script to analyze the records to calculate the below. The analysis is printed to the terminal and  text file is exported with the results.
  - The total number of months included in the dataset

  - The net total amount of "Profit/Losses" over the entire period

  - The changes in "Profit/Losses" over the entire period, and then the average of those changes

  - The greatest increase in profits (date and amount) over the entire period
  
  - The greatest decrease in profits (date and amount) over the entire period

Output.txt - Analysis result

  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $22564198
  Average Change: $-8311.11
  Greatest Increase in Profits: Aug-16 ($1862002)
  Greatest Decrease in Profits: Feb-14 ($-1825558)

b) PyPoll

Task - to help a small, rural town modernize its vote-counting process

Files:
election_data.csv - poll dataset composed of three columns: "Voter ID", "County", and "Candidate".
main.py - Python script that analyzes the votes and calculates each of the following values below. The script prints both the analysis to the terminal and export a text file with the results.

  - The total number of votes cast

  - A complete list of candidates who received votes

  - The percentage of votes each candidate won

  - The total number of votes each candidate won

  - The winner of the election based on popular vote

output.txt - analysis with below election results:

Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
