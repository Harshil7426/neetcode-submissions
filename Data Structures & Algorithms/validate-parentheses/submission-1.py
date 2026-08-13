class Solution:
    def isValid(self, s: str) -> bool:
        map={"}":"{",")":"(","]":"["}
        stack=[]
        for i in s:
            if i not in map:
                stack.append(i)
            else:
                if len(stack)!=0:
                    if map[i]!=stack[-1]:
                        return False
                    else:
                        stack.pop()
                else:
                    return False
        return len(stack)==0