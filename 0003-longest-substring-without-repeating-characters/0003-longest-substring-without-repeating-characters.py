class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = 0
        n=len(s)
        right = 0
        left = 0
        my_dict = {}
        while right<n:
            if s[right] in my_dict:
                left = max(left,my_dict[s[right]]+1)
            maxi = max(maxi,right-left+1)
            my_dict[s[right]]=right
            right+=1
        return maxi