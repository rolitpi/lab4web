class Solver20:
    FILE_NAME = "inputs/26-96.txt"

    def solve(self) -> str:
        with open(self.FILE_NAME) as F:
            N = int(F.readline())
            data = {}
            for i in range(N):
                lat, long = map(int, F.readline().split())
                modLat = lat // 10 if lat >= 0 else -(-lat // 10)
                if long in data:
                    data[long].append(modLat)
                else:
                    data[long] = [modLat]

        maxLong, maxCount, diffCount = None, 0, 0
        for long, lats in sorted(data.items()):
            count = len(lats)
            if maxLong == None or count >= maxCount:
                maxLong, maxCount, diffCount = long, count, len(set(lats))

        return f'{maxLong} {diffCount}'
