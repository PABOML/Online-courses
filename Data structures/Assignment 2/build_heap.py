# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []
    #print('data=',self._data)

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    #print('data=',self._data)
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

    
  def SiftDown(self):
    self.maxIndex = self.i
    l = 2*self.i + 1 # left Child
    r = 2*self.i + 2 # right Child
    if l <= (len(self._data)-1) and self._data[l] < self._data[self.maxIndex]:
       self.maxIndex = l
    if r <= (len(self._data)-1) and self._data[r] < self._data[self.maxIndex]:
       self.maxIndex = r
    if self.i != self.maxIndex:
       self._data[self.i], self._data[self.maxIndex] = self._data[self.maxIndex], self._data[self.i]
       self._swaps.append((self.i, self.maxIndex))
       self.i = self.maxIndex
       self.SiftDown()    

  def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    '''
    for i in range(len(self._data)):
      for j in range(i + 1, len(self._data)):
        if self._data[i] > self._data[j]:
          self._swaps.append((i, j))
          self._data[i], self._data[j] = self._data[j], self._data[i]
    ''' 
#.....................Pauls code......................................
    for self.i in range( (len(self._data) // 2), -1, -1):
        self.SiftDown()
        
  

#.....................................................................
    
    
  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
