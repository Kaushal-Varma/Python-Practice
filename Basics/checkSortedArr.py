class Solution:
    def arraySortedOrNot(self, arr: list) -> bool:
        for i in range(len(arr)-1):
            if arr[i] <= arr[i+1]:
                continue
            else:
                return False

        return True

def main():
    myList = [1,2,3,6,5]
    s=Solution()
    print(s.arraySortedOrNot(myList))

if __name__ == "__main__":
    main()


