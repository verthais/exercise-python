
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def add(self,value):
        if self.next is None:
            self.next = ListNode(value)
        else:
            self.next.add(value)
    
    def __eq__(self, o: object) -> bool:
        if o is None:
            return False

        if self.val != o.val:
            return False
        
        if self.next != o.next:
            return False
        
        return True

    def __str__(self):
        out = f'{{ val: {self.val} }} -> '
        return out + str(self.next)



class List:
    def __init__(self):
        self.root = None
        self.end = None

    @classmethod
    def create(cls, *args):
        list = List()
        for e in args:
            list.add(e)

        return list.root

    def add(self, value):
        if self.root is None:
            self.root = ListNode(value)
            self.end = self.root
        else:
            self.end.add(value)
            self.end = self.end.next


def step(node):
    if node is not None:
        val = node.val
        node = node.next
        return node, val
    else:
        return None, 0


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        out = List()
        co = 0

        while l1 is not None or l2 is not None:
            l1, lhs = step(l1)
            l2, rhs = step(l2)
            val = co + lhs + rhs
            co = val // 10
            out.add(val%10)

        if co != 0:
            out.add(co)

        return out.root

def eq(exp, res):
    assert exp == res, res

def main():
    input = [List.create(2, 4, 3), List.create(5, 6, 4)]
    input2 = [List.create(9,9,9,9,9,9,9), List.create(9,9,9,9)]
    input3 = [List.create(0,0,0), List.create(0,0,0)]

    exp = List.create(7,0,8)
    exp2 = List.create(8,9,9,9,0,0,0,1)
    exp3 = List.create(0,0,0)

    s = Solution()

    eq(exp, s.addTwoNumbers(*input))
    eq(exp2, s.addTwoNumbers(*input2))
    eq(exp3, s.addTwoNumbers(*input3))
    print('Success')

if __name__ == '__main__':
    main()