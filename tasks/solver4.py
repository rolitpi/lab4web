class Solver4:
    FILE_NAME = "inputs/26-k3.txt"

    def solve(self) -> str:
        with open(self.FILE_NAME) as F:
            n, k, m = map(int, F.readline().split())

            a = []
            for i in range(n):
                rez = F.readline()
                a.append(int(rez))

            a.sort(reverse=True)
        return f'{a[k + m - 1]} {a[k - 1]}'
