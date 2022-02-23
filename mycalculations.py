# This is the fist, base file

inital_appartment_cost = 1000000
initial_appartment_founds = 220000
first_mortage = 150000
second_mortage = 0
print("What is your FIRST mortage percentage: ")
first_mortage_rate = float(input())
first_mortage_rate = first_mortage_rate/100
print("What is your SECOND mortage percentage: ")
second_mortage_rate = float(input())
second_mortage_rate = second_mortage_rate/100


print("What is your work estimate (k): ")
estimated_work = int(input())
estimated_work = estimated_work * 1000

second_mortage = inital_appartment_cost - first_mortage
second_mortage = second_mortage + estimated_work
total_appartment_cost = inital_appartment_cost + estimated_work
second_mortage = total_appartment_cost - first_mortage

print(f'Your initial appartment costs : {inital_appartment_cost} and your founds are calculated on {initial_appartment_founds} CHF')
print(f'Your want {estimated_work} CHF, making the total costs of and your founds are calculated on {total_appartment_cost} CHF')
print(f'Your first mortage of {100*first_mortage_rate}) % will cost you {first_mortage_rate*first_mortage} CHF per year')
