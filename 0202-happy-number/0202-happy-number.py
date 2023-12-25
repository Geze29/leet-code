class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        if n == 1:
            return True
        while n != 1:
            num = str(n)
            val = 0
            for i in range(len(num)):
                val += (int(num[i]) * int(num[i]))
            if val in visit:
                return False
            else:
                visit.add(val)
                n = val
            
        return True