def twoSum(nums, target):
    complements = {}

    for i in range(len(nums)):
        if nums[i] in complements:
            return [complements[nums[i]], i]
        else:
            complements[target - nums[i]] = i

print(twoSum([3,4,3,6,7,9], 9))            