# TODO
# Michael Albornoz
# Readability

graded_sentence = input("Text: ") #to get the input needed
k = 0
csentence = 0
cletters = 0
cwords = 0

while k < len(graded_sentence): #to loop to each letter in the array is scanned
    if graded_sentence[k] == '?' or graded_sentence[k] == '.' or graded_sentence[k] == '!': #if the ASCII value matches any puncation marks
        csentence = csentence + 1 #then there is one more sentence in the text

    if graded_sentence[k] == ' ': #if the ASCII value matches a space text
        cwords = cwords + 1 #then there is one more word in the text

    if str(graded_sentence[k]).isalpha(): #if the ASCII value matches any letters
        cletters = cletters + 1 #then there is one more letter in the text

    k = k + 1 #in order for the text scanner to use arrays, the varible k must go up

cwords = cwords + 1 #since there is one less space in every single sentence, one more word must be added to the total

index = round(0.0588 * (cletters / cwords * 100) - 0.296 * (csentence / cwords * 100) - 15.8) #Coleman-Liau formula

if index > 16: #if above 16, then print
    print("Grade 16+")

elif index < 1: #if below 1, then print
    print("Before Grade 1")

else: #if between, print the index 
    print("Grade", end = ' ')
    print(index)
