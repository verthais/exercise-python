import re

class Solution:
    def is_the_match(self, s, p):
        s_idx, p_idx = 0, 0
        pattern = re.compile(p)
        result = pattern.fullmatch(s)
        
        if result is None:
            return False
        return True

    def isMatch(self, s: str, p: str) -> bool:
        self.s_idx, self.p_idx = 0, 0
        return self.is_the_match(s,p)


def eq(exp, res):
    assert exp == res, f'{exp} != {res}'

def main():
    input = ['aa', 'a']
    input2 = ['aa' , 'a*']
    input3 = ['ab', '.*']
    input4 = ['aab', 'c*a*b']
    input5 = ['mississippi', 'mis*is*p*.']

    s = Solution()

    eq(False,s.isMatch(*input))
    eq(True,s.isMatch(*input2))
    eq(True,s.isMatch(*input3))
    eq(True,s.isMatch(*input4))
    eq(False,s.isMatch(*input5))
    print('Success')

if __name__ == "__main__":
    main()