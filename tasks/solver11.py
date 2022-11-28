class Solver11:
    FILE_NAME = "inputs/26-72.txt"

    def solve(self) -> str:
        with open(self.FILE_NAME) as F:
            N, M, K = map(int, F.readline().split())
            filled = []
            for i in range(K):
                r, c = map(int, F.readline().split())
                filled.append((r, c))

        count = maxRow = maxCount = 0
        for r in range(1, M + 1):
            row = [0] * N
            for c in [cm for rw, cm in filled if rw == r]:
                row[c - 1] = 1
            posCount = 0
            for startPos in range(N - 3):
                if row[startPos] == row[startPos + 1] == \
                        row[startPos + 2] == row[startPos + 3] == 0:
                    # print( '+', startPos )
                    posCount += 1
            count += posCount
            if posCount > maxCount:
                maxRow, maxCount = r, posCount

        return f'{count} {maxRow}'
