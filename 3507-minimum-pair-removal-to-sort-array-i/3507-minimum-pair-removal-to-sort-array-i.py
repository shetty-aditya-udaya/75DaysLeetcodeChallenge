class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        operations = 0

        while True:
            # Check if array is already non-decreasing
            sorted_array = True

            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    sorted_array = False
                    break

            if sorted_array:
                return operations

            # Find adjacent pair with minimum sum
            min_sum = float('inf')
            index = 0

            for i in range(len(nums) - 1):
                pair_sum = nums[i] + nums[i + 1]

                if pair_sum < min_sum:
                    min_sum = pair_sum
                    index = i

            # Replace the pair with their sum
            nums[index] = min_sum
            nums.pop(index + 1)

            operations += 1
        