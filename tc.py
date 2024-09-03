import math 

fds = 13200 
cds = 4609
nyds = 8000

def fit(income, percent):
    return (income * percent) / 100

def fin_tax(total_income:float) -> float:
    if total_income <= 10400:
        return 0.10
    elif total_income <= 41225:
        return 0.12
    elif total_income <= 89400:
        return 0.22
    elif total_income <= 174050:
        return 0.24
    elif total_income <= 215400:
        return 0.32
    elif total_income <= 549900:
        return 0.35
    else:
        return 0.37

def cin_tax(total_income:float) -> float:
    if total_income <= 10420:
        return 0.01
    elif total_income <= 24684:
        return 0.02
    elif total_income <= 38959:
        return 0.04
    elif total_income <= 54081:
        return 0.06
    elif total_income <= 68350:
        return 0.08
    elif total_income <= 349137:
        return 0.093
    elif total_income <= 418961:
        return 0.103
    elif total_income <= 698271:
        return 0.113
    else:
        return 0.123   

def nyin_tax(total_income:float) -> float:
    if total_income <= 8500:
        return 0.04
    elif total_income <= 11700:
        return 0.045
    elif total_income <= 13900:
        return 0.0525
    elif total_income <= 21400:
        return 0.059
    elif total_income <= 80650:
        return 0.0645
    elif total_income <= 215400:
        return 0.0685
    elif total_income <= 10777550:
        return 0.0882
    else:
        return 0.103    

def state_tax(total_income):
    if state == "California":
       return cin_tax(total_income) * (total_income - cds)
    else:
       return nyin_tax(total_income) * (total_income - nyds)


total_income = float(input("What is your gross yearly income? "))
state = input("What state do you live in? ")
ftax = fin_tax(total_income) * (total_income - fds) 
stax = state_tax(total_income)
ttax = ftax + stax 
takehome = total_income - ttax
print(f"total federal tax to be paid is {ftax}")
print(f"total tax to be paid is {ttax}")
print(f" Your yearly take home income is {takehome}")






##print("Welcome to the tax calculator")

##income = input("What is your gross yearly income? ")





#def calculate_california_tax() 

#def calculate_new_york_tax()





