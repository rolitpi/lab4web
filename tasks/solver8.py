class Solver8:
    FILE_NAME = "inputs/26-52.txt"

    def solve(self) -> str:
        F = open(self.FILE_NAME)
        N = int(F.readline())
        data = sorted([int(s) for s in F])

        gap = 100

        count, ma = 0, float('inf')
        for i in range(N - 1):
            for j in range(i + 1, i + gap + 2):
                if j < N and (data[i] + data[j]) % 10 == 0:
                    count += 1
                    ma = min(ma, (data[i] + data[j]) // 2)

        return f'{count} {ma}'
