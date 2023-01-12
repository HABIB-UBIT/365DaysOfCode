def removeElement(nums, val):
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i

# nums = [0,1,2,2,3,0,4,2]
# exp = []
# val =2
# for j in range (len(nums)):
#     if nums[j] != val:
#         exp.append(nums[j])
# print(len(exp),exp)