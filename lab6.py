#Denzel Young
#Lab 6: Probability

#For any code involving proability, methods from "random" and "math" will be required
import random
import math

#The first method throws darts at a circle as described in the problem, and using the
#number of hits and misses, attempts to estimate the value of pi.
#Upon testing, 1,000,000 throws recorded the value 3.144304 
def piProbability():
    #The number of attempts is entered by the user and a hit counter is initialized at 0
    numAttempts = int(input("Please enter the number of attempts: "))
    numHit = 0
    #Next, the program "throws" the darts at the board based on the user's input
    for x in range(0, numAttempts):
        #A random x any y coordinate are chosen first
        xCoord = random.uniform(-1.0,1.0)
        yCoord = random.uniform(-1.0,1.0)
        #Then the distance from the center is calculated. If it is less than 1, the dart hit the board.
        distFromCenter = math.sqrt(pow(xCoord,2) + pow(yCoord,2))
        if distFromCenter <= 1.0:
            numHit = numHit + 1.0
    #Finally, an estimation of pi is calculated using the ratio pi = 4m/n
    #Where m is the number of hits and n is the number of attempts.
    pi = (4 * numHit)/numAttempts
    print ("Based on the experiment, pi is estimated to be ", pi)

#The second method replicates the Monty Hall problem, using probability over a large number of trials to
#see if, given 3 doors and 1 winning solution, would it be better to stay with the door you have chosen,
#Or to change doors after one of the losing doors has been revealed.
def gameShowProbability():
    #NUMTRIALS is 20 because the program operates on user input, an alterative version called autoGameShowProbability
    #Does this 1000 times automatically without printing every win and loss. This version allows the tester to see
    #what exactly is happening.
    NUMTRIALS = 20
    #The list of doors will be randomized every time the loop is run while the counters keep track of winning and
    #losing results.
    doors = ["goat", "goat", "car"]
    originalWins = 0
    originalLosses = 0
    newWins = 0
    newLosses = 0
    #This first loop runs based on the assumption that the user will keep the door that they have selected.
    for i in range (0, NUMTRIALS):
        #The doors are shuffled, meaning that "car" will be in a new place every time.
        random.shuffle(doors)
        #Then the user is asked which door they would like to choose. If it matches the address of the door,
        #They have won, if not, then they get a goat.
        choice = int(input("Please choose a door! 1, 2, or 3: "))
        if doors[choice - 1] == "car":
            print ("You won the brand new car!")
            originalWins = originalWins + 1
        else:
            print ("Well...you can't take the goat with you, sorry, you lose!")
            originalLosses = originalLosses + 1

    #This loop is making the assumption that the user will change their selection once they have been
    #shown a losing door.
    for j in range (0, NUMTRIALS):
        #As before, the doors are shuffled and the user is asked for an input.
        random.shuffle(doors)
        choice = int(input("Please choose a door! 1, 2, or 3: "))
        #This time though, the host will pick a door too. If that door is the winning door or the same
        #as the player's door, then the host will pick again until they have a losing door.
        hostChoice = random.randint(0,2)
        while doors[hostChoice] == "car" or hostChoice == choice:
            hostChoice = random.randint(0,2)
        #Now that a losing door has been revealed a chain of if-elif statements will change the door
        #chosen by the player depending on the host's choice and the player's choice.
        print ("I am going to eliminate one of the losing doors and open door number", (hostChoice + 1))
        print ("So let's switch your pick to the other unopened door and see if you won!")
        if hostChoice == 0 and choice == 1:
            choice = 2
        elif hostChoice == 0 and choice == 2:
            choice = 1
        elif hostChoice == 1 and choice == 0:
            choice = 2
        elif hostChoice == 1 and choice == 2:
            choice = 0
        elif hostChoice == 2 and choice == 0:
            choice = 1
        elif hostChoice == 2 and choice == 1:
            choice = 0
        #Then, as in the loop that did not change the door, the result is chosen.
        if doors[choice - 1] == "car":
            print ("You won the brand new car!")
            newWins = newWins + 1
        else:
            print ("Well...you can't take the goat with you, sorry, you lose!")
            newLosses = newLosses + 1

    #After each loop has run its number of times, the winning percent for each choice (pick new door or stay)
    #is calculated and, depending on the greater one, prints a statement recommending the best course of action.
    originalWinPercent = (originalWins/NUMTRIALS) * 100
    newWinPercent = (newWins/NUMTRIALS) * 100
    print ("When you kept the same door, you won ", originalWins, "times!")
    print ("That's ", originalWinPercent, "%")
    print ("But when you changed doors, you won ", newWins, "times!")
    print ("That's ", newWinPercent, "%")

    if originalWinPercent > newWinPercent:
        print ("I guess that means you should stick by your choice!")
    elif originalWinPercent == newWinPercent:
        print ("In that case, it really doesn't matter does it?")
    elif originalWinPercent < newWinPercent:
        print ("You should change your choice if you wanna drive out of here in a new car!")
        
        

