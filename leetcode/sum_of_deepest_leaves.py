class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        queue = [root]
        sum = 0

        while queue:
            ls = len(queue)
            sum = 0
            for _ in range(ls):
                if queue[0].right is not None:
                    queue.append(queue[0].right)
                
                if queue[0].left is not None:
                    queue.append(queue[0].left)
                
                sum += queue[0].val
                del queue[0]
        return sum


def eq(exp, res):
    assert exp == res, (exp, res)

def main():
    input = [1,2,3,4,5,None,6,7,None,None,None,None,8]
    input2 = [6,7,8,2,7,1,3,9,None,1,4,None,None,None,5]

    s = Solution()

    eq(15, s.deepestLeavesSum(input))
    eq(19, s.deepestLeavesSum(input2))

if __name__ == '__main__':
    main()