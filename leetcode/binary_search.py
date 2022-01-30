def binary_search(collection, lhs, rhs, value):
    if rhs > lhs:
        mid = lhs + (rhs - lhs) // 2

        if collection[mid] == value:
            return mid

        if collection[mid] > value:
            return binary_search(collection, lhs, mid-1, value)

        return binary_search(collection, mid+1, rhs, value)
    return -1


def eq(exp, val):
    assert exp == val, f'Expected: {exp}, got value {val}'


def main():
    tests = [
        (0, 5, [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),
        (8, 13, [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),
        (8, 9, [1,2,3,4,5,6,7,8,9]),
    ]

    for expected, value, collection in tests:
        eq(expected, binary_search(collection, 0, len(collection), value))


if __name__ == '__main__':
    main()
    print('success')