data="""0 44 175060 3442 593 54398 9 8101095"""

nums = list(map(int, data.split(" ")))

for i in range(25):
  next_nums = []
  for num in nums:
    if num == 0:
      next_nums.append(1)
    elif len(str(num)) % 2 == 0:
      str_num = str(num)
      next_nums.append(int(str_num[:len(str_num) // 2]))
      next_nums.append(int(str_num[len(str_num) // 2:]))
    else:
      next_nums.append(num * 2024)
  nums = next_nums

print(len(nums))