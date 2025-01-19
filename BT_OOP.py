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
