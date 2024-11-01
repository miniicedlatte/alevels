#part a
StackData = [" " for i in range(10)]
StackPointer = 0


#part b
def display():
    global StackPointer,StackData
    for i in StackData:
        print(i)
    print(StackPointer)

#part c [ store then increment ]
def Push(value):
    global StackPointer,StackData
    if StackPointer == len(StackData):
        return False
    else:
        StackData[StackPointer] = value
        StackPointer += 1
        return True


#part e
def Pop():
    global StackPointer, StackData
    if StackPointer == 0:
        return -1
    else:
        StackPointer -= 1
        item = StackData[StackPointer]
        StackData[StackPointer] = " "
        return item

#part d
for _ in range(11):
    num = int(input("input value : "))
    success = Push(num)
    if (success):
        print("Value added to stack successfully")
    else:
        print("Value cannot be added to stack as stack is full")
for i in StackData:
    print(i)
print()
Pop()
Pop()
print()
for i in StackData:
    print(i)

