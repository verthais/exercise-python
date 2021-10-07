'''
** Instructions:
**
** Given a forest ( one or more disconnected trees ), find the root of largest tree
** and return its Id, If there are multiple such roots, retur the smallest Id of them.
**
** Complete the largest Tree function in the editor below
** It has one parameter, immediateParent, which is a map containing key-value pair indicating
** child -> parent relationship. The key is child and value is the corresponding immediate parent.
** Constraints:
**   - Child cannot have more then one immediate parent.
**   - Parent can have more than one immediate child.
**   - The given key-value pair forms a well-formed forest ( a tree of n nodes will have n-1 edges )
**
** Example:
**
** Input:
**   { { 1 - > 2 }, { 3 -> 4 } }
**
** Expected output: 2
** Explenation: There are two trees one having a root of 2 and another having a root of 4.
**              Both tree have size 2. The smaller number between 4 and 2 is 2, hence 2.
'''


def find_max_val_min_root(data):
    max_k, max_v = 0, 0

    for k, v in data.items():
        if v > max_v:
            max_v = v
            max_k = k
        elif v == max_v:
            if max_k > k:
                max_k = k

    return max_k


def bfs(root, out, data, queue):
    while queue:
        child = queue[0]
        del queue[0]

        for next_of_keen, parent in data.items():
            if child == parent:
                queue.append(next_of_keen)
                out[root] += 1


def dfs(root, out, data, stack):
    while stack:
        child = stack[-1]
        del stack[-1]

        for next_of_keen, parent in data.items():
            if child == parent:
                stack.append(next_of_keen)
                out[root] += 1


def solution(data, search_order):
    roots = set(data.values()) - set(data.keys())
    out = dict.fromkeys(roots, 0)

    while roots:
        root = roots.pop()
        children = [
            child for child, parent in data.items()
            if root == parent
        ]

        out[root] += len(children)
        search_order(root, out, data, children)

    return find_max_val_min_root(out)


def eq(exp, res):
    assert exp == res, f'exp: {exp}, res: {res}'


def main():
    input = [
        (
            {1:2, 3:4},
            2
        ),
        (
            {1:2, 2:5, 3:4},
            5
        ),
        (
            {},
            0
        ),
        (
            {2:4, 1:4, 3:4, 9:3, 2:11, 11:5},
            4
        ),
        (
            {1:2, 3:2, 4:2, 6:5, 7:5, 8:5},
            2
        )
    ]

    for data, exp in input:
        eq(exp, solution(data, bfs))

    for data, exp in input:
        eq(exp, solution(data, dfs))

    print('success')

if __name__ == '__main__':
    main()