class Solver9:
    FILE_NAME = "inputs/26-59.txt"

    def solve(self) -> str:
        with open(self.FILE_NAME) as F:
            N = int(F.readline())
            data = {}
            for i in range(N):
                row, seat = map(int, F.readline().split())
                data[row] = data.get(row, []) + [seat]

        for row, seats in sorted(data.items(), reverse=True):
            seats.sort()
            done = False
            for i in range(len(seats) - 1):
                if seats[i + 1] - seats[i] == 3:
                    return f'{row} {seats[i] + 1}'
