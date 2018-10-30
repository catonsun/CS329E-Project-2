def makeList(file): #adds words individually into a list
    questions = []
    questions = file.split()

    return (questions)

def main():
    file = open("Questions.txt", "r") #reading file
    quiz = file.read()
    qList = []
    qList = makeList(quiz)
    print(qList)