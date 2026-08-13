class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {')' : '(', '}':'{', ']':'['}
        stk = []

        for symbol in s:
            if symbol in closeToOpen:
                if stk and stk[-1]==closeToOpen[symbol]:
                    stk.pop()
                else:
                    return False    
            else:
                stk.append(symbol)
        return False if stk else True            