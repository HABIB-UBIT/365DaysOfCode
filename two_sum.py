# a = [3,2,3]
# target = 6
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         if(a[i] + a [j] == target):
#             print([i,j])
#     break    


def twoSum(nums, target):
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      if nums[i] + nums[j] == target:
        return [i, j]

print(twoSum([3,2,3], 6))