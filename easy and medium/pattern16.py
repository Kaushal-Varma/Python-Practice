def main():
    x = int(input("What's x? "))
    pattern16(x)

def pattern16(n):
    for i in range(0,n):
        for _ in range(i):
            print(chr(65+i),end=' ')
        print()

if __name__ == "__main__":
    main()