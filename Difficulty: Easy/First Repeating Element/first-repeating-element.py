class Solution:
    def firstRepeated(self, arr):
        # code here 
        visited=set()
        mi=-1
        for i in range(len(arr)-1,-1,-1):
            if arr[i] in visited:
                mi=i+1
            else:
                visited.add(arr[i])
        return mi