def main():
    x = int(input("What's x? "))
    pattern11(x)

def pattern11(n):
    sub=0
    for i in range(1,n+1):
        if i%2 != 0:
            sub = 1
        else:
            sub = 0
        for _ in range(i):
            print(sub, " ", end='')
            sub = 1-sub
        print()
        



if __name__ == "__main__":
    main()
        

