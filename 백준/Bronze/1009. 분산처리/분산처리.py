dictN = {
    0: [10],
    1: [1],
    2: [2, 4, 8, 6],
    3: [3, 9, 7, 1],
    4: [4, 6],
    5: [5],
    6: [6],
    7: [7, 9, 3, 1],
    8: [8, 4, 2, 6],
    9: [9, 1]
}

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    ld = a % 10
    n = dictN[ld]
    Idx = (b - 1) % len(n)
    print(n[Idx])