class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0]*n 

        for i,temp in enumerate(temperatures):
            while stack and stack[-1][0]<temp:
                stack_t,stack_i = stack.pop()
                res[stack_i] = i - stack_i
            stack.append((temp,i)) 
        return res          



        
        