# TODO
#Michael Albornoz
#Cash


check = True

while check: #check if input is number
    cents = input("How many cents is owed? ----> $")
    try:
        cents = float(cents)
        if cents>0:
            check = False
        else:
            print("Please enter valid amount")
    except:
        print("Wrong")

cents = round(cents * 100) #convert cents to whole numbers

pennies = 0
dimes = 0
nickels = 0
quarters = 0

while cents >= 25: #to see how many quarter can go through
    quarters = quarters + 1 #counter to count the coins
    cents = cents - 25 #subtract amt after one cycle
while cents >= 10:
    dimes = dimes + 1
    cents = cents - 10
while cents >= 5:
    nickels = nickels + 1
    cents = cents - 5
while cents >= 1:
    pennies = pennies + 1
    cents = cents - 1

coins = pennies + nickels + dimes + quarters #add them all together

print(coins)
