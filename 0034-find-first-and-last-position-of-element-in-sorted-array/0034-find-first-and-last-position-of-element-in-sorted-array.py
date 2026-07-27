class Solution:
    def lowerbound(self,nums,target):
        n=len(nums)
        lb=n
        low,high=0,n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                lb=mid
                high=mid-1
            else:
                low=mid+1
        return lb

    def upperbound(self,nums,target):
        n=len(nums)
        UB=n
        low,high=0,n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>target:
                UB=mid
                high=mid-1
            else:
                low=mid+1
        return UB

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb=self.lowerbound(nums,target)
        if lb==len(nums) or nums[lb]!=target:
            return [-1,-1]
        UB=self.upperbound(nums,target)
        return [lb,UB-1]

        
        