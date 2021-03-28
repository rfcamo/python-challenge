# Imports here
import os
import csv


# Files to load and output
dirname = os.path.dirname(__file__)
data_source = os.path.join(dirname, "Resources", "budget_data.csv")


# Track various revenue parameters
total_months = 1
change_month = []
revenue_change_list = []
great_increase = ["", 0]
great_decrease = ["", 0]
total_revenue = 0

# Read the csv and convert it into a list of dictionaries
with open(data_source) as budget_data:
    reader = csv.DictReader(budget_data, delimiter=",")
	

    # Extract first row to avoid appending to revenue_change_list
    first_row = next(reader)
    total_revenue = total_revenue + int(first_row["Profit/Losses"])
    prev_revenue = int(first_row["Profit/Losses"])
		
	
    for row in reader:
	
		# Totals
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Profit/Losses"])

        # Revenue change
        revenue_change = int(row["Profit/Losses"]) - prev_revenue
        prev_revenue = int(row["Profit/Losses"])
        revenue_change_list = revenue_change_list + [revenue_change]
        change_month = change_month + [row["Date"]]

        # Greatest increase and decrease
        if revenue_change > great_increase[1]:
            great_increase[0] = row["Date"]
            great_increase[1] = revenue_change
        else:
            revenue_change < great_decrease[1]
            great_decrease[0] = row["Date"]
            great_decrease[1] = revenue_change
    
# Average Revenue Change
avg_revenue = sum(revenue_change_list) / len(revenue_change_list)

# Summary Output
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue Change: ${round(avg_revenue, 2)}\n"
    f"Greatest Increase in Revenue: {great_increase[0]} (${great_increase[1]})\n"
    f"Greatest Decrease in Revenue: {great_decrease[0]} (${great_decrease[1]})\n")

# Terminal Output
print(output)

# Export to textfile
data_output = os.path.join(dirname,"analysis", "Pybank_Analysis.txt")

with open(data_output, "w") as txt_file:
    txt_file.write(output)
