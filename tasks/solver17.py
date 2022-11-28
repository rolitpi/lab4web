class Solver17:
    FILE_NAME = "inputs/26-90.txt"

    def solve(self) -> str:
        with open(self.FILE_NAME) as F:
            N = int(F.readline())
            data = [int(F.readline()) for i in range(N)]

        data.sort()

        S = sum(data)
        D = 4
        Nact = N // D

        return f'{S - sum(data[-Nact:]) // 2} {S - sum(data[:Nact]) // 2}'
