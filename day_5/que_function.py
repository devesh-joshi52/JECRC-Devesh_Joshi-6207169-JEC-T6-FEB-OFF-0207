def findSum(nums, target):
    for i in range(len(nums)-1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

nums = eval(input("Enter values: "))
target = int(input("Enter your target: "))

print(findSum(nums, target))
