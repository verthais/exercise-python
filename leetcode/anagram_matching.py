class Solver():
    def _is_anagram(self, word: str, match: str):
        m = list(match)
        for c in word:
            if c not in m:
                return False
            del m[m.index(c)]
        return True

    def find_anagrams(self, word: str, data: list) -> list:
        r_value = [word]
        idx = 0
        while idx < len(data):
            if self._is_anagram(word, data[idx]):
                r_value.append(data[idx])
                del data[idx]
            idx += 1

        return r_value

    def solve(self, data):
        r_value = []
        while data:
            word = data[0]
            del data[0]
            r_value.append(self.find_anagrams(word, data))

        return r_value

def eq(exp, res):
    assert exp == res, res

def main():
    input = ['cat', 'dog', 'god', 'pot', 'top',]

    exp = [
        ['cat'],
        ['dog', 'god'],
        ['pot', 'top'],
    ]

    s = Solver()
    eq(exp, s.solve(input))
    print('Success')

if __name__ == "__main__":
    main()
