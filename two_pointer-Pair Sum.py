class solution:
    def PairSum(nums:List[int], target:int)-> List[int]:
        left , right = 0, len(nums)-1
        while left < right:
            sum = nums[left] + nums[right]
            if sum < target:
                left = left+1
            elif sum > target:
                right -= 1
            else:
                return [left, right]
        return []
    res=PairSum(nums=[-8,-7,0,6,8],target=14)
    print(res)
    
        
