def main():
    x = int(input("What's x? "))
    pattern7(x)

def pattern7(n):
    for i in range(n):
        for _ in range(n-i-1):
            print(" ",end='')
        for _  in range((2*i)+1):
            print("*", end='')
        print()

main()