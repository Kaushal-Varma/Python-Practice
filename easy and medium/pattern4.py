def main():
    n = int(input("What's x? "))
    pattern2(n)

def pattern2(x):
    for i in range(1,x+1):
        for _ in range(i):
            print(i, end="")
        print("")


main()