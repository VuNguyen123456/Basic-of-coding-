#Greeting the user
print('Pet Love Vet Weekly Profit Calculator')
#Input for total patient in the week
total_patients = int( input( "Total patients this week: "))
#Input for total charged per payment
per_patients = float( input( "Total charged per patient: "))
#Input for part-timers hourly payment
hourly_pay = int( input( "Part timer's hourly pay: "))
#Input for number of part-timers
num_pt = int( input( "Number of part-timers: "))
#Input for total hours that part-timers work a week
hour_worked = int( input( "Part-timers total hours worked: "))
#Input for total supply cost
supply_cost = float( input( "Total supply costs: "))
#Input for the overhead fees
overhead = float(input( "Overhead fees: "))
#Newline
print()
#calculate and display the gross made
gross_made = total_patients * per_patients
print("Gross Made:\t"+ str(float(round(gross_made,2))))
#calculate and display the total paid to part-timers
paid = (((hour_worked - (hour_worked - (num_pt*20)))*hourly_pay) + 
       ((hour_worked - (num_pt*20))*(hourly_pay * 1.5)))
print('Total paid to Part-Timers:\t' + str(round(paid,2)))
#calculate total taxes paid
taxs = gross_made * (15/100)
print("Total tax paid:\t"+str(round(taxs,2)))
#calculate the net profit for the week
net_profit = gross_made - (paid + taxs + supply_cost + overhead)
print("Net Profit for the Week:\t" + str(round(net_profit,2)))
