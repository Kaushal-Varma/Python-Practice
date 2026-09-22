def main():
    n = int(input("What's x? "))
    pattern2(n)

def pattern2(x):
    for i in range(1,x+1):
        for j in range(1,i+1):
            print(j, end="")
        print("")


main()