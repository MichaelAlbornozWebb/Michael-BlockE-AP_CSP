# TODO
#Michael Albornoz
#Credit

cardnum = input("Card Number: ")

eodstrlen = len(cardnum) - 2 #starting the strlen at -2 will make it start at the second to last digit
eodsum = 0
eodsum2 = 0

while eodstrlen > -1: #doing every other digit
    eod = (2 * int(cardnum[eodstrlen])) #doubles each digit
    if eod > 10: #if it is a double digit whe doubled
        eods = str(eod)
        eodsum = eodsum + int(eods[1]) + int(eods[0]) #split the digit
    else:
        eodsum = eodsum + eod
    eodstrlen = eodstrlen - 2

eodstrlen2 = len(cardnum) - 1 #the other digits
while eodstrlen2 > -1:
    eodsum2 = eodsum2 + int(cardnum[eodstrlen2]) #adding them together
    eodstrlen2 = eodstrlen2 - 2

cardnumsum = eodsum + eodsum2 #total sum of the checksum

checker = cardnumsum % 10
if checker != 0: #checks if invalid
    print("INVALID")

if int(len(cardnum)) == 15: #AMEX checker
    print("AMEX")

if int(len(cardnum)) == 16 and int(cardnum[0]) == 5 and int(cardnum[1]) < 6: #MC checker
    print("MASTERCARD")

if (int(len(cardnum)) == 13 or int(len(cardnum)) == 16) and int(cardnum[0]) == 4: #VISA checker
    print("VISA")

else: #in case the checksum is correct but doesn't follow the credit card requirements
    print("INVALID")
