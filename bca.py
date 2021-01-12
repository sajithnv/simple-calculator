class abc:
    def a1(n,m):
        for _ in range(n):
            print(f'{m}')
c=abc
m=str(input('Enter a string: '))
n=int(input('Range: '))
c.a1(n,m)
