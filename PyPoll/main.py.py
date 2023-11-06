#import dependencies
import csv
import os

#file to load
file_to_load = os.path.join("Resources", "election_data.csv")

#file for final results
file_to_output = os.path.join("analysis", "election_analysis.txt")

#vote counter, candidate options, vote counters, winning candidate, winning count, 
ttl_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0

#read the csv file and convert into list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

#header reader
    header = next(reader)

    for row in reader:

        print(".", end=""),

        #add to the total vote count
        ttl_votes = ttl_votes + 1

        #extract the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidates
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        #then add vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# Print the results and export the data to our text file
with open(file_to_output, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results =(
        f"\nElection Results\n"
        f"---------------------\n"
        f"Total Votes: {ttl_votes}\n"
        f"---------------------\n)")
    print(election_results, end="")

    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Determine the winner by looping through the counts
    for candidate in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(ttl_votes) * 100

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # Print each candidate's voter count and percentage (to terminal)
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # Save each candidate's voter count and percentage to text file
        txt_file.write(voter_output)

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
