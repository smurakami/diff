# coding: utf-8
import sys

class Diff:
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def solve(self):
    self.result = None
    self.createTable()
    self.selectMatches()
    self.connectPath()
    self.genResult()
    return self.result

  def createTable(self):
    self.table = [[x == y for y in self.b] for x in self.a]

  def selectMatches(self):
    self.matches = [ (i, j)
      for i in range(len(self.table))
      for j in range(len(self.table[i]))
      if self.table[i][j]]

    self.max_path = []
    self.path = []

    self.search((-1, -1)) # 左上から探索
    # print self.max_path

  def search(self, pos):
    def isReachable(pos, match):
      return match[0] > pos[0] and match[1] > pos[1]

    if pos != (-1, -1): self.path.append(pos)
    is_term = True
    for match in self.matches:
      if isReachable(pos, match):
        is_term = False
        next_pos = match
        self.search(next_pos)

    if is_term: # 終端の場合
      if len(self.path) > len(self.max_path):
        self.max_path = list(self.path) # 最良経路の更新
    if pos != (-1, -1): self.path.pop()

  def connectPath(self):
    # self.path = [(0, 0)]
    self.path = []
    prev = (0, 0)
    for pos in self.max_path:
      p = prev
      while p[0] < pos[0]:
        p = (p[0] + 1, p[1])
        self.path.append(p)
      while p[1] < pos[1]:
        p = (p[0], p[1] + 1)
        self.path.append(p)
      p = (p[0] + 1, p[1] + 1)
      self.path.append(p)
      prev = p
    p = prev
    while p[0] < len(self.table):
      p = (p[0] + 1, p[1])
      self.path.append(p)
    while p[1] < len(self.table[0]):
      p = (p[0], p[1] + 1)
      self.path.append(p)
    # print self.path

  def genResult(self):
    prev = (0, 0)
    i_a = 0
    i_b = 0
    self.result = []
    for pos in self.path:
      if pos == (0, 0): continue
      if pos[1] == prev[1]: # 縦への移動 : a の -
        self.result.append((self.a[i_a], '-'))
        i_a += 1
      elif pos[0] == prev[0]: # 横への移動 : b の +
        self.result.append((self.b[i_b], '+'))
        i_b += 1
      else: # 斜めへの移動
        self.result.append((self.a[i_a], ' '))
        i_a += 1
        i_b += 1
      prev = pos
      # print self.result

  def printResult(self):
    for line, sign in self.result:
      print sign, line,

def diff(filename_a, filename_b):
  a = []
  with open(filename_a) as f:
    for line in f:
      a.append(line)

  b = []
  with open(filename_b) as f:
    for line in f:
      b.append(line)

  # a = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
  # b = ['a', 'b', 'x', 'c', 'y', 'e', 'g']
  solver = Diff(a, b)
  result = solver.solve()
  solver.printResult()

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print "Usage: python %s fileA fileB" % sys.argv[0]
    quit()
  diff(sys.argv[1], sys.argv[2])

