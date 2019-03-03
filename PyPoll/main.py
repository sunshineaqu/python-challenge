import os
import csv

csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath, newline="") as csvfile: #open the csvfile
    csvreader = csv.reader(csvfile, delimiter=",") #read the file
    csv_header = next(csvfile) #skip the header

    votes = 0
    counts = 0
    candList = [] #make a list for candidates
    voteList = [] #make a list to hold all the vote result
    
    for row in csvreader: #loop through entire rows
        voteList.append(row[2])
        votes += 1 #calculate the votes
        if row[2] not in candList:
            candList.append(row[2]) #get the candidate names
    
    
    for row in csvreader:
        for x in candlist:
            if candList[x] == row[2]:
                count += 1
        print(f"{x} has {count}")

exit(0)

    '''
    #how to define the variable to 
    for x in range(votes-1)

    NoteList = []
    candList[0]
    ..
    candList[len(candList)-1]

    
    print("Election Results")
    print("-------------------------------")
    print(f"Total Votes: {votes}")