class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        i = 0
        for i,a in enumerate(nums):
                if i>0 and a == nums[i-1]:
                    continue
                j=i+1
                k=len(nums)-1
                while j<k:
                    threeSum = a + nums[j] + nums[k]
                    if threeSum<0:
                        j+=1
                    elif threeSum>0:
                        k-=1
                    else:
                        res.append([a,nums[j],nums[k]])
                        j+=1
                        while j<k and nums[j] == nums[j-1]:
                            j+=1
        return res            


        