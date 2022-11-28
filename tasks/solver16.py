class Solver16:
    FILE_NAME = "inputs/26-89.txt"

    def solve(self) -> str:
        f = open(self.FILE_NAME)
        n = int(f.readline())
        a = [int(f.readline()) for i in range(n)]
        a = sorted(set(a), reverse=1)
        gift = [a[0]]
        for i in range(1, len(a)):
            if gift[-1] - a[i] >= 3:
                gift.append(a[i])

        return f'{len(gift)} {gift[-1]}'
