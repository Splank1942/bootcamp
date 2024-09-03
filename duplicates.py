

def remdups(nums: list[int]) -> int:
    i = 0
    l = len(nums) - 1
    if len(nums) == 1: 
        return nums
    else:
        while i < l:
            if nums[i] == nums[i + 1]:
                del nums[i+1]
                l -= 1
                continue
            i += 1
        return nums, l + 1


print(remdups([0,0,1,1,1,2,2,3,3,4]))
