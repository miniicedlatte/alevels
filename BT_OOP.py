#node class definition
class Node():
#PRIVATE LeftPointer
#PRIVATE RightPointer
#PRIVATE Data
def __init__（self,d）：
  self.__LeftPointer = -1
  self.__Data = d
  self.__RightPointer = -1
def GetLeft(self) :
  return self.__LeftPointer
def GetRight(self):
  return self.__RightPointer
def GetData(self) :
  return self.__Data
def SetLeftPointer (self, Lp):
  self.__LeftPointer = Lp
def SetRightPointer(self, rp):
  self.__RightPointer = rp

def SetData(self, d):
self.-_Data = d

# treeclass definition
Eclass TreeClass():
def -_init__(self):
self.__Tree = [Node(-1) for - in range (20)]
self.-FirstNode = -1
self.-_NumberNodes = 0
# something
def
InsertNode(self, NewNode) :
if
self.__NumberNodes = 0:
self.-_Tree[self.-_NumberNodes] = NewNode
self.-_NumberNodes += 1
self.-_FirstNode = 0
else:
self.-_Tree[self. __NumberNodes] = NewNode
current = self.-_FirstNode

while current != -1:
previous = current

if NewNode._Data > self.-_Tree[current] .GetData():
current = self.__Tree[current].Getright)

direction = "R"
if NewNode.-_Data < self.-_Tree [current] GetData():
current = self.__Tree[current] .GetLeft
