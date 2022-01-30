# On one of mine interview I got this question to traverse
# the tree from the most left node to most right node order
# obviously i failed to implement it in at the time...
# and I must say it's a little much for a 15min problem to be solve in C
#          E
#        /   \
#       D      I
#      /      / \
#     B      H   J
#   /  \    /     \
#  A    C  F       K
#           \       \
#             G      L
#
# solution: A -> B -> C -> D -> E -> F -> G -> H -> I -> J -> K


def tov(node):
  return  node.value if node is not None else 'None'


class Node():
  def __init__(self, value, lhs=None, rhs=None, prnt=None):
    self.value = value
    self.lhs: Node = lhs
    self.rhs: Node = rhs
    self.prnt: Node = prnt

  def __repr__(self) -> str:
    return f'Node(v:{self.value}, p:{tov(self.prnt)}, l:{tov(self.lhs)}, r:{(self.rhs)})'

  def __iter__(self):
    return NodeIterator(self)

  def is_root(self) -> bool:
    return self.prnt is None

  def is_right_child(self) -> bool:
    return not self.is_root() and self.prnt.rhs is self

  def has_left_child(self) -> bool:
    return self.lhs is not None

  def has_right_child(self) -> bool:
    return self.rhs is not None


class NodeIterator:
  def __init__(self, node: Node):
    self.node = node

  def __next__(self) -> Node:
    n = self.node

    if n.has_right_child():
      n = n.rhs
      while n.has_left_child():
        n = n.lhs

    elif n.is_right_child():
      if n.prnt.prnt:
        n = n.prnt.prnt

      while n.is_right_child():
        n = n.prnt

      if n.is_root():
        raise StopIteration

    else:
      n = n.prnt

    self.node = n
    return n


def eq(exp: str, res: str) -> None:
  assert exp == res, f'Exp: {exp} got Res: {res}'


def main():
  e = Node('E')
  d = Node('D', prnt=e)
  i = Node('I', prnt=e)
  e.lhs = d
  e.rhs = i

  j = Node('J', prnt=i)
  h = Node('H', prnt=i)
  i.lhs = h
  i.rhs = j

  k = Node('K', prnt=j)
  j.rhs = k

  l = Node('L', prnt=k)
  k.rhs = l

  f = Node('F', prnt=h)
  h.lhs = f
  g = Node('G', prnt=f)
  f.rhs = g

  b = Node('B', prnt=d)
  d.lhs = b

  a = Node('A', prnt=b)
  c = Node('C', prnt=b)
  b.lhs = a
  b.rhs = c
  expected = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']

  for node, exp in zip(a, expected):
    print(node)
    eq(exp, node.value)


if __name__ == '__main__':
  main()
  print('success')