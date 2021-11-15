# Problem : Count and Say
# Leetcode link : https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int):
        
        if n == 1:
            return "1"
        
        original_Str = "1"
        for i in range(1,n):         
            manipulated_num = original_Str + "X"
            stack = []
            new_str = ""
            for i in range( len(manipulated_num)):
                
                if len(stack)!=0 and stack[-1] != manipulated_num[i]   :
                    # empty the stack
                    popped_item = stack[-1]
                    new_str += str(len(stack)) + str(popped_item)
                    stack.clear()

                stack.append(manipulated_num[i])
            original_Str = new_str
            
        return original_Str