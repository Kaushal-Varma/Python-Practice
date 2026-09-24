class Solution:
    def isPerfect(self, n: int) -> bool:
        sum=0
        for i in range(1,n):
            if n%i==0:
                sum+=i

        if sum == n:
            return True
        return False

def main():
    s=Solution()
    print(s.isPerfect(int(input("What's x? "))))

if __name__ == "__main__":
    main()


# def checkPerfectNumber(self, n: int) -> bool: {*Another method*}
#         if n<=1:
#             return False
#         sum=1
#         i=2

#         while i*i<=n:
#             if n%i == 0:
#                 sum += i

#                 if i!=n//i:
#                     sum += n//i
            
#             i += 1
        
#         return (sum == n) 