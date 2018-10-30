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

    # print("Question:")
    # print(qList[0])
    # print("")
    # print("Answer Choices:")
    # print(qList[1])
    # print(qList[2])
    # print(qList[3])
    # print(qList[4])
    #
    # print("")
    # x = input()
    #
    # if x == qList[5]:
    #     print("Good Job")
    # else:
    #     print("You Suck")



main()