from bisect import bisect_left


class Solver7:
    FILE_NAME = "inputs/26-50.txt"

    def solve(self) -> str:

        def isSmaller(l, elem):
            index1 = index2 = bisect_left(l, elem)
            if elem < l[index2]: index2 -= 1
            return len(l) // 2 <= index1 and index2 < len(l) // 4 * 3

        f = open(self.FILE_NAME)
        n = int(f.readline())
        a = sorted([int(s) for s in f])

        count, m = 0, float('inf')
        for i in a:
            for j in a:
                if i < j and (i + j) % 2 == 0 and isSmaller(a, (i + j) // 2):
                    count += 1
                    m = min(m, (i + j) // 2)

        return f'{count} {m}'
