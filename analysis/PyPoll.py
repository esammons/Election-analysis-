# Add our dependencies.
import csv
import os

#Assign a variable for the absolute path. This is not covered in class.
mainpath = os.path.dirname(__file__)
# Assign a variable to load a file from a path.
file_to_load = os.path.join(mainpath, "Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join(mainpath, "analysis", "election_analysis.txt")

# TVC1 - Initialize a total vote counter.
total_votes = 0
# CO1 - Declare an empty list with variable candidate options
candidate_options = []
# CV1 - Declare an empty dictionary 
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Print the file object.
    #print(election_data)
    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)
    
    # Read the header row. This assigns 1st row as header.
    headers = next(file_reader)
    # Print the header row.
    #print(headers)

    # TVC2 - Add to the total vote count.
    # Iterate through each row in the CSV file. 
    # Then assign total_votes as total of row.
    for row in file_reader:
        #Add to the total vote count.
        total_votes += 1

        # CO2 - Print the candidate name from each row.
        candidate_name = row[2]

        # CO3 - If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # CO4 - Add in candidate_options
            candidate_options.append(candidate_name)
            # CV2 - Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # CV3 - Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # Determine the percentage of votes for each candidate by looping through the counts.
        # PV1 - Iterate through the candidate list.

    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        #  To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        #print(candidate_name + ":" + str(vote_percentage) + str(votes))
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(f"{candidate_name}")


        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

        #  To do: print out the winning candidate, vote count and percentage to
        #   terminal.
# TV3 - Print total votes.
#print(total_votes)

# CO4 - Print the candidate list.
#print(candidate_options)

# CV - Print the candidate votes.
#print(candidate_votes)