class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        my_dict = dict()
        n = len(nums)
        for num in nums:
            if num in my_dict:
                return True
            else:
                my_dict[num]=1
        return False
        