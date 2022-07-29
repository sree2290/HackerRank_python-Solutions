n = int(input())

x = map(int, input().split())
x = sorted(x)

for i in range(len(x)):
    if(i != len(x)-1):
        if(x[i]!=x[i-1] and x[i]!=x[i+1]):
            print(x[i])
            break;
    else:
        print(x[i])
