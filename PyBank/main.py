import os
import csv

#set path for file    
csvpath = os.path.join("Resources", "budget_data.csv")

#open the file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #read the header row first
    csv_header = next(csvfile)

    monthList = []
    profitList = []
    profitchangeList = []

    #create a list of profit values
    for row in csvreader:
        monthList.append(row[0])
        profitList.append(int(row[1]))
    #calculate month and total based on the profit list    
    months = len(monthList)
    total = sum(profitList)

    print("Financial Analysis")
    print("-------------------------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${total}")

    #calculate average change
    first_profit = profitList[0]
    last_profit = profitList[len(profitList) - 1]
    average = round((last_profit - first_profit) / (months - 1), 2)
   
    print(f"Average Change: ${average}")

    for x in range(months-1):
        profitchange = profitList[x+1] - profitList[x]
        profitchangeList.append(profitchange)
    profit_increase = max(profitchangeList)
    profit_decrease = min(profitchangeList)

    month_increase = monthList[profitchangeList.index(profit_increase)+1]
    month_decrease = monthList[profitchangeList.index(profit_decrease)+1]

    print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")
    print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")

#print to a text file
    f = open("finance.txt", "w")
    f.write("Financial Analysis\n")
    f.write("-------------------------------------\n")
    f.write(f"Total Months: {months}\n")
    f.write(f"Total: ${total}\n")
    f.write(f"Average Change: ${average}\n")
    f.write(f"Greatest Increase in Profits: {month_increase} (${profit_increase})\n")
    f.write(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})\n")
    f.close()

    