#As this is simply an automatic version of the above program, I will only comment where changes have occurred
def autoGameShowProbability():
    #No one wants to spend their time choosing 1000 x 2 (each scenario) doors, so this one will be automatically done.
    NUMTRIALS = 1000
    doors = ["goat", "goat", "car"]
    originalWins = 0
    originalLosses = 0
    newWins = 0
    newLosses = 0
    #This first loop runs based on the assumption that the user will keep the door that they have selected.
    for i in range (0, NUMTRIALS):
        #The doors are shuffled, meaning that "car" will be in a new place every time.
        random.shuffle(doors)
        #This time, the choice is randomly selected by the program itself and no "win" or "loss" statement
        #is printed.
        choice = random.randint(0,2)
        if doors[choice - 1] == "car":
            originalWins = originalWins + 1
        else:
            originalLosses = originalLosses + 1
    #This loop is making the assumption that the user will change their selection once they have been
    #shown a losing door.
    for j in range (0, NUMTRIALS):
        #The user input has been replaced by a pseudo-random number generator between 0 and 2
        #mimicing a random choice made by a human
        random.shuffle(doors)
        choice = random.randint(0,2)
        #This time though, the host will pick a door too. If that door is the winning door or the same
        #as the player's door, then the host will pick again until they have a losing door.
        hostChoice = random.randint(0,2)
        while doors[hostChoice] == "car" or hostChoice == choice:
            hostChoice = random.randint(0,2)
        #The print statements are gone, but the door choice is still switched here by the "player"
        if hostChoice == 0 and choice == 1:
            choice = 2
        elif hostChoice == 0 and choice == 2:
            choice = 1
        elif hostChoice == 1 and choice == 0:
            choice = 2
        elif hostChoice == 1 and choice == 2:
            choice = 0
        elif hostChoice == 2 and choice == 0:
            choice = 1
        elif hostChoice == 2 and choice == 1:
            choice = 0
        #Then, as in the loop that did not change the door, the result is chosen.
        if doors[choice - 1] == "car":
            newWins = newWins + 1
        else:
            newLosses = newLosses + 1
    #After each loop has run its number of times, the winning percent for each choice (pick new door or stay)
    #is calculated and, depending on the greater one, prints a statement recommending the best course of action.
    #These print statements will remain as the will give insight as to the number of wins and losses as well
    #as the chance of success with each scenario.
    originalWinPercent = (originalWins/NUMTRIALS) * 100
    newWinPercent = (newWins/NUMTRIALS) * 100
    print ("When you kept the same door, you won ", originalWins, "times!")
    print ("That's ", originalWinPercent, "%")
    print ("But when you changed doors, you won ", newWins, "times!")
    print ("That's ", newWinPercent, "%")
    if originalWinPercent > newWinPercent:
        print ("I guess that means you should stick by your choice!")
    elif originalWinPercent == newWinPercent:
        print ("In that case, it really doesn't matter does it?")
    elif originalWinPercent < newWinPercent:
        print ("You should change your choice if you wanna drive out of here in a new car!")
