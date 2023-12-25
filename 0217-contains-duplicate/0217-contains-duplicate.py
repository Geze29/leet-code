class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        dict_count = Counter(nums)
        
        for n in dict_count.values():
            if n > 1:
                return True
        return False