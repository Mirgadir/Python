import os
import csv
budget_data = os.path.join("Resources","budget_data.csv")

with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    month_count = 0
    net_total = 0
    my_dict={}
    #combine row lists in one dictionary
    for row in csvreader:
        if row[0] != 0:
            month_count = month_count + 1    
            my_dict[row[0]]=row[1]
    
    
#convert dictionary values to list    
my_dict_list = list(my_dict.values())
#convert dictionary keys to list
dif_keys = list(my_dict.keys())
#remove first month from the list
dif_keys.pop(0)
#convert list items to integers                   
my_dict_list = [int(i) for i in my_dict_list]
#calculate sum of all items in the list
net_total = sum(my_dict_list)

#create a new list and populate calculated difference between months items to that list
dif = []
dif = [my_dict_list[i+1] - my_dict_list[i] for i in range(len(my_dict_list)-1)]

#calculate average of difference numbers
average = 0
average = sum(dif) / (month_count - 1)

#find Gtreatest Increase and Decrease
month_ind_maxi = 0
month_ind_maxi = dif.index(max(dif))

maxi_month = dif_keys[month_ind_maxi]


month_ind_mini = dif.index(min(dif))
mini_month = dif_keys[month_ind_mini]


maxi = max(dif)
mini = min(dif)

#print everything to terminal
print("\nFinancial Analysis")
print("------------------------------------------")
print(f"Total Months: {month_count}") 
print(f"Total: ${net_total}")
print('Average  Change: $' + "{:07.2f}".format(average))
print(f"Greatest Increase in Profits: {maxi_month} (${maxi})")
print(f"Greatest Decrease in Profits: {mini_month} (${mini})")

#output to txt file
file_to_output = os.path.join("Analysis", "budget_analysis.txt")
a = "Financial Analysis"
b = "------------------------------------------"
c = f"Total Months: {month_count}"
d = f"Total: ${net_total}"
e = 'Average  Change: $' + "{:07.2f}".format(average)
f = f"Greatest Increase in Profits: {maxi_month} (${maxi})"
g = f"Greatest Decrease in Profits: {mini_month} (${mini})"
n = '\n' 

output = f'{a} \n{b} \n{c} \n{d} \n{e} \n{f} \n{g}'
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
