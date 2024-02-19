#Michael Albornoz
#Word Game
import random
import sys
from datetime import date
import json
import os.path

category = {
    "NFL": ["49ers", "bears", "bengals", "bills", "broncos", "browns", "buccaneers", "cardinals", "chargers", "chiefs", "colts", "commanders", "cowboys", "dolphins", "eagles", "falcons", "giants", "jaguars", "jets", "lions", "packers", "panthers", "patriots", "raiders", "rams", "ravens", "saints", "seahawks", "steelers", "texans", "titans", "vikings"],
    "NBA": ["76ers", "Bucks", "Bulls", "Cavaliers", "Celtics", "Clippers", "Grizzlies", "Hawks", "Heat", "Hornets", "Jazz", "Kings", "Knicks", "Lakers", "Magic", "Mavericks", "Nets", "Nuggets", "Pacers", "Pelicans", "Pistons", "Raptors", "Rockets", "Spurs", "Suns", "Thunder", "Timberwolves", "TrailBlazers", "Warriors", "Wizards"],
    "MLB": ["Angels", "Astros", "Athletics", "BlueJays", "Braves", "Brewers", "Cardinals", "Cubs", "Diamondbacks", "Dodgers", "Giants", "Guardians", "Mariners", "Marlins", "Mets", "Nationals", "Orioles", "Padres", "Pirates", "Phillies", "Rangers", "Rays", "Reds", "RedSox", "Rockies", "Royals", "Tigers", "Twins", "WhiteSox", "Yankees"],
}
#these are making the categories

def menu(): #this prints the menu
    print("|| ------------Word Game------------")
    print("|| ------------Options------------")
    print("||  1) NFL")
    print("||  2) NBA")
    print("||  3) MLB")
    print("||  4) Random")
    print("||  5) Scoreboard")
    print("||  6) Instructions")
    print("||  7) Exit")

def scoreboard(score, name): #this writes the score that was just played into a file
    today = date.today().strftime('%Y-%m-%d') #gets the date when the game was played
    scoreboardfile = { #makes the dict that records the name and score and date
            "Name" : name,
            "Score" : score,
            "Date" : today
            }
    with open('scoreboardtrack.txt', 'a') as file:
        file.write(json.dumps(scoreboardfile) + '\n') #writes the dict into a file line and \n after it does it
    menu()
    interface()


def displayscoreboard(): #if this function is called, it displays the past 5 scores
    scores = []
    with open('scoreboardtrack.txt', 'r') as file:
        for line in file: #for every line in the file
            scores.append(json.loads(line)) #it appends the line into a single value in the array
    sortedscores = sorted(scores, key=lambda x: x.get('Score', 0), reverse=True) #sorts the array by score
    print("Scoreboard")
    print(sortedscores[0])
    print(sortedscores[1])
    print(sortedscores[2])
    print(sortedscores[3])
    print(sortedscores[4]) #prints hgihest 5 scores
    yousee = input("\nMove On? ---- Y/N: ")
    if yousee == ord('Y') or yousee == ord('y'): #confirmation to move on
        menu()
        interface()

wordcat = 0
randomwordcat = 0
otherwords = 0
def frandom(): #choses random cat
    wordcat = list(category.keys())
    randomwordcat = random.choice(wordcat)
    randomwords = list(category[randomwordcat])
    chosenword = random.choice(randomwords)
    hangman(chosenword)

def cat1():#choses NFL cat
    nflword = list(category["NFL"])
    chosenword = random.choice(nflword)
    hangman(chosenword)

def cat2():#choses NBA cat
    nbaword = list(category["NBA"])
    chosenword = random.choice(nbaword)
    hangman(chosenword)

def cat3():#choses MLB cat
    mlbword = list(category["MLB"])
    chosenword = random.choice(mlbword)
    hangman(chosenword)

def winner(tries, length): #if the user wins the game, it calculates the score then prints it and asks for the name
    score = tries * int(length)
    print("Your score is ", end = '')
    print(score)
    nameget = input("What is your name: ")
    scoreboard(score, nameget)

