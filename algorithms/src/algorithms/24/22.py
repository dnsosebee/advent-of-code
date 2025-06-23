
data="""0 44 175060 3442 593 54398 9 8101095"""


nums = list(map(int, data.split(" ")))

# num rocks per split for each number
s = {}

def do_blink(num, blink_num):
  if blink_num == 75:
    return 1
  k = (num, blink_num)
  if k in s:
    return s[k]
  res = 0
  if num == 0:
    res += do_blink(1, blink_num + 1)
  elif len(str(num)) % 2 == 0:
    str_num = str(num)
    res += do_blink(int(str_num[:len(str_num) // 2]), blink_num + 1)
    res += do_blink(int(str_num[len(str_num) // 2:]), blink_num + 1)
  else:
    res += do_blink(num * 2024, blink_num + 1)
  
  s[k] = res
  return res
  
res = 0
for num in nums:
  res += do_blink(num, 0)

print(res)