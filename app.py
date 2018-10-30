def makeList(file): #adds words individually into a list
    questions = []
    questions = file.splitlines()

    return (questions)

def main():
    numQuestions = 0
    file = open("Questions.txt", "r") #reading file
    quiz = file.read()
    qList = []
    qList = makeList(quiz)

    numQuestions = input("How many questions do you want (5-30)?")
    print(numQuestions)


main()