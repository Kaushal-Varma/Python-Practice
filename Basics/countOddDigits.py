class Solution:
    def oddDigits(self, n: int) -> int:
        # Example n = 123,  output = 2
        count = 0
        n = abs(n)
        while n>0:
            temp=n%10 
            n //= 10 
            if not temp%2 == 0:
                count += 1
        return count

def main():
    s=Solution()
    print(s.oddDigits(int(input("What's the number? "))))

if __name__ == "__main__":
    main()