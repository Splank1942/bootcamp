#def dollarizer():
 #  return input1.replace("s", "$") 

#def eurizer():
 #  return input1.replace("e", "€")

def replacer():
   return input1.replace("s", "$").replace("e", "€").replace("i", "£").replace(input2, input3)

input1 = input("Please provide a word ").lower()

input2 = input("please define character to be replaced ")

input3 = input("please define replacement character ")

print(replacer())

def celsius_to_farenheit():
    return farenheit

celsius = int(input("what is the temperature in celcius? "))   

farenheit = celsius * 9/5 + 32

print(celsius_to_farenheit())

def age_in_days():
    return in_days

    
in_years = int(input("How old are you in years? "))

in_days = in_years * 365

print(age_in_days())

def simple_interest():
    return si


principle = int(input("Enter the principle amount "))

rate = int(input("Enter the interest rate "))

time = int(input("Enter time in years "))

si = principle * rate * time

print(simple_interest())

def plan_finances():
    return target < si 

principle = int(input("Enter the principle amount "))

rate = int(input("Enter the interest rate "))

time = int(input("Enter time in years "))

si = principle * rate * time

target = int(input("enter your target return amount "))
 
print(plan_finances())