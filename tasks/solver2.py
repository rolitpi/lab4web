class Solver2:
    FILE_NAME = "inputs/26-k1.txt"

    def solve(self) -> str:
        with open(self.FILE_NAME) as F:
            nC, n = map(int, F.readline().split())

            a = []
            for i in range(nC):
                stroka = F.readline()
                a.append(int(stroka))

            a.sort(reverse=True)

            summa = 0
            for i in range(n):
                summa += a[i] * 0.2
        return f'{a[n]} {int(summa)}'
