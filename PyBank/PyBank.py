import os
import csv

PyBank_csv = os.path.join("Resources", "budget_data.csv")

with open(PyBank_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)

    Total_Months = 0
    Total_Net = 0
    Changes = 0
    Monthly_List = []
    Greatest_Increase = ["", 0]
    Greatest_Decrease = ["", 9999]

    # The first row
    first_row = next(csv_reader)
    Total_Months += 1
    Total_Net += int(first_row[1])
    Previous_Net = int(first_row[1])

    for row in csv_reader:
        Total_Months += 1
        Total_Net += int(row[1])
        # Print(row[1]

        Changes = int(row[1]) - Previous_Net
        Previous_Net = int(row[1])
        Monthly_List += [Changes]

        if Changes > Greatest_Increase[1]:
            Greatest_Increase[1] = Changes
            Greatest_Increase[0] = row[0]

        if Changes < Greatest_Decrease[1]:
            Greatest_Decrease[1] = Changes
            Greatest_Decrease[0] = row[0]

Average = sum(Monthly_List) / len(Monthly_List)

Results = (
    f"Financial Analysis\n"
    f"---------------------\n"
    f"Total_Months: {Total_Months}\n"
    f"Total: ${Total_Net}\n"
    f"Average Change: ${Average}\n"
    f"Greatest Increase in Profits: {Greatest_Increase[0]} (${Greatest_Increase[1]})\n"
    f"Greatest Decrease in Profits: {Greatest_Decrease[0]} (${Greatest_Decrease[1]})"
    )

print(Results)

PyBank_export = os.path.join("Analysis", "PyBank.text")
with open('PyBank.text', 'w+') as outfile:
    outfile.write(f"Financial Analysis\n")
    outfile.write(f"---------------------\n")
    outfile.write(f"Total_Months: {Total_Months}\n")
    outfile.write(f"Total: ${Total_Net}\n")
    outfile.write(f"Average Change: ${Average}\n")
    outfile.write(f"Greatest Increase in Profits: {Greatest_Increase[0]} (${Greatest_Increase[1]})\n")
    outfile.write(f"Greatest Decrease in Profits: {Greatest_Decrease[0]} (${Greatest_Decrease[1]})")
