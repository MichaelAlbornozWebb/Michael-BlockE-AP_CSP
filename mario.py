# TODO
#Michael Albornoz
#Mario-More

check = True

while check:

    height = input("Height: ")
    try:
        height = int(height)
        if height>0 and height < 9:
            check = False
        else:
            print("Please enter a number between 1 - 8")
    except:
        print("That was not a number")


    #given code by teacher to check if height was acceptable

f = height
g = 0

for i in range (height): #prints 'height' many lines

    f = f - 1
    for j in range (f):
        print(" ", end = '') #prints the spaces needed in first line
    g += 1
    for k in range (g): #prints the hashes needed first line first half
        print("#", end = '')
    print(" ", end = ' ') #prints space in between
    for l in range (g): #prints hashes needed first line second half
        print("#", end = '')
    print('')

#subtract the amount of spaces printed by 1 and add 1 to the amount of hashes printed when going to next line
