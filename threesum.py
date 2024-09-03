def ts(nums: list[int], target):
    r = [] 
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == target:
                    r.append([nums[i], nums[j], nums[k]])

    return r

print(ts([-1,0,1,2,-1,-4], 0))