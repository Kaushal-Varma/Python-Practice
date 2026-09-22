def main():
    x = int(input("What's x? "))
    pattern12(x)

def pattern12(n):
    for i in range(1,n+1):
        #print first range of numbers
        for j in range(1,i+1):
            print(j,end='')
    
        #no. of gaps
        for _ in range(2*(n-i)):
            print(" `   ",end='')

        #print second range of numbers

        for j in range(i,0,-1):
            print(j,end='')
        print()
        
    

    









if __name__ == "__main__":
    main()