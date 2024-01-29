# The first function to define the cost of a hotel stay multiplied by the user input.

def hotel_cost(num_nights):
    return num_nights * 650

# The second function we are checking to make sure input matches an option.

def plane_cost(city_flight):
    if city_flight == '1':
        return 500
    if city_flight == '2':
        return 750
    if city_flight == '3':
        return 400
    if city_flight == '4':
        return 250
    else:
        print ("\nInvalid Destination") # Making sure to give an output if an unlisted item is selected. 

# Third function for much like the hotel_cost will have us multiply by the user input and store it.

def car_rental(rental_days):
    return rental_days * 80

# Final function will take our totals and add them together in order to give the user a total and breakdown of their costs.

def holiday_cost(num_nights, city_flight, rental_days):
    num_nights = hotel_cost(num_nights)
    city_flight = plane_cost(city_flight)
    rental_days = car_rental(rental_days)
    return num_nights + city_flight + rental_days
   
# List of locations to display for the user to choose from.

locations = ['1. Dubai International Airport',
             '2. London Heathrow Airport',
             '3. Amsterdam Airport Schiphol',
             '4. Paris-Charles de Gaulle Airport']

# Getting our first user input to store in our variable to callback to.
while True:
    print ("_" * 60)
    city_flight = input("\nWhere are you flying to?""\n""\n" 
             + "\n".join(locations) 
             + "\n""\n""Please Select option as 1,2,3 or 4.\n")

# Creating a short if/else block to store their chosen destination seperately for displaying their information back to them.

    if city_flight == '1': 
        airport = 'Dubai International Airport'
    elif city_flight == '2':
        airport = 'London Heathrow Airport'
    elif city_flight == '3':
        airport = 'Amsterdam Airport Schiphol'
    elif city_flight == '4':
        airport = 'Paris-Charles de Gaulle Airport'
    else:
        print ("\nInvalid Destination, Try again.\n")
        continue

    while True:
        print ("_" * 60)   
        num_nights = (input("\nHow many nights will you be staying?\n"))
        if num_nights.isalpha():
            print ("\nInput must be numeric, Try again.\n")
            continue
        else:
            num_nights = int(num_nights)
            
        
        while True:
            print("_" * 60)
            rental_days = (input("\nHow many days will you need a car for?\n"))
            if rental_days.isalpha():
                print ("\nInput must be numeric, Try again.\n")
                continue
            else:
                rental_days = int(rental_days)

# Calculating the totals for the user and giving them a complete breakdown of their trip cost.

                total = holiday_cost(num_nights,city_flight,rental_days)
                print("_" * 60)
                print (f"""
The total cost of your trip will be £{total}\n
The break down is as follows;\n
Flight to {airport}: £{plane_cost(city_flight)}
Hotel cost for {num_nights} nights : £{hotel_cost(num_nights)}
Private car rental for {rental_days} days : £{car_rental(rental_days)}
""")

                print("_" * 60)
                break
        break
