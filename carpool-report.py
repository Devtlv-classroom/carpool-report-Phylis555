# Variables
cars_available = 100
drivers = 30
waiting_passengers = 90
max_in_car = 5

# My Report :
print("the number of cars available is:", cars_available)
print("the number of drivers registered is:", drivers)
print("the number of empty cars today:", cars_available - (waiting_passengers + drivers) / max_in_car)
print("the number of passengers that can be transported today:", drivers * 4)
print("the average of passengers to put in each car:", cars_available / drivers )


