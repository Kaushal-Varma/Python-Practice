class Solution:
    def linearS(self, nums: list, key: int) -> int:
        for num in range(len(nums)):
            if nums[num] == key:
                return num
        return -1
            
def main():
    searchList = [1,2,3,4,5,6]
    s=Solution()
    if (k := s.linearS(searchList, int(input("Key: ")))) != -1:
        print("Number found at index:", k)
    else:
        print("Number not found")

if __name__ == '__main__':
    main()
