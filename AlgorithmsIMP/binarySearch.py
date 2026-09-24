class Solution:
    def binaryS(self, nums: list, key: int) -> int:
        first = 0
        last = len(nums)-1
        while (first <= last):
            mid=(first+last)//2
            if (key<nums[mid]):
                last=mid-1
            elif (key>nums[mid]):
                first=mid+1
            elif key==nums[mid]:
                return mid
        return -1
            
            
def main():
    searchList = [1,2,3,4,5,6]
    s=Solution()
    if (k := s.binaryS(searchList, int(input("Key: ")))) != -1:
        print("Number found at index:", k)
    else:
        print("Number not found")

if __name__ == '__main__':
    main()
