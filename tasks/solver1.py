class Solver1:
    FILE_NAME = "inputs/26.txt"

    def solve(self) -> str:
        f = open(self.FILE_NAME)
        data = f.readlines()
        s = data[0].split()
        s = int(s[0])
        del (data[0])
        for i in range(0, len(data)):
            data[i] = int(data[i])
        data = sorted(data)
        summa = 0
        for count in range(0, len(data)):
            if summa + data[count] > s: break
            summa += data[count]

        zapas = s - summa
        for i in range(0, len(data)):
            if data[i] - data[count - 1] <= zapas:
                itog = data[i]

        return f"{count} {itog}"
