def pascals(n):
    bico = 1

    for i in range(1, n+1):
        for j in range(1, n-i+1):
            print(' ', end='')
        for j in range(1, i+1):
            # bico = bico * (i-j)//(j+1)
            print(' ', bico, end='')
            bico = bico * (i-j)//(j+1)
            # print(bico)
        print()

# print(pascals(6))


def prime(n):
    
    for i in range(1, n+1):
        for j in range(i):
            print(j+1, end=' ')

print(prime(6))