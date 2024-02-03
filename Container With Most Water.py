'''
Time Complexity: O(N)
Space Complexity: O(1)
'''  

class Solution:
    def maxArea(self, height: List[int]) -> int:

        l, r = 0, len(height)-1
        curr_volume = 0
        max_volume = float('-inf')

        while l <= r:
            if height[l] < height[r]:
                curr_volume = height[l] * (r - l)
                l += 1
            else:
                curr_volume = height[r] * (r - l)
                r -= 1
            max_volume = max(curr_volume, max_volume)
        
        return max_volume


'''
Brute Force
Time Complexity: O(N^2)
Space Complexity: O(1)
'''  

class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_volume = float('-inf')

        for i in range(len(height)):
            for j in range(i+1, len(height)):
                curr_volume = min(height[i], height[j]) * (j - i)
                max_volume = max(curr_volume, max_volume)
 
        return max_volume
        
        
