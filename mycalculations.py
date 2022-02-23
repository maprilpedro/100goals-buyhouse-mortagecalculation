# This is the fist, base file

inital_appartment_cost = 1000000
initial_appartment_founds = 220000
first_mortage = 150000
second_mortage = 0
amortisment = 733
total_amortisment = amortisment*12*3
nebencosten = 6800/12

print("What is your FIRST mortage percentage: ")
first_mortage_rate = float(input())
first_mortage_rate = first_mortage_rate/100
print("What is your SECOND mortage percentage: ")
second_mortage_rate = float(input())
second_mortage_rate = second_mortage_rate/100


print("What is your work estimate (kCHF): ")
estimated_work = int(input())
estimated_work = estimated_work * 1000

second_mortage = inital_appartment_cost - first_mortage
second_mortage = second_mortage + estimated_work
total_appartment_cost = inital_appartment_cost + estimated_work
second_mortage = total_appartment_cost - (first_mortage + initial_appartment_founds)

total_cost_3y = first_mortage * first_mortage_rate
total_cost_3y = total_cost_3y + (second_mortage*second_mortage_rate)
total_cost_3y = nebencosten + amortisment + (total_cost_3y)/12
total_cost_12y = (second_mortage_rate*second_mortage)
total_cost_12y = nebencosten + total_cost_12y/12

print(f'Your initial appartment costs : {inital_appartment_cost} and your founds are calculated on {initial_appartment_founds} CHF')
print(f'Your want {estimated_work} CHF, making the total costs of and your founds are calculated on {total_appartment_cost} CHF')
print(f'Your first mortage total is {first_mortage} CHF of {round(100*first_mortage_rate,2)} % will cost you {round(first_mortage_rate*first_mortage,2)} CHF per year')
print(f'Your second mortage total of {second_mortage} CHF of {round(100*second_mortage_rate,2)} % will cost you {round(second_mortage_rate*second_mortage,2)} CHF per year')
print(f'Your amortisment is {amortisment} CHF per month, and nebencosten {nebencosten} CHF')
print(f'You will pay for the first 3 years {round(total_cost_3y,2)} CHF per month')
print(f'You will pay for the next 12 years {round(total_cost_12y,2)} CHF per month, with amortisment removed !')
print(f'Your amortisment total is {total_amortisment} CHF, thus you shall pay {first_mortage-total_amortisment} CHF to close the first amortisment')
