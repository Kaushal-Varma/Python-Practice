def main():
    x = int(input("What's x? "))
    pattern6(x)

def pattern6(n):
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(j, end='')
        print()

main()