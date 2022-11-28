class Solver3:
    FILE_NAME = "inputs/26-k2.txt"

    def solve(self) -> str:
        with open(self.FILE_NAME) as F:
            n, k = map(int, F.readline().split())

            a = []
            for i in range(n):
                izm = F.readline()
                a.append(int(izm))

            a.sort()
            a = a[k:-k]
            summa = sum(a)
            sred = int(summa / len(a))
        return f'{a[-1]} {sred}'
