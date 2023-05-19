#Python script that analyzes the votes and calculates the winner

#Dependencies
import os
import csv

#set path for poll data
election_data_csv = os.path.join("Resources", "election_data.csv")

title = "Election Results"

ballot_id = []
candidates = []
votes = []

# Open and read csv
with open(election_data_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    # Read the header row first
    csv_header = next(csv_file)
    for row in csvreader:
        # Make list of ballot ids for vote count
        ballot_id.append(row[0])
        # Make list of candidates
        if row[2] not in candidates:           
            candidates.append(row[2])
        votes.append(row[2])

#Count total number of votes cast
total_votes = len(ballot_id)

#Print election results
print(title)
print("-----------------------------------------")
print(f'Total Votes: {total_votes}')
print("-----------------------------------------")

vote_count = []

#Calculate the percentage of votes each candidate won
percentages = ''
for candidate in candidates:
    percentages += candidate + ": " + str(round((votes.count(candidate)/total_votes)*100,3) ) + "% (" + str(votes.count(candidate))+")" + "\n"
    vote_count.append(votes.count(candidate))
print(percentages)

maximum=max(vote_count)

# Calculate the winner of the election based on popular vote
print("-----------------------------------------")
winner = candidates[vote_count.index(maximum)]
# Print the winner
print(f'Winner: {candidates[vote_count.index(maximum)]}')

print("-----------------------------------------")

# Set output path for text file
output_path = os.path.join("Analysis","output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as textfile:


    #Write the results to file
    textfile.write(f'{title} \n')
    textfile.write("----------------------------------------- \n")
    textfile.write(f'Total Votes: {total_votes} \n')
    textfile.write(f'----------------------------------------- \n')
    textfile.write(f'{percentages} \n')
    textfile.write(f"----------------------------------------- \n")
    textfile.write(f'Winner: {winner} \n')
    textfile.write("-----------------------------------------")

