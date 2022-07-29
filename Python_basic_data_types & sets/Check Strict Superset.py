x = set(input().split())
N = int(input())
output = True

for i in range(N):
    y = set(input().split())
    if not y.issubset(x):
        output = False
    if len(y) >= len(x):
        output = False

print(output)
