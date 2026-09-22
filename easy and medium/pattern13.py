def main():
    x = int(input("What's x? "))
    pattern13(x)


def pattern13(n):
    k = 1
    for i in range(1,n+1):
        for _ in range(i):
            print(k,end=' ')
            k+=1
        print()

if __name__ == "__main__":
    main()
        