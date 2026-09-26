class Solution:
    def LCM(self,n1: int, n2: int) -> int:
        if n1 > n2:
            n = n1
        else:
            n = n2

        while True:
            if n % n1 == 0 and n % n2 == 0:
                return n
            n += 1

def main():
    s = Solution()

    a = 6
    b = 8

    result = s.LCM(a, b)

    print("LCM =", result)

if __name__ == "__main__":
    main()