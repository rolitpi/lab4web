class Solver6:
    FILE_NAME = "inputs/26-47.txt"

    def solve(self) -> str:
        with open(self.FILE_NAME) as F:
            N = int(F.readline())
            data = [int(s) for s in F]

        data.sort()

        averages = []
        for i in range(N - 1):
            for j in range(i + 1, N):
                averages.append((data[i] + data[j]) / 2)
        averages.sort()

        count, ma = 0, 0
        k = 0
        for avg in averages:
            while k < N and data[k] < avg:
                k += 1
            if k > 0 and k % 3 == 0:  # в примере к задаче указано почему-то "кратно тройке",
                # хотя в самой задаче написано "кратно 100"
                count += 1
                ma = max(ma, k)

        return f'{count} {ma}'
