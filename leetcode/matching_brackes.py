"""
 **You're working with an intern that keeps coming to you with JavaScript code that won't run because the braces, brackets, and parentheses are off. To save you both some time, you decide to write a braces/brackets/parentheses validator.**

Let's say:

- '(', '{', '[' are called "_openers_."
- ')', '}', ']' are called "_closers_."

Write an efficient function that tells us whether or not an input string's openers and closers are properly nested.

Fularczyk Tymoteusz
Bień Krystian



Examples:

- "{[]()}" should return **`1`**
- "{[(])}" should return **`0`**
- "{[}" should return **`0`**
"""
def solve(exp: str) -> bool:
    stack = []
    pairs = {
        '{' : '}',
        '[': ']',
        '(': ')',
    }

    for c in exp:
        if c in pairs.keys():
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            if pairs[stack[-1]] != c:
                return False            
            del stack[-1]

    if len(stack):
        return False
    
    return True

def eq(exp, res):
    if exp == res:
        print('success')
    else:
        print(f'test failed: exp: {exp} res: {res}')


def exercise():
    input = '{[]()}'
    input2 = '{[(])}'
    input3 = '{[}'
    input4 = ''
    input5 = '}()'
    
    eq(True,  solve(input))
    eq(False, solve(input2))
    eq(False, solve(input3))
    eq(True,  solve(input4))
    eq(False, solve(input5))
    

if __name__ == '__main__':
    exercise()