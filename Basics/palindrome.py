class Solution:
    def palindrome(self, n: int) -> bool:
        #Example n = 123, Output = False
        reverse=0
        k = abs(n)
        while k>0:
            temp = k%10
            reverse = (reverse*10) + temp
            k //= 10
        if reverse==n:
            return True
        return False

    
def main():
    s=Solution()
    print(s.palindrome(int(input("What's the number? "))))


if __name__ == "__main__":
    main()