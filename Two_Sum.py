class Solution:
    def twoSum(self, nums, target):
        d={}
        for i,n in enumerate(nums):
            if n in d:
                return d[n],i
            d[target-n]=i

ob=Solution()
a=[2,7,11,15]
print(ob.twoSum(a,9))
