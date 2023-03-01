def swap_them(a, b, nums):
  temp = nums[a]
  nums[a] = nums[b]
  nums[b] = temp
  return nums

list = [3, 11, 10]

starting_ele = 0
small_index = 0
small_num = 0
while starting_ele != len(list) - 1:
  small_index = 10000000
  small_num = 10000000
  for i in range(starting_ele, len(list)):
    if list[i] < small_num:
      small_index = i
      small_num = list[i]
  list = swap_them(starting_ele, small_index, list)
  starting_ele += 1
print(list)
