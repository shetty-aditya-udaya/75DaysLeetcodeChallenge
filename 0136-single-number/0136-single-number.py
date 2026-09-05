class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        my_dict=dict()

        for num in nums:
            if num in my_dict:
                my_dict[num]+=1
            else:
                my_dict[num]=1

        for num in nums:
            if my_dict[num] == 1:
                return num
        