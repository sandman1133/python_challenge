# Importing required packages
import os
import csv
import pandas as pd

# path of csv file
csvpath = os.path.join("/OneDrive - Total Quality Financial/Documents/data course/HW/hw 3/Instructions/PyBank/Resources/budget_data.csv")

# Reading csv file
election_df = pd.read_csv(csvpath)

# Getting total number of votes
# The total number of votes will be the total number of rows in dataframe
# .shape returns total (rows, columns of a dataframe)
# Picking only rows using index 0
total_votes = election_df.shape[0]

# Using groupby() to first group the dataframe based on each candidate.
# Then using count() to count each rows i.e. it will count VOter ID and
# Country columns.
# So just retreiving 'Voter ID' columns count
candidate_group_by_count = election_df.groupby(['Candidate']).count()['Voter ID']

# candidate_group_by_count is a pandas series where an index is each unique candidate name
# and values are their corresponding vote counts
# Hence, retrieving candidate name and their corresponding vote counts in a list

# Getting list of all unique candidates
candidate_list = list(candidate_group_by_count.index)

# Getting list of vote count for corresponding candidates
candidate_vote_count_list = list(candidate_group_by_count.values)

# Calculating The percentage of votes each candidate won
candidate_vote_percent_list = []
for candidate_vote_count in candidate_vote_count_list:
  
  # Using below formula to calculate vote percentage
  # vote_percent = (vote for candidate * 100) / total votes
  vote_percent = (candidate_vote_count * 100) / total_votes
  
  # Rounding of the percetage till 3 digit precision
  vote_percent = round(vote_percent, 3)
  
  # Appending vote_percent for each candidate in a list
  candidate_vote_percent_list.append(vote_percent)

# Finding winner of election result
# Winner will be the candidate having maximum number of votes
# For this getting the index of list from candidate_vote_count_list
# where there is maximum number of votes
# Because using that index winning candidate name can be fetched from
# candidate list
index = candidate_vote_count_list.index(max(candidate_vote_count_list))
# Wiinning candidate
winner = candidate_list[index]

# Preparing the election result
## Concatenating the result in a variable so that it can printed directly
## as well as it can exported to text file without rewriting the same code again
election_result = 'Election Result:\n' # Adding \n to goto next line
election_result += '-'*20 # This will print '-' 20 times
election_result += f'\nTotal Votes: {total_votes}\n'
election_result += '-'*20

# Looping over candidate name, vote count and vote percent to print the desired output
for candidate_name, vote_percent, vote_count in zip(candidate_list, candidate_vote_percent_list, candidate_vote_count_list):
  election_result += f'\n{candidate_name}: {vote_percent}% ({vote_count})'

election_result += '\n'
election_result += '-'*20
election_result += f'\nWinner: {winner}\n'
election_result += '-'*20

# Printing the final election result
print(election_result)

# Writing the election result or say saving it in a text file
with open("election_result.txt", "w") as text_file:
  text_file.write(election_result)