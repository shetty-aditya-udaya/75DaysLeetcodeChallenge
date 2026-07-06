class Solution:
    def merge_sort(self,nums):
        if len(nums)<=1:
            return nums
        mid=len(nums)//2
        left_arr=nums[:mid]
        right_arr=nums[mid:]
        left=self.merge_sort(left_arr)
        right=self.merge_sort(right_arr)
        return self.merge_array(left,right)

    def merge_array(self,left,right):
        result=[]
        i,j = 0,0
        n,m = len(left),len(right)
        while i<n and j<m:
            if left[i]<=right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1

        while i<n:
            result.append(left[i])
            i+=1

        while j<m:
            result.append(right[j])
            j+=1
        return result

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)
        
        