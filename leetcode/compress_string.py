"""
    Instruction for the candidate.
    1) Given a string compres the repeating letters following each letter
       with number of repetition in the output string
    2) Example:
       'a'    -> 'a1'
       'aaa'  -> 'a3'
       'aabb' -> 'a2b2'
       ''     -> ''
"""

def rle(test_string):
    result = ''

    if not test_string:
        return result
    
    current = test_string[0]
    count = 1

    for c in test_string[1:]:
        if c == current:
            count += 1
        else:
            result += current
            result += str(count)
            current = c
            count = 1
    
    result += current
    result += str(count)

    return result

def eq(exp, res):
    assert exp == res, f'expected: {exp} - result: {res}'

def main():
    input = ['',  'a', 'aaabbc', 'aaabbbccc',        'abcdefg']
    expect= ['', 'a1', 'a3b2c1',    'a3b3c3', 'a1b1c1d1e1f1g1']

    for i, o in zip(input, expect):
        eq(o, rle(i))
    
    print('success')

if __name__ == '__main__':
    main()