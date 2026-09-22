class Solution:
    def pattern21(self, n):
        for _ in range(n):
            print('*',end='')
        print()
        for _ in range(n-2):
            print('*'+(' '*(n-2))+'*')
        for _ in range(n):
            print('*',end='')
        print()

