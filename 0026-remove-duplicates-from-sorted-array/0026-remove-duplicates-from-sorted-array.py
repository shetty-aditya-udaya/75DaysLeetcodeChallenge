class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq_map={}
        for i in range(0,len(nums)):
            freq_map[nums[i]]=0
        j=0
        for key in freq_map:
            nums[j]=key
            j+=1
        return j
        