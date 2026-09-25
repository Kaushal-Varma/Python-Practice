class Solution:
    def countOdd(self, arr: list) -> int:
        count=0
        for i in range(len(arr)):
            if arr[i]%2 == 0:
                continue
            count+=1

        return count

def main():
    s=Solution()
    myList = [1,2,3,4,5]
    print(s.countOdd(myList))

if __name__ == "__main__":
    main()
