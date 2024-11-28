def count(x, n):
    if n == 0:
        return 1
    return (x * count(x, n - 1)) / n


print(count(5, 5))



def find_max():
    n = int(input())
    if n == 0:
        return 0
    else:
        return max(n, find_max())


print(find_max())
