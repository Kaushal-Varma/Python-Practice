class Solution:
    def sum(self, nums: list) -> int:
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
        return sum

def main():
    s=Solution()
    myList = [1,2,3,4,5]
    print(s.sum(myList))

if __name__ == "__main__":
    main()
