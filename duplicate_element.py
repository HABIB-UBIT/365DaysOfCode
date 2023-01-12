nums = [0,0,1,1,2,3,4,4]
i = 0
while i < len(nums)-1:
    if nums[i] == nums[i+1]:
        nums.remove(nums[i])
    else:
        i += 1
print(nums)
