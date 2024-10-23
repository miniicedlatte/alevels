#non-recursive
def insertionSort():
    arr = [3,4,5,6,7,8,9]

    for i in range(len(arr)):
        for j in range(i-1):
            if arr[j]<arr[i]:
                temp=arr[i]
                for k in range(i,j,-1):
                    arr[k]=arr[k-1]
                arr[j]=temp
                break
    return arr
print(insertionSort())
