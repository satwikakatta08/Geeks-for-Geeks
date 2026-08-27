class Solution:
    def findMin(self, n: int) -> int:
       # code here 
       c=0
       c+=n//10
       n%=10
       c+=n//5
       n%=5
       c+=n//2
       n%=2
       c+=n
       return c