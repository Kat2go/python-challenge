#enter Dependencies
import csv
import os

#files to load
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("analysis", "budget_analysis.txt")

#parameters
total_months = 0
month_change = []
net_change_list = []
greatest_inc = ["", 0]
greatest_dec = ["", 9999]
total_net = 0

#Read the csv and convert to dictionaries. 
#header
with open(file_to_load) as fin_data:
    reader = csv.reader(fin_data)

    header = next(reader)

    # Extract first row 
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:

        #get total months and net
        total_months += 1
        total_net += int(row[1])

        #get net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_change += [row[0]]

        # get greatest inc
        if net_change > greatest_inc[1]:
            greatest_inc[0] = row[0]
            greatest_inc[1] = net_change

        # get greatest dec
        if net_change < greatest_dec[1]:
            greatest_dec[0] = row[0]
            greatest_dec[1] = net_change

# get the Average Net Change
net_monthly_avg = sum(net_change_list) / len(net_change_list)

# get Output Summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_inc[0]} (${greatest_inc[1]})\n"
    f"Greatest Decrease in Profits: {greatest_dec[0]} (${greatest_dec[1]})\n")

# Print output
print(output)

# Export to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)


    