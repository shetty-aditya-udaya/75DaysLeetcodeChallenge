class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        mini=float("inf")
        low,high=0,n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]<=nums[high]:
                mini=min(mini,nums[mid])
                high=mid-1
            else:
                mini=min(mini,nums[low])
                low=mid+1
        return mini

        