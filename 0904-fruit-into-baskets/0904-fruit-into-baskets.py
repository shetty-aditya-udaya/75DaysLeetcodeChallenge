class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        maxi=0
        my_dict={}
        n=len(fruits)
        left=0
        right=0
        while right<n:
            my_dict[fruits[right]]=my_dict.get(fruits[right],0)+1
            while len(my_dict)>2:
                my_dict[fruits[left]]-=1
                if my_dict[fruits[left]]==0:
                    del my_dict[fruits[left]]
                left+=1
            if len(my_dict)<=2:
                maxi = max(maxi,right-left+1)
            right+=1
        return maxi
        