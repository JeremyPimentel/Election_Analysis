# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("election_results.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

winning_county = ""
winning_count_county = 0
winning_percentage_county = 0


#county votes
county_votes = {}
county_options = []

#open results and read file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)

    for row in file_reader:
        county_name = row[1]

        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1
    
# Open the election results and read the file.
    with open(file_to_load) as election_data:
        file_reader = csv.reader(election_data)
    # Read the header row.
        headers = next(file_reader)
    # Print each row in the CSV file.
        for row in file_reader:
        # Add to the total vote count.
            total_votes += 1
        # Get the candidate name from each row.
            candidate_name = row[2]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
            if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
                candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
                candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
            candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)
   
   
      
    for county_name in county_votes:
        # Retrieve vote count and percentage.
        votes_county = county_votes[county_name]
        vote_percentage_county = float(votes_county) / float(total_votes) * 100
        county_results = (
        f"\nCounty Votes:\n"
        f"{county_name}: {vote_percentage_county:.1f}% ({votes_county:,})\n"
        f"\n-------------------------\n")
        # Print each counties voter count and percentage to the terminal.
        print(county_results)
        #  Save the county results to our text file.
        txt_file.write(county_results)
      

        if (votes_county > winning_count_county) and (vote_percentage_county > winning_percentage_county):
            winning_count_county = votes_county
            winning_county = county_name
            winning_percentage_county = vote_percentage_county
            Largest_Turnout = (
            f"\nLargest County Turnout: {winning_county}\n")
       




    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
    print(Largest_Turnout)
    txt_file.write(Largest_Turnout)