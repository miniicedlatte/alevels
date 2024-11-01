#part a
'''
DECLARE QueueArray : ARRAY[0:9] OF STRING
DECLARE head, tail, numItems : INTEGER
'''
QueueArray = [" " for i in range(10)]
HeadPointer = 0
TailPointer = 0
NumberItems = 0

#part b [head deletes,tail adds]
def Enqueue(DataToAdd):
    global HeadPointer, TailPointer, NumberItems
    if NumberItems == 10:
        return False
    QueueArray[TailPointer] = DataToAdd
    if TailPointer >= 9:
        TailPointer=0
    else:
        TailPointer += 1
    NumberItems += 1
    return True

#part c
def Dequeue():
    global HeadPointer, TailPointer, NumberItems
    if NumberItems == 0:
        return False
    else:
        item = QueueArray[HeadPointer]
        HeadPointer += 1
        NumberItems -= 1
        if HeadPointer == TailPointer:
            HeadPointer = 0
            TailPointer = 0
        return item

#part d
for _ in range(11):
    value = input("input string : ")
    success = Enqueue(value)
    if success:
        print("addition successful")
    else :
        print("addition unsuccessful")

print(Dequeue())
print(Dequeue())


