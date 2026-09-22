def main():
    x = int(input("What's x? "))
    pattern8(x)

def pattern8(n):
    for i in range(n):
        for _ in range(i):
            print(" ",end='')
        for _ in range(2*(n-i)-1):
            print("*",end='')
        print()
            


main()