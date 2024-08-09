# Create Path 
import os 
import csv

csvpath = os.path.join("Resources", "election_data.csv")

# Define Variables
total_votes = 0
candidate_name = []
candidate_vote = {}
names = []

# Read CSV File
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader) 

# Process each row
# The total number of votes each candidate won
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]

# A complete list of candidates who received votes 
        if candidate_name not in names:
            names.append(candidate_name)
        if candidate_name in candidate_vote:
            candidate_vote[candidate_name] += 1
        else:
            candidate_vote[candidate_name] =1


# The percentage of votes each candidate won
results = []
for candidate, votes in candidate_vote.items():
    percentage = (votes / total_votes) * 100
    results.append(f'{candidate}: {percentage:.3f}% ({votes})')

# The winner of the election based on popular vote 
winner = max(candidate_vote, key=candidate_vote.get)

# Print Results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for result in results:
    print(result)
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Create a text file of the results to add to analysis folder
output_path = os.path.join('analysis', 'election_results.txt')
with open(output_path, 'w') as file:
    file.write("Election Results\n")
    file.write("----------------------------")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("----------------------------")
    for result in results:
        file.write(result + '\n')
    file.write("----------------------------")
    file.write(f"Winner: {winner}\n")
    file.write("----------------------------")
