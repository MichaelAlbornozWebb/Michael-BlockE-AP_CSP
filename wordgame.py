#Michael Albornoz
#Word Game
import random
import sys
from datetime import date
import json

category = {
    "NFL": ["49ers", "bears", "bengals", "bills", "broncos", "browns", "buccaneers", "cardinals", "chargers", "chiefs", "colts", "commanders", "cowboys", "dolphins", "eagles", "falcons", "giants", "jaguars", "jets", "lions", "packers", "panthers", "patriots", "raiders", "rams", "ravens", "saints", "seahawks", "steelers", "texans", "titans", "vikings"],
    "NBA": ["76ers", "Bucks", "Bulls", "Cavaliers", "Celtics", "Clippers", "Grizzlies", "Hawks", "Heat", "Hornets", "Jazz", "Kings", "Knicks", "Lakers", "Magic", "Mavericks", "Nets", "Nuggets", "Pacers", "Pelicans", "Pistons", "Raptors", "Rockets", "Spurs", "Suns", "Thunder", "Timberwolves", "TrailBlazers", "Warriors", "Wizards"],
    "MLB": ["Angels", "Astros", "Athletics", "BlueJays", "Braves", "Brewers", "Cardinals", "Cubs", "Diamondbacks", "Dodgers", "Giants", "Guardians", "Mariners", "Marlins", "Mets", "Nationals", "Orioles", "Padres", "Pirates", "Phillies", "Rangers", "Rays", "Reds", "RedSox", "Rockies", "Royals", "Tigers", "Twins", "WhiteSox", "Yankees"],
}

def menu():
    print("|| ------------Word Game------------")
    print("|| ------------Options------------")
    print("||  1) NFL")
    print("||  2) NBA")
    print("||  3) MLB")
    print("||  4) random")
    print("||  5) scoreboard")
    print("||  6) Exit")

def scoreboard(score, name):
    today = date.today().strftime('%Y-%m-%d')
    scoreboardfile = {
            "Name" : name,
            "Score" : score,
            "Date" : today
            }

    with open("scoreboard.txt", 'a') as f:
        f.write(json.dumps(scoreboardfile))

def displayscoreboard():
    i = 0

wordcat = 0
randomwordcat = 0
otherwords = 0
def frandom():
    wordcat = list(category.keys())
    randomwordcat = random.choice(wordcat)
    randomwords = list(category[randomwordcat])
    chosenword = random.choice(randomwords)
    hangman(chosenword)

def cat1():
    nflword = list(category["NFL"])
    chosenword = random.choice(nflword)
    hangman(chosenword)

def cat2():
    nbaword = list(category["NBA"])
    chosenword = random.choice(nbaword)
    hangman(chosenword)

def cat3():
    mlbword = list(category["MLB"])
    chosenword = random.choice(mlbword)
    hangman(chosenword)

def winner(tries, length):
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
    print(cword)

    for p in range (len(cword) - 1):
        hangmanword.append("_")

    while wordchecker == False:
        print("")
        print("--------------------------")
        for k in range (len(cword)):
            print(hangmanword[k], end = ' ')
        lettergetter = input("Please type a letter: ")
        print("--------------------------")

        repeatcheckerint = repeatcheckerint + 1
        repeatchecker.append(lettergetter)
        print(repeatchecker)

        for j in range (repeatcheckerint):
            if ord(lettergetter) == ord(repeatchecker[j]):
                print("No repeats")
                mistakes = mistakes - 1
                break

        for i in range (len(cword)):
            if ord(cword[i]) == ord(lettergetter):

                hangmanword[i] = str(lettergetter)
                mistakedoublechecker = mistakedoublechecker + 1

        if mistakedoublechecker >= 1:
            mistakes = mistakes + 0
        else:
            mistakes = mistakes - 1

        mistakedoublechecker = 0

        if mistakes <= 0:
            print("Oh No!!! You lost :(")
            print("Your word was -------> ", end = ' ')
            print(cword)
            menu()
            interface()


        for q in range (10):
            print("")
        print("------------------------------------------------------")
        print("Mistakes Left: ", end = ' ')
        print(mistakes)

        for v in range (len(cword)):
            if ord(hangmanword[v]) == ord('_'):
                winnerchecker = winnerchecker + 1


        if winnerchecker == 0:
            wordchecker = True
            for e in range (10):
                print("")
            print("Congrats you won!!!")
            winner(mistakes, f)


        winnerchecker = 0

menuint = 0
programrun = True

def interface():
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
        programrun = False
        sys.exit()

while(programrun == True):
    menu()
    interface()




