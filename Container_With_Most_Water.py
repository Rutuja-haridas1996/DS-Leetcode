# Problem: Container With Most Water
# Leetcode link : https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        i = 0
        j = len(height) - 1
        while(i < j):
            max_area = max(max_area, min(height[i], height[j]) * (j-i))
         
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return max_area
        
        
        
        # TC: O(n^2) SC= O(n^2)
        # areas = []
        # for i in range(0, len(height)):
        #     for j in range(1, len(height)):
        #         area = min(height[i], height[j]) * (j-i)
        #         areas.append(area)
        # return max(areas)
    
    
    
      