def hangman(cword):
    wordchecker = False
    wordcheckerint = 0
    mistakes = 5
    mistakedoublechecker = 0
    hangmanword = ["_"]
    repeatchecker = []
    repeatcheckerint = -1
    winnerchecker = 0
    f = len(cword)

    for p in range (len(cword) - 1): #makes an array with the length of the chosen word but replaces the letters with _ to display to the user
        hangmanword.append("_")

    while wordchecker == False: #runs the program while the user hasnt won yet
        print("")
        print("--------------------------")
        for k in range (len(cword)): #prints the array from line 101 to the user
            print(hangmanword[k], end = ' ')
        lettergetter = input("\nPlease type a letter: ") #gets input from user
        print("--------------------------")

        repeatcheckerint = repeatcheckerint + 1
        repeatchecker.append(lettergetter)

        for j in range (repeatcheckerint):
            if ord(lettergetter) == ord(repeatchecker[j]):
                print("No repeats") #if the user repeats a letter theyve used before, it loses them the game
                mistakes = mistakes - 1 #subtracts the

        for i in range (len(cword)): #checks for every letter in the word
            if ord(cword[i]) == ord(lettergetter): #if the letter chosen by the user matches one in thw chosen word

                hangmanword[i] = str(lettergetter) #that letter will be revealed
                mistakedoublechecker = mistakedoublechecker + 1 #this makes sure that if the letter found is in thw word mutiple times (go line 124)

        if mistakedoublechecker >= 1:
            mistakes = mistakes + 0 #the mistakes wont increase
        else:
            mistakes = mistakes - 1 #subtracts a mistake if wrong

        mistakedoublechecker = 0 #resets the checker back to zero so it can work again

        if mistakes <= 0: #if mistakes runs out, they lost
            print("Oh No!!! You lost :(")
            print("Your word was -------> ", end = ' ') #reveals the chosen word
            print(cword)
            menu() #goes back to menu
            interface()


        for q in range (10):
            print("")
        print("------------------------------------------------------")
        print("Mistakes Left: ", end = ' ')
        print(mistakes) #prints how many mistakes are left in the round

        for v in range (len(cword)):
            if ord(hangmanword[v]) == ord('_'):
                winnerchecker = winnerchecker + 1 #this loop checks to see if the user has guessed all the letters
# if the array no longer has any _, then the user has guessed all the letters

        if winnerchecker == 0:
            wordchecker = True #releases the while loop on line 104
            for e in range (10):
                print("")
            print("Congrats you won!!!")
            winner(mistakes, f) #calls the winner function

        winnerchecker = 0 #resets the winner checker bc it will run again if the user hasnt guessed all the words

menuint = 0
programrun = True #keeps the program running

def instructions():
    print("|| ------------Word Game------------")
    print("|| ------------Instructions------------")
    print("||  1) You are playing Hangman")
    print("||  2) Pick a category or pick a random one")
    print("||  3) The program will give you a word based on your decision")
    print("||  4) Guess the word letter by letter until you guess the whole word")
    print("||  5) If you guess a letter that is not in the word OR you guess a letter you have already guessed, you will lose a mistake")
    print("||  6) If you guess a letter you have already guessed that was wrong, you will lose more mistakes than usual")
    print("||  7) You have 5 mistakes")
    print("||  8) Once you guess the word, your socre will be based on your mistakes and how long the word was")
    print("||  9) Have Fun")
    yougood = input("\nDo you understand? ---- Y/N: ")
    if yougood == ord('Y') or yougood == ord('y'): #clarification if the user can move on
        menu()
        interface()

def interface(): #menu code
    menuint = input("Please select a choice: ")
    if int(menuint) == 1:
        cat1()

    if int(menuint) == 2:
        cat2()

    if int(menuint) == 3:
        cat3()

    if int(menuint) == 4:
        frandom()

    if int(menuint) == 5:
        displayscoreboard()

    if int(menuint) == 6:
        instructions()

    if int(menuint) == 7:
        programrun = False
        sys.exit()

while(programrun == True): #keeps the program running
    menu()
    interface()




