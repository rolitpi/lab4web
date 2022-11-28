class Solver5:
    FILE_NAME = "inputs/26-j1.txt"

    def solve(self) -> str:
        with open(self.FILE_NAME) as F:
            n = int(F.readline())

            a = []
            for i in range(n):
                monet = F.readline()
                a.append(int(monet))

            k = 0
            for i in range(n - 1):
                for j in range(i + 1, n):
                    if a[i] + a[j] == 100:
                        k += 1
                        a[j] = 0
                        a[i] = 0
            print()
        return f'{k}'
