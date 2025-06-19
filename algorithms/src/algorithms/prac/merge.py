def merge_sort_1(arr):
  n = len(arr)
  if n < 2: return arr
  a, b, = merge_sort_1(arr[:n//2]), merge_sort_1(arr[n//2:])
  a_i, b_i = 0,0
  res = []
  while True:
    if a_i < len(a) and (b_i >= len(b) or a[a_i] < b[b_i]):
      res.append(a[a_i])
      a_i += 1
    elif b_i < len(b):
      res.append(b[b_i])
      b_i += 1
    else:
      break
  return res

print(merge_sort_1([1,3,5,4,2,3,6,6,5,544,3,4,5]))