def main():
    x = int(input("What's x? "))
    pattern14(x)

def pattern14(n):
    for i in range(1,n+1):
        for j in range(i):
            print(chr(65+j),end=' ')
        print()


if __name__ == "__main__":
    main()