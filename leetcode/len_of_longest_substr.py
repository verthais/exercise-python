class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rhs = 0
        out = 0
        sub = ''

        while rhs < len(s):
            if s[rhs] not in sub:
                sub+=s[rhs]
                out = max(out, len(sub))
            else:
                sub = sub[sub.index(s[rhs]) + 1:] + s[rhs]
            rhs += 1
        
        return out

def eq(exp, res):
    assert exp == res, f'Got: {res}, expected: {exp}'

def main():
    input = "abcabdef"
    exp = 6

    s = Solution()

    eq(exp, s.lengthOfLongestSubstring(input))
    print('Success')

if __name__ == '__main__':
    main()