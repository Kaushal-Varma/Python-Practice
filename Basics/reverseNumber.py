class Solution:
    def reverse(self, n: int) -> int:
        #Example n = 123, Output = 321
        reverse=0
        k = abs(n)
        while k>0:
            temp = k%10
            reverse = (reverse*10) + temp
            k //= 10

        if n<0:
            return -reverse
        return reverse
    
def main():
    s=Solution()
    print(s.reverse(int(input("What's the number? "))))


if __name__ == "__main__":
    main()

                
