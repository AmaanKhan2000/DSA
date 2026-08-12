class Solution:
    def maxArea(self, height: List[int]) -> int:
        tempArea = 0
        maxArea = 0
        i = 0
        j= len(height)-1

        while i<j:
            breadth = j-i 
            if height[i] <= height[j]:
                tempArea = height[i] * breadth
                i+=1
                maxArea = max(tempArea,maxArea)
            elif height[j] < height[i]:
                tempArea = height[j] * breadth
                j-=1
                maxArea = max(tempArea,maxArea)
        return maxArea        

                   

        