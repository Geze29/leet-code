class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sStack = []
        tStack = []
        
        for i in range(len(s)):
            if s[i] == "#":
                if len(sStack) != 0:
                    sStack.pop()
            else:
                sStack.append(s[i])
        for i in range(len(t)):
            if t[i] == "#":
                if len(tStack) != 0:
                    tStack.pop()
            else:
                tStack.append(t[i])
                
        if sStack == tStack:
            return True
        else:
            return False
        