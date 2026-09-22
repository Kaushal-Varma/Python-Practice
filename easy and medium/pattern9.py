def main():
    x = int(input("What's x? "))
    pattern9(x)

def pattern9(n):
    for i in range(n):
        for _ in range(n-i-1):
            print(" ",end='')
        for _  in range((2*i)+1):
            print("*", end='')
        print()

    for i in range(n):
        for _ in range(i):
            print(" ",end='')
        for _ in range(2*(n-i)-1):
            print("*",end='')
        print()
    
main()