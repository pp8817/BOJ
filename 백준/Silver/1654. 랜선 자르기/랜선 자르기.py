import sys
input = lambda: sys.stdin.readline().rstrip()

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]

start, end = 1, max(lan)

while start <= end: # 이분 탐색으로 적절한 랜선의 길이를 탐색
    mid = (start+end)//2
    lines = 0
    for i in lan:
        lines += i//mid

    if lines >= n:
        start = mid + 1
    else:
        end = mid-1
print(end)