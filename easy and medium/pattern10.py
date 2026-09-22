def main():
    x = int(input("What's x? "))
    pattern10(x)

def pattern10(n):
    for i in range(1,n+1):
        for _ in range(i):
            print("*",end='')
        print()
    for i in range(n-1,0,-1):
        for _ in range(i):
            print("*",end='')
        print()

main()