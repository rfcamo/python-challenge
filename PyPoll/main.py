# Imports here
import os
import csv

# File Source
dirname = os.path.dirname(__file__)
data_source = os.path.join(dirname, "Resources", "election_data.csv")

total_votes = 0
candidates = []
vote_numbers = []
vote_percentage = []
winner =  ""

# CSV read and convert to dictionaries
with open(data_source, newline='') as election_data:
        reader = csv.reader(election_data)

        next(reader)
		
		# Loop to the rows
        for row in reader:
            if row[2] not in candidates:
                candidates.append(row[2])
                vote_numbers.append(1)
            else:
                index = candidates.index(row[2])
                vote_numbers[index] += 1
            total_votes += 1
		
		#Calculate vote percentages
        for votes in vote_numbers:
            percentages = "{0:.3f}".format(round((votes/total_votes)*100, 2))
            vote_percentage.append(percentages) 
        
		# Output winning candidate
        winning_candidate = vote_percentage.index(max(vote_percentage))
		# Output winning candidate
        winner = candidates[winning_candidate]
            
		
# Output results
output = (
	f"\nElection results\n"
	f"----------------------------\n"
	f"Total votes: {total_votes}\n"
	f"----------------------------\n"
	f"{candidates[0]}: {vote_percentage[0]}% ({vote_numbers[0]})\n"
	f"{candidates[1]}: {vote_percentage[1]}% ({vote_numbers[1]})\n"
	f"{candidates[2]}: {vote_percentage[2]}% ({vote_numbers[2]})\n"
	f"{candidates[3]}: {vote_percentage[3]}% ({vote_numbers[3]})\n"
	f"----------------------------\n"
	f"Winner: {candidates[0]}\n"
	f"----------------------------\n")

# Terminal output
print(output)
		
# Export to textfile
data_output = os.path.join(dirname,"analysis", "Pybank_Analysis.txt")

with open(data_output, "w") as txt_file:
    txt_file.write(output)
