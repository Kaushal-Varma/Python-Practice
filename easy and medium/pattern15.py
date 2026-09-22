def main():
    x = int(input("What's x? "))
    pattern15(x)

def pattern15(n):
    for i in range(n,0,-1):
        for j in range(i):
            print(chr(65+j), end=' ')
        print()

if __name__ == "__main__":
    main()