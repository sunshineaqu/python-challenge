import os
import csv

csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath, newline="") as csvfile: #open the csvfile
    csvreader = csv.reader(csvfile, delimiter=",") #read the file
    csv_header = next(csvfile) #skip the header

    total_votes = 0
    candList = [] #make a list for candidates
    voteList = [] #make a list to hold all the vote result
    
    for row in csvreader: #loop through entire rows
        voteList.append(row[2])
        total_votes += 1 #calculate the votes
        if row[2] not in candList:
            candList.append(row[2]) #get the candidate names
    
    print("Election Results")
    print("-------------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------------")
    
    for x in range(len(candList)):
        counts = voteList.count(candList[x])
        percentage = round((counts / total_votes *100),2)
        print(f"{candList[x]}: {percentage}% ({counts})")