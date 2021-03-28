import pathlib as path
import csv

with open('Resources/budget_data.csv', 'r') as budget_data_file:
    budget_data = csv.reader(budget_data_file, delimiter=',')

    header = next(budget_data)

    pnlamount_count = 0
    pnlamount_sum = 0
    pnlamount_change = 0
    pnlamount_0 = 0
    pnlamount_change_sum = 0
    min_pnlamount_change = 0
    max_pnlamount_change = 0
    pnlamount_change_avg = 0



    for pnlamount in budget_data:
        pnlamount = int(pnlamount[1])
        pnlamount_sum += pnlamount
        pnlamount_count += 1
        pnlamount_change = pnlamount - pnlamount_0
        pnlamount_0 = pnlamount
        pnlamount_change_sum += pnlamount_change


        if min_pnlamount_change == 0:
            min_pnlamount_change = pnlamount_change
        elif pnlamount_change > max_pnlamount_change:
            max_pnlamount_change = pnlamount_change
        elif pnlamount_change < min_pnlamount_change:
            min_pnlamount_change = pnlamount_change

    pnlamount_change_avg = pnlamount_change_sum / pnlamount_count

    print("Financial Analysis")
    print("Total Months: " + str(pnlamount_count))
    print("Total: $" + str(pnlamount_sum))
    print ("Average Change: $" + str(pnlamount_change_avg))
    print("Greatest Increase in Profits: $" + str(min_pnlamount_change))
    print("Greatest Decrease in Profits: $" + str(max_pnlamount_change))

    file_out = open("output.txt","w")
    file_out.write("Financial Analysis")
    file_out.write("Total Months: " + str(pnlamount_count))
    file_out.write("Total: $" + str(pnlamount_sum))
    file_out.write("Average Change: $" + str(pnlamount_change_avg))
    file_out.write("Greatest Increase in Profits: $" + str(min_pnlamount_change))
    file_out.write("Greatest Decrease in Profits: $" + str(max_pnlamount_change))


