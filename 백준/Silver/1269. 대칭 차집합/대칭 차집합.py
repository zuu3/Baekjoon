import sys
input = sys.stdin.readline
N, M = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))
result = (A - B) | (B - A)
print(len(result))