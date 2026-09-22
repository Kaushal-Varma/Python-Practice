def main():
    n = int(input("What's x? "))
    pattern5(n)

def pattern5(x):
    for i in range(x,0,-1):
        for _ in range(1,i+1):
            print("*", end='')
        print()

main()