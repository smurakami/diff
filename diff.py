# coding: utf-8
class Diff:
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def solve(self):
    self.result = None
    self.createTable()
    self.selectMatches()
    self.connectPath()
    return self.result

  def createTable(self):
    pass

  def selectMatches(self):
    pass

  def connectPath(self):
    pass


def diff(filename_a, filename_b):
  a = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
  b = ['a', 'b', 'x', 'c', 'y', 'e', 'g']
  solver = Diff(a, b)
  result = solver.solve()
  print result

if __name__ == "__main__":
  diff(None, None)

