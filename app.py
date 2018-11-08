import random
import csv
import codecs
import time
from threading import Thread


class compPlayer():
    def __init__(self, name, maxPoints):
        self.points = 0
        self.name = name
        self.maxPoints = maxPoints

    #we will make this randomly generated by questions later instead of total points so it would be like the bot is playing
    def totalPoints(self):
        self.points = random.randint(0,self.maxPoints)
        return self.points


#adds words individually into a list
def makeList(qList):
    header = 0
    # with open('Questions.csv', 'r') as csvfile:
    with codecs.open('Questions.csv', "r", encoding='utf-8', errors='ignore') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if header == 0:
                header += 1
            else:
                qList.append(row)
    csvfile.close()
    return qList

def selectDifficulty():
    difficulty = str(input("What difficulty of bot do you want to play against? (1 - easy, 2 - medium, 3 hard): "))
    while str(difficulty) != '1' and str(difficulty) != '2' and str(difficulty) != '3':
        difficulty = str(input("Please input a number that was specified previously! (1 - easy, 2 - medium, 3 hard): "))
    print()
    difficulty = int(difficulty)
    levels = ['easy', 'medium', 'hard']
    print("Okay, you will play against a bot with a difficulty level of " + str(levels[difficulty - 1]) + ".")
    return difficulty

def selectNumQuestions():
   #numQuestions = str(input("How many questions do you want (1-Infinite)? "))
    numQuestions = str(input("How many questions do you want (1-30)? "))
    flag = False
    while not flag:
        try:
            numQuestions = int(numQuestions)
            if numQuestions < 1 or numQuestions > 30:
                numQuestions = str(input("Please enter a number within the range of 1-30! "))
            else:
                flag = True
        except:
            numQuestions = str(input("Please enter a number within the range of 1-30! "))

    print()
    print("Okay, you will have " + str(numQuestions) + " question(s).")
    print()
    return int(numQuestions)

def askQuestion(q, qList):
    print("Question " + str(q + 1) + '!')
    print(qList[q][0])
    print("")
    print("Answer Choices:")
    print('A) ' + qList[q][1])
    print('B) ' + qList[q][2])
    print('C) ' + qList[q][3])
    print('D) ' + qList[q][4])
    print()
    return ""

def answerQuestion(q, qList, points):
    answer = qList[q][5]
    ansLetter = answer[0].lower()
    ansActual = answer[3:].lower()
    x = str(input("Your answer: "))
    if x.lower() == ansLetter or x.lower() == ansActual:
        points[0] += 1
        print("Correct! You now have " + str(points[0]) + " point(s).\n")
    #     return False
    # elif x.lower() == "stop":
    #     print("Game Stopped")
    #     return True
    else:
        points[1] += 1
        print("Incorrect! The bot is correct with answer: " + answer + ". You still have " +
              str(points[0]) + " point(s).\n")
        # return False

def calculateScores(points):
    print("Your score is: " + str(points[0]))
    # for bots in range (numBots):
    #     print(bot.name + " score is: " + str(bot.totalPoints()))
    print("The bot's score is: " + str(points[1]))
    if points[0] > points[1]:
        print("Congratulations! You win!")
        return "win"
    elif points[0] == points[1]:
        print("It's a tie! Better luck next time!")
        return "tie"
    else:
        print("You lose! Try again!")
        return "lose"

def main():
    # file = open("Questions.csv", "r") #reading file
    # quiz = file.read()
    # qList = []
    # qList = makeList(quiz)
    # print(qList)
    qList = []
    makeList(qList)

    print('Welcome to our trivia game! Test your knowledge about our CS329E class!')
    print('Here are our rules:')
    print('You will be playing against a bot of a chosen difficulty. The bot has a certain amount of time to answer '
          'the question. You will have to beat that bot within that time by choosing the correct multiple choice '
          'answer!')
    print()

    numQuestions = selectNumQuestions()

    #creating the different computers
    # numBots = int(input("How many players do you want to play against (0-3)?"))
    # print("Okay you will be playing against " + str(numBots) + " computer(s)")
    # for bots in range(numBots):
    #     maxPoints = numQuestions
    #     bot = compPlayer("Computer" + str(bots+1), maxPoints)
    #     print(bot.name)

    difficulty = selectDifficulty()

    print()
    input("Press any key to start!")
    print()

    #asking questions
    stopper = False
    points = [0, 0]
    q = 0
    # while stopper == False and q < numQuestions:
    for q in range(numQuestions):
        askQuestion(q, qList)
        answerQuestion(q, qList, points)
        # stopper = answerQuestion(q, qList, points)
        # q += 1
        #grading the question and giving out points
        # if x == qList[q]:
        #     playerPoints += 1
        #     print("Good Job, you have " + str(playerPoints) + " points\n")
        # else:
        #     print("You Suck, you have " +str(playerPoints) +" points\n")

    input("Game finished. Press any key to see final score.")
    calculateScores(points)


if __name__ == '__main__':
    main()
