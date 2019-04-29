#Jason Kildare
#this program is a trivia game that stores a users highest score in a file called highscore

#end game function
def endGame(n,p,c):
    #game count
    count = c
    #if users first time playing, read highscore file
    if count == 1:
        infile = open('highscore.txt', 'r')
        line1 = infile.readline()
        #if highscore file is empty, write to file
        if line1 == '':
            outfile = open('highscore.txt', 'w')
            outfile.write(str(n+','))
            outfile.write(str(p))
            outfile.close()

        #if file is not empty, compare previous scores to current scores    
        if line1 != '':
            #split text file by line
            prevName,prevPoints = line1.split(',')

            #if previoues score is less than current score
            #add new highscore to file
            if int(prevPoints) < p:
                newScore = p
                #open file
                outfile = open('highscore.txt', 'w')
                #write to file
                outfile.write(str(n+','))
                outfile.write(str(newScore))
                #close file
                outfile.close()

            #if previous score is greater than current score
            #keep previous scores in file
            elif int(prevPoints) > p:
                return

    #if user played more than once
    if count >=2:
        infile = open('highscore.txt', 'r')
        line1 = infile.readline()
        prevName,prevPoints = line1.split(',')

        #if previous scores are less than current score, add new score to file
        if int(prevPoints) < p:
            infile = open('highscore.txt', 'w')
            newScore = str(prevPoints)
            infile.write(str(prevName+','))
            infile.write(str(newScore))
            infile.close()
        # if previous scores are greater than current scores
        #keep previous scores in file
        elif int(prevPoints) > p:
            return

#play again function
def playAgain(name,points):
    choice = 1
    name = name
    #open highscore file
    infile = open('highscore.txt', 'r')
    #read lines from file store in line1 variable
    line1 = infile.readline()
    #if file is empty, add scores
    if line1 == '':
        #open file to write
        infile = open('highscore.txt', 'w')
        infile.write(name+',')
        infile.write(str(points))
        #close file
        infile.close()

        #if the file is not empty, read file
    if line1 != '':
        infile = open('highscore.txt', 'r')
        line1 = infile.readline()
        #split lines from file
        prevName,prevPoints = line1.split(',')

        #if previous points are less than current
        #replace previous points with current points
        if int(prevPoints) < points:
            newScore = points
            outfile = open('highscore.txt', 'w')
            outfile.write(str(name+','))
            outfile.write(str(newScore))
            outfile.close()
        #if previous points are greater than current points
        #keep previous points in file
        elif int(prevPoints) > points:
            return
    choice +=1

#questions function
def questions(n,c):
    points = 0
    name = n
    count = 0
    choice = c

    while choice >= 1:
        points = 0
        print('question 1:')
        print('Muhammad Ali was associated with which sport?')
        print('1) Baseball')
        print('2) Golf')
        print('3) Boxing')
        print('4) Water Polo')
        userChoice = eval(input('Enter a number 1 - 4: '))
        while userChoice < 1 or userChoice > 4:
            if userChoice < 1 or userChoice > 4:
                userChoice = eval(input('Enter a number 1 - 4: '))
        if userChoice == 3:
            print('Correct!')
            points += 100;
            print('+',points)
        elif userChoice != 3:
            print('Incorrect.')

        print('question 2:')
        print('Which fictional city is the home of Batman?')
        print('1) New York City')
        print('2) Bat City')
        print('3) Miami')
        print('4) Gotham City')
        userChoice = eval(input())
        while userChoice < 1 or userChoice > 4:
            if userChoice < 1 or userChoice > 4:
                userChoice = eval(input('Enter a number 1 - 4: '))
        if userChoice == 4:
            print('Correct!')
            points += 200;
            print('+',points)
        elif userChoice !=4:
            print('Incorrect.')

        print('question 3:')
        print('How many sides does an octagon have?')
        print('1) 2')
        print('2) 4')
        print('3) 6')
        print('4) 8')
        userChoice = eval(input('Enter a number 1 - 4: '))
        while userChoice < 1 or userChoice > 4:
            if userChoice < 1 or userChoice > 4:
                userChoice = eval(input('Enter a number 1 - 4:'))
        if userChoice == 4:
            print('Correct!')
            points += 500 ;
            print('+',points)
        elif userChoice !=4:
            print('Incorrect.')

        print('question 4:')
        print('Mount Everest is found in which mountain range?')
        print('1) Rocky Mountains')
        print('2) Himalayas')
        print('3) Twin Peaks')
        print('4) Wasatch Range')
        userChoice = eval(input('Enter a number 1 - 4: '))

        while userChoice < 1 or userChoice > 4:
            if userChoice < 1 or userChoice > 4:
                userChoice = eval(input('Enter a number 1 - 4:'))
        if userChoice == 2:
            print('Correct!')
            points += 1000;
            print('+',points)
        elif userChoice !=2:
            print('Incorrect.')

        print('question 5:')
        print('Approximately, how far away is the Eatch from the Sun?')
        print('1) 92,960,000 miles')
        print('2) 699,859 miles')
        print('3) 95,500,3400 miles')
        print('4) 1 light year')
        userChoice = eval(input('Enter a number 1 - 4: '))

        while userChoice < 1 or userChoice > 4:
            if userChoice < 1 or userChoice > 4:
                userChoice = eval(input('Enter a number 1 - 4: '))
        if userChoice == 1:
            print('Correct!')
            points += 2000;
            print('+',points)
        elif userChoice !=1:
            print('Incorrect.')

        totalScore = 0
        totalScore += points
        print('Your total Score is: '+str(totalScore))
        print('Would you like to play again?')
        print('1) Yes')
        print('2) No')

        userChoice2 = eval(input('Enter 1 - 2: '))
        while userChoice2 < 1 or userChoice > 2:
            if userChoice2 < 1 or userChoice > 2:
                userChoice2 = eval(input('Choose a number 1 -2: '))

        if userChoice2 == 1:
            playAgain(name,points)

        if userChoice2 == 2:
            choice = 0
            print('Thanks for playing!')
            count +=1
            endGame(name,points,count)

def menu():
    print('')
print( "Welcome to Who Wants To Be A Millionaire! ")
print("Please choose from the following menu:\n")
print('Enter your name: ')
name = input()
print(' 1) Play\n 2) Quit');
menuChoice = eval(input('Enter number 1 or 2: '))
while menuChoice < 1 or menuChoice > 2:
    if menuChoice < 1 or menuChoice > 2:
        menuChoice = eval(input('Enter numbers 1 or 2 to continue: '))

if menuChoice == 1:
    choice +=1
    questions(name,choice)
if menuChoice == 2:
    print('Goodbye!')

#define main function
def main():
    menu()


	
	
