import os
import csv

PyPoll_csv = os.path.join("Resources","election_data.csv")

total_votes = 0
candidate_list = {}
voter_percentage = {}
candidate_votes = 0
winner = ""

with open(PyPoll_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    first_row = next(csv_reader)


    for row in csv_reader:
        total_votes += 1

        if row[2] in candidate_list.keys():
            candidate_list[row[2]] += 1

        else:
            candidate_list[row[2]] = 1

    for key, value in candidate_list.items():
            voter_percentage[key] = round((value/total_votes)*100,2)

    for key in candidate_list.keys():

        if candidate_list[key] > candidate_votes:
            winner = key
            candidate_votes = candidate_list[key]

print(f"Election Results")
print("-------------------------------------")
print("Total: " + str(total_votes))
print("-------------------------------------")
for key, value in candidate_list.items():
    print (key + ": " + str(voter_percentage[key]) + "% (" + str(value) +")")
print("-------------------------------------")
print("Winner: " + winner)
print("-------------------------------------")

PyPoll_export = os.path.join("Analysis", "PyPoll.text")
with open('PyPoll.text', 'w+') as outfile:
    outfile.write(f"Election Results\n")
    outfile.write(f"---------------------------\n")
    outfile.write(f"Total: " + str(total_votes) + "\n")
    outfile.write(f"---------------------------\n")
    for key, value in candidate_list.items():
        outfile.write(key + ": " + str(voter_percentage[key]) + "% (" + str(value) + ")\n")
    outfile.write(f"---------------------------\n")
    outfile.write(f"Winner: " + winner + "\n")
    outfile.write(f"---------------------------\n")
