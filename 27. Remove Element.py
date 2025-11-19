class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        numscount = nums.count(val)
        for i in range(numscount):
            nums.remove(val)
        return len(nums)