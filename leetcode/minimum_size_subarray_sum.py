
class Solution():
    def solve(self, target, nums):
        min_len = 10e5 + 1
        tmp = 0
        l_idx, r_idx = 0, 0
        
        while r_idx < len(nums):
            tmp += nums[r_idx]
            r_idx += 1
            while tmp >= target:
                min_len = min(min_len, r_idx - l_idx)
                tmp -= nums[l_idx]
                l_idx += 1

        return min_len if min_len < 10e5+1 else 0

def eq(exp, res):
    assert exp == res, res

def main():
    input = [7, [2,3,1,2,4,3]]
    input2 = [11, [1,1,1,1,1,1,1,1]]
    input3 = [4, [1,4,4]]
    input4 = [11, [1,2,3,4,5]]
    input5 = [15, [1,2,3,4,5]]

    s = Solution()

    eq(2, s.solve(*input))
    eq(0, s.solve(*input2))
    eq(1, s.solve(*input3))
    eq(3, s.solve(*input4))
    eq(5, s.solve(*input5))
    print('Success')

if __name__ == '__main__':
    main()