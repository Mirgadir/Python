import os
import csv
election_data = os.path.join("Resources","election_data.csv")

with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    
    #steps to calculate total number of votes and call it total_votes:
    vote_list=[row[2] for row in csvreader] 
    total_votes = 0
    total_votes = len(vote_list)


#make a candidates list 
candidates_list = [] 
for x in vote_list:
    if x not in candidates_list:
        candidates_list.append(x)

#calculate votes for each candidate, find percentages
candidates_num_list = [] 
candidates_percent_list = []
candidates_num_list = [vote_list.count(item) for item in candidates_list] 
z = 0
while z < len(candidates_num_list):
    candidates_percent_list.append(candidates_num_list[z]/total_votes)
    z = z + 1
 
#assign winner
winner_index = 0
winner_index = candidates_num_list.index(max(candidates_num_list))
winner = candidates_list[winner_index]

#print results to terminal
print("\nElection Results")
print("--------------------------------")
print(f"Total Votes:  {total_votes}")
print("--------------------------------")
print(candidates_list[0] + ': ' + "{:.3%}".format(candidates_percent_list[0]) + ' ' + '(' + str(candidates_num_list[0]) + ')')
print(candidates_list[1] + ': ' + "{:.3%}".format(candidates_percent_list[1]) + ' ' + '(' + str(candidates_num_list[1]) + ')')
print(candidates_list[2] + ': ' + "{:.3%}".format(candidates_percent_list[2]) + ' ' + '(' + str(candidates_num_list[2]) + ')')
print(candidates_list[3] + ': ' + "{:.3%}".format(candidates_percent_list[3]) + ' ' + '(' + str(candidates_num_list[3]) + ')')
print("--------------------------------")
print(f"Winner: {winner}")
print("--------------------------------")


#output to txt file
file_to_output = os.path.join("Analysis", "budget_analysis.txt")
a = "\nElection Results"
b = "--------------------------------"
c = f"Total Votes:  {total_votes}"
d = "--------------------------------"
e = candidates_list[0] + ': ' + "{:.3%}".format(candidates_percent_list[0]) + ' ' + '(' + str(candidates_num_list[0]) + ')'
f = candidates_list[1] + ': ' + "{:.3%}".format(candidates_percent_list[1]) + ' ' + '(' + str(candidates_num_list[1]) + ')'
g = candidates_list[2] + ': ' + "{:.3%}".format(candidates_percent_list[2]) + ' ' + '(' + str(candidates_num_list[2]) + ')'
h = candidates_list[3] + ': ' + "{:.3%}".format(candidates_percent_list[3]) + ' ' + '(' + str(candidates_num_list[3]) + ')'
i = "--------------------------------"
j = f"Winner: {winner}"
k = "--------------------------------"
n = '\n' 

output = f'{a} \n{b} \n{c} \n{d} \n{e} \n{f} \n{g} \n{h} \n{i} \n{j} \n{k}'
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
