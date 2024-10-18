'''
ArrayLength <- 10
FOR X <- 0 TO ArrayLength - 1
    FOR Y <- 0 TO ArrayLength - 2
        FOR Z <- 0 TO ArrayLength - Y - 2
            IF ArrayData[X, Z] > ArrayData[X, Z + 1] THEN
                TempValue <- ArrayData[X, Z]
                ArrayData[X, Z] <- ArrayData[X, Z+1]
                ArrayData[X, Z + 1] <- TempValue
            ENDIF
        NEXT Z
    NEXT Y
NEXT X
'''
import random as r

def printArr(array): #part c (print array)
    for g in array:
        print (g)

arr = [[r.randint(1,100) for h in range(10)] for l in range(10)] #part a

printArr(arr) #part c (call before)
print() #part c (seperator)

# part b
arrLen = 10
for x in range(arrLen):
    for y in range(arrLen-1):
        for z in range(arrLen - y -1):
            if arr[x][z] > arr[x][z+1] :
                arr[x][z], arr[x][z+1] = arr[x][z+1], arr[x][z]

printArr(arr) #part c (call after)
