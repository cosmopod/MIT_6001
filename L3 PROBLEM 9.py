
# In this problem, you'll create a program that guesses a secret number!

# The program works as follows: you (the user) thinks of an integer between 0 and 100 (not inclusive).
# The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!


minNum = 0
midNum = 50
maxNum = 100
guess = "Is your secret number: "
print"Please think of a number between 0 and 100!"
print guess + str(midNum) + "?"
request = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
while request != 'c':
    if  request == 'h':
        maxNum = midNum
        midNum = int((midNum + minNum)/2)
    elif request == 'l':
        minNum = midNum
        midNum = int((midNum + maxNum)/2)
    else:
        print"Sorry, I did not understand your input."
    print guess + str(midNum) + "?"
    request = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
if request == 'c':
    print "Game over. Your secret number was:" + str(midNum)
