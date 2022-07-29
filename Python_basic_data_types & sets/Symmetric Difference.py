# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
mset = set(map(int, input().split()))
N = int(input())
nset = set(map(int, input().split()))

mdefference = mset.difference(nset)
ndefference = nset.difference(mset)

output = mdefference.union(ndefference)
#print(output)
for i in sorted(list(output)):
    print(i)
