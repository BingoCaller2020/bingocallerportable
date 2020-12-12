#Importing functions
import random
import time
import webbrowser
import ctypes

version = '1.1.0'

ctypes.windll.kernel32.SetConsoleTitleW("Bingo Caller Portable")
#Welcome Message
print('Welcome to Bingo Caller Portable Version ' + version)

print('Would you like to send the developers an email about this program?')
questionEmail = input('Enter \'Y\' for yes and \'N\' for no: ')
if questionEmail == 'y':
       webbrowser.open('mailto:software.bingocallerapp@outlook.com', new=2)

else:
       print('After you type a value, press Enter to submit it.')
       #Pause
       time.sleep(0.4)

       #Main process
       def begin():
              try: numberOfRounds = int(input('How many numbers would you like generated for this: '))
              except ValueError:
                     numberOfRounds = int(input('Please enter a valid number '))
       #Checks if the user is happy with the amount of numbers being called in the game
              confirmRounds = input('Are you sure? Enter \'Y\' for yes and \'N\' for no: ')
              #Loops until valid input
              while confirmRounds != 'y' and confirmRounds != 'n':
                     
                     confirmRounds = input('Invalid input. Enter \'Y\' for yes and \'N\' for no: ')

              #Loops until user sure about number of rounds
              while confirmRounds == 'n':
                     try: numberOfRounds = int(input('How many numbers would you like generated for this game? '))
                     except ValueError:
                            numberOfRounds = int(input('Please enter a valid number '))
                     confirmRounds = input('Are you sure? Enter \'Y\' for yes and \'N\' for no: ')
              while confirmRounds != 'y' and confirmRounds != 'n':
                     confirmRounds = input('Invalid input. Enter \'Y\' for yes and \'N\' for no: ')

              #If happy, the loops end, and the code contines
              if confirmRounds == 'y':
                     print('Lets play bingo!')
                     ready = input('Press Enter to get your first number: ')
              #To start the game, the user can hit ENTER. Any other value is also accepted to avoid errors.
              if ready >= '':
              #The game has started, and a variable is declared as a random number between 0 and 90
                            nextNumber = random.randint(0,90)
              #A list is created for numbers already called to go in
                            alreadyCalled = []
              #A while loop is initiated, so long a x is less than the number of rounds inputted on line 17
                            x = 0
              while x < numberOfRounds:
              #The number is reset if it has already been called; x stays the same
                     if nextNumber in alreadyCalled:
                                   nextNumber = random.randint(1,90)
                                   
              #If the number hasn't been called, then it is included in the list, printed, and reset.
                     elif nextNumber not in alreadyCalled:
                            alreadyCalled.append(nextNumber)
                            print (nextNumber)
                            nextNumber = random.randint(1,90)
                            input("Press Enter to view next drawn number")
                            x +=1
              #Ends the loop when conditions met
                     else:
                            break
              
              #When all numbers are called...
              print ('You have reached your selected amount of numbers')
              time.sleep(0.5)

       #Actually runs the game
       begin()
       #Asks if they want to play again
       again = input('Would you like to play again? Enter \'Y\' for yes and \'X\' to exit: ')
       #Loops until valid input
       while again != 'y' and again != 'x':
              again = input('Invalid input. Enter \'Y\' for yes and \'X\' to exit: ')
       #The game loops until the user declars 'x'
       while again == 'y':
              begin()
              again = input('Would you like to play again? Enter \'Y\' for yes and \'X\' to exit: ')
       while again != 'y' and again != 'x':
              again = input('Invalid input. Enter \'Y\' for yes and \'X\' to exit: ')

       if again == 'x':
              print ('Goodbye and thank you for playing Bingo Caller Portable Version ' + version)
              time.sleep(1.21)