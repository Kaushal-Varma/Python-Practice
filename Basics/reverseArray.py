class Solution:
    def reverse(self, arr: list) -> list:
        n = len(arr)
        for i in range(n//2):
            arr[i], arr[n-i-1] = arr[n-i-1], arr[i]

        return arr

def main():
    myList = [1,2,3,4,5]
    s=Solution()
    updated = s.reverse(myList)
    for i in range(len(updated)):
        print(updated[i])

if __name__ == "__main__":
    main()
