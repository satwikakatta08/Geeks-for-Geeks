class Solution:

    def sortExceptK(self, arr, k):
        # code here
        val=arr[k]
        arr.remove(val)
        arr.sort()
        arr.insert(k,val)