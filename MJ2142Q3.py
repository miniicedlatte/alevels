#class declaration
class TreasureChest():

    # PRIVATE question
    # PRIVATE answer
    # PRIVATE points

    def __init__(self, q, a, p):
        self.__question = q
        self.__answer = a
        self.__points = p

    def getQuestion(self):
        return self.__question

    def checkAnswer(self, ans):
        if self.__answer == ans:
            return True
        else:
            return False

    def getPoints(self,num):
        if num == 1:
            return self.__points
        elif num == 2:
            return int(self.__points/2)
        elif num == 3 or num == 4:
            return int(self.__points/4)
        else:
            return 0

# readdata
def readData():
    global arrayTreasure
    try:
        file = open("TreasureChestData.txt", "r")
        arrayTreasure = [TreasureChest("","", 0) for _ in range(5)]

        for i in range(5):
            Question = (file.readline()).strip()
            Answer = (file.readline()).strip()
            Points = (file.readline()).strip()
            element = TreasureChest(Question, Answer, int(Points))
            arrayTreasure[i] = element
        file.close()

    except FileNotFoundError:
        print("File could not be found")

# main program
readData()
q = int(input("Enter the treasure chest number (between 1 - 5) : "))
if 0 < q < 6:
    count = 1
    while True:
        question = arrayTreasure[q-1].getQuestion()
        a = input(f"{question} : ")
        if arrayTreasure[q-1].checkAnswer(a):
            p = arrayTreasure[q-1].getPoints(count)
            print(p)
            break
        else:
            count = count + 1


