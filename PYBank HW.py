import csv
import os

book_budgets = ("1","2")

for books in book_budgets:
	total_months = 0
	total_revenue = 0
	first_month_revenue = 0
	revenue_change = 0
	revenu_1 = 0
	revenue_data = {}
	total_revenue_change = 0
	average_revenue_change = []
	

	csv_file = os.path.join("raw_data","budget_data_"+ books +".csv")
	
	data_output = os.path.join("output","budget_data_"+ books +".txt")

	with open(csv_file, 'r') as csvfile:
		
		csv_reader = csv.reader(csvfile, delimiter=",")
		
		next(csv_reader, None)

		for row in csv_reader:
			if len(average_revenue_change) == 0:
				first_month_revenue = int(row[1])
				average_revenue_change.append(row[1])
				revenue_date = row[0]
				revenue_data[revenue_date] = first_month_revenue
			else:
				revenue_change = revenue_1 - int(row[1])
				average_revenue_change.append(revenue_change)
				total_revenue_change = total_revenue_change + revenue_change	
			revenue_date = row[0]
			revenue_data[revenue_date] = revenue_change
			revenue_1 = int(row[1])
			total_months = total_months + 1
			total_revenue = total_revenue + int(row[1])
		average_revenue_change = round((total_revenue_change)/total_months,2)
		print("================================")
		print("budget_data_"+ books +".csv")
		print("================================")
		print("Total Months: "+ str(total_months))
		print("Total Revenue: $"+ str(total_revenue))	
		print("Average Revenue Change: $"+str(average_revenue_change))
		for revenue_date, revenue_value in revenue_data.items():
			max_date = max(revenue_date, key=revenue_data.get)
			min_date = min(revenue_date, key=revenue_data.get)
			print("Greatest Increase in Revenue: " + max(revenue_data, key=revenue_data.get) + " ($"+ str((revenue_data[max_date])) + ")")
			print("Greatest Decrease in Revenue: " + min(revenue_data, key=revenue_data.get) + " ($"+ str((revenue_data[min_date])) + ")")
			break
		print("=================================")
		
		max_revenue_increase = max(revenue_data, key=revenue_data.get)
		max_increase_date = str((revenue_data[max_date]))
		max_revenue_decrease = str((revenue_data[min_date]))
		max_decrease_date = min(revenue_data, key=revenue_data.get)
		
		csvWriter = open("budget_data_"+books+".txt", "w+")

		csvWriter.write("=======================\n")
		csvWriter.write("budget_data_"+ books +".csv\n")
		csvWriter.write("=======================\n")
		csvWriter.write("Total Months: "+ str(total_months))
		csvWriter.write("\nTotal Revenue: $"+ str(total_revenue))	
		csvWriter.write("\nAverage Revenue Change: $"+str(average_revenue_change))
		for revenue_date, revenue_value in revenue_data.items():
			max_date = max(revenue_data, key=revenue_data.get)
			min_date = min(revenue_data, key=revenue_data.get)
			csvWriter.write("\nGreatest Increase in Revenue: " + max(revenue_data, key=revenue_data.get) + " ($"+ str((revenue_data[max_date])) + ")")
			csvWriter.write("\nGreatest Decrease in Revenue: " + min(revenue_data, key=revenue_data.get) + " ($"+ str((revenue_data[min_date])) + ")")
			break
		csvWriter.write("\n========================")
		
		csvWriter.close()

