class Solution:
    def maxArea(self, heights: List[int]) -> int:
        tempArea = 0
        maxArea = 0
        i = 0
        j= len(heights)-1

        while i<j:
            breadth = j-i 
            if heights[i] <= heights[j]:
                tempArea = heights[i] * breadth
                i+=1
                maxArea = max(tempArea,maxArea)
            elif heights[j] < heights[i]:
                tempArea = heights[j] * breadth
                j-=1
                maxArea = max(tempArea,maxArea)
        return maxArea          


        