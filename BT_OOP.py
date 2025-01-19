#node class definition
class Node():
    #PRIVATE LeftPointer
    #PRIVATE RightPointer
    #PRIVATE Data
    def __init__(self, d):
        self.__LeftPointer = -1
        self.__Data = d
        self.__RightPointer = -1

    def GetLeft(self):
        return self.__LeftPointer

    def GetRight(self):
        return self.__RightPointer

    def GetData(self):
        return self.__Data

    def SetLeftPointer (self, Lp):
        self.__LeftPointer = Lp

    def SetRightPointer(self, rp):
        self.__RightPointer = rp

    def SetData(self, d):
        self.__Data = d

# treeclass definition
class TreeClass():
    def __init__(self):
        self.__Tree = [Node(-1) for _ in range(20)]
        self.__FirstNode = -1
        self.__NumberNodes = 0
# something
    def InsertNode(self, NewNode) :
        if self.__NumberNodes == 0:
            self.__Tree[self.__NumberNodes] = NewNode
            self.__NumberNodes += 1
            self.__FirstNode = 0
        else:
            self.__Tree[self.__NumberNodes] = NewNode
            current = self.__FirstNode
            self.__NumberNodes += 1
            direction = ""
            while current != -1:
                previous = current
                if NewNode.GetData() > self.__Tree[current].GetData():
                    current = self.__Tree[current].GetRight()
                    direction = "R"
                elif NewNode.GetData() < self.__Tree[current].GetData():
                    current = self.__Tree[current].GetLeft()
                    direction = "L"

            if direction == "R":
                self.__Tree[previous].SetRightPointer(self.__NumberNodes - 1)
            elif direction == "L":
                self.__Tree[previous].SetLeftPointer(self.__NumberNodes - 1)

    def OutputTree(self):
        if self.__NumberNodes == 0:
            print("No nodes")
        else:
            for i in range(self.__NumberNodes):
                node = self.__Tree[i]
                print(f"{node.GetLeft()} {node.GetData()} {node.GetRight()}")


TheTree = TreeClass()
dataval = [10,11,5,1,20,7,15]
for val in dataval:
    new = Node(val)
    TheTree.InsertNode(new)
TheTree.OutputTree()
