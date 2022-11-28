class Solver14:
    FILE_NAME = "inputs/26-80.txt"

    def solve(self) -> str:
        with open(self.FILE_NAME) as F:
            N = int(F.readline())
            data = {}
            for i in range(N):
                row, pos = map(int, F.readline().split())
                data[row] = data.get(row, []) + [pos]

        maxCount, maxRow = -1, None
        totalCount = 0
        for r in data:
            row = sorted(data[r])
            count = 0
            for i in range(len(row)):
                pos = row[i]
                if not (pos - 2 in row or pos - 1 in row or pos + 1 in row or pos + 2 in row):
                    count += 1
                    row += [pos + 2]

            if count > maxCount:
                maxCount = count
                maxRow = r
            totalCount += count

        return f'{totalCount} {maxRow}'
