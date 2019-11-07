import random                                                               #imports random module

guesses_taken = 0                                                           #assign 0 to "guesses_taken" variable

print('Hello! What is your name?')                                          #prints out 'Hello! What is your name?')
myName = input()                                                            #it expects a name as input and assings it to "myName" variable

number = random.randint(1, 20)                                              #assign a random value, between 1 and 20, to "number" variable
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  #prints out 'Well, ' the value of myName variabile ',I am thinking...

while guesses_taken < 6:                                     #loops the code indented under 'while' function as long as guesses_taken variabile is smaller than 6
    print('Take a guess.')                                                  #prints out 'Take a guess.'
    guess = input()                                                         #it expects a value as input and assings it to "guess" variable                                         
    guess = int(guess)                                                      #converts "guess" to decimal number

    guesses_taken += 1                                                      #increments "guesses_taken" by 1

    if guess < number:                                                      #prints out 'Your guess is too low.' only if "guess" smaller than "number"
        print('Your guess is too low.')                                     #condition is met

    if guess > number:                                                      #prints out 'Your guess is too high.' only if "guess" bigger than "number"
        print('Your guess is too high.')                                    #condition is met

    if guess == number:                                                     #terminates the loop only if "guess" equals to "number"
        break

if guess == number:                                                         #if "guess" equals to "number" condition is met
    guesses_taken = str(guesses_taken)                                      #converts "guesses_taken" to string
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!')  #prints out 'Good job....

if guess != number:                                                         #if "guess" different from "number" condition is met
    number = str(number)                                                    #converts "number" to string
    print('Nope. The number I was thinking of was ' + number)               #prints 'Nope. The number...
