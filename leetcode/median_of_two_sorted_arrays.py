class Solution:
    def merge(self, lhs, rhs):
        r_value = []
        while lhs and rhs:
            if lhs[0] < rhs[0]:
                r_value.append(lhs[0])
                del lhs[0]
            else:
                r_value.append(rhs[0])
                del rhs[0]
            
        if lhs:
            r_value.extend(lhs)

        if rhs:
            r_value.extend(rhs)

        return r_value

    def findMedianSortedArrays(self, nums1, nums2) -> float:
        # merged = nums1 + nums2
        # merged.sort()
        merged = self.merge(nums1, nums2)
        l = len(merged)

        if l%2:
            return merged[l//2]
        else:
            a, b = merged[l//2], merged[l//2-1]
            return (a+b)/2

def eq(exp, res):
    assert exp == res, res

def main():
    input = [[1,3], [2]]
    input2 = [[1,2],[3,4]]
    input3 = [[0,0],[0,0]]
    input4 = [[],[1]]
    input5 = [[1],[]]

    s = Solution()
    eq(2.0,s.findMedianSortedArrays(*input))
    eq(2.5,s.findMedianSortedArrays(*input2))
    eq(0,s.findMedianSortedArrays(*input3))
    eq(1,s.findMedianSortedArrays(*input4))
    eq(1,s.findMedianSortedArrays(*input5))
    print('Success')

if __name__ == '__main__':
    main()