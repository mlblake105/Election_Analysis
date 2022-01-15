#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. Thetotal number of votes each candidate won
#5. The winner of the election based on popular vote
import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join("resources", "election_results.csv")
#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#1. initialize a total vote counter
total_votes =0
#Candidate options
candidate_options = []
#1. Declare the empty dictonary
candidate_votes = {}
#open the election results and read the file.
#Winning candidate and winning count tracker
winning_candidate= ""
winning_count =0
winning_percentage=0
with open(file_to_load) as election_data:
    #To do: read and analyze the data here
    file_reader=csv.reader(election_data)
    #Read and print the header row
    headers=next(file_reader)
    #Print each row in the CSV file
    for row in file_reader:
        #2. Add to the total vote count.
        total_votes += 1
        #Print the candidate name from each row
        candidate_name = row[2]
        #if the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name]=0
        #add a vote to that candidate's count.
        candidate_votes[candidate_name] +=1 
#save the results to our text file
with open(file_to_save, "w") as txt_file:
    #print the final vote count to the terminal 
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results,end="")
    #save the final vote count to the text file
    txt_file.write(election_results) 

    #Determine the percentage of votes for each candidate by looping through the counts
    #1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        #2. Retrieve vote count of a candidate.
        votes=candidate_votes[candidate_name]
        #3. Calculate the percentage of votes.
        vote_percentage= float(votes)/float(total_votes)*100
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,}).\n")
        candidate_results =(
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
           
        #To do: print out each candidate's name, vote count, and percentage of 
        #votes to the terminal.
        print(candidate_results)
        #save the candidate results to our text file.
        txt_file.write(candidate_results)
        #Determine winning vote count and candidate
        #Determine if the votes is greater than the winning count.
        if (votes> winning_count) and (vote_percentage > winning_percentage):
            #if true then set winning_count = votes and winning_percent =
            #vote_percentage.
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
                
                
                
    #To do: print out the winning candiate, vote count and percentage to
    # terminal.
    #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
        
    #print (winning_candidate_summary)
    print(winning_candidate_summary)

    #save the candidate results to our text file
    txt_file.write(winning_candidate_summary)