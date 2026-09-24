class Solution:
    def pattern22(self, n):
        size = 2*n-1

        for i in range(size):
            for j in range(size):
                distance = i
                if j<distance:
                    distance = j
                if size-1-i<distance:
                    distance =(size-1-i)
                if size-1-j<distance:
                    distance =(size-1-j)

                value = n-distance
                print(value,end=' ')
            print()
        


def main():
    x = int(input("What's x? "))
    sol = Solution()
    sol.pattern22(x)

if __name__ == "__main__":
    main()