if __name__ == '__main__':
    (_, x) = (int(input()),set(map(int, input().split())))
    y = int(input())
    for _ in range(y):
        (command, newSet) = (input().split()[0],set(map(int, input().split())))
        getattr(x, command)(newSet)

    print (sum(x))
