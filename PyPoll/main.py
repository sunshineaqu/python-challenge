import os
import csv

csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath, newline="") as csvfile: #open the csvfile
    csvreader = csv.reader(csvfile, delimiter=",") #read the file
    csv_header = next(csvfile) #skip the header

    total_votes = 0
    candList = [] #make a list for candidates
    voteList = [] #make a list to hold all the vote result
    countList = [] #make a list to hold the corresponding number of votes for each candi
    
    for row in csvreader: #loop through entire rows
        voteList.append(row[2])
        total_votes += 1 #calculate the votes
        if row[2] not in candList:
            candList.append(row[2]) #get the candidate names
    
    f = open("output.txt", "w") #new file for write
    f.write("Election Results\n")
    f.write("-------------------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write("-------------------------------\n")
    
    for x in range(len(candList)):
        counts = voteList.count(candList[x]) #count the candidate name in votelist
        countList.append(counts) #add the number to countlist
        percentage = round((counts / total_votes *100),2)
        f.write(f"{candList[x]}: {percentage}% ({counts})\n")
    
    winner_index = countList.index(max(countList)) # get the winner name using index

    f.write("-------------------------------\n")
    f.write(f"Winner: {voteList[winner_index]}\n")
    f.write("-------------------------------\n")
    f.close()

    f = open("output.txt", "r") #open the file as r
    file_contents = f.read() 
    print(file_contents)  # print to terminal
    f.close()
    
