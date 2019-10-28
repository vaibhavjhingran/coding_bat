# Coding Bat - List 1

# first_last6
def first_last6(nums):
  return True if nums[0]==6 or nums[len(nums)-1]==6 else False

# same_first_last
def same_first_last(nums):
  return True if len(nums)>=1 and nums[0]==nums[len(nums)-1] else False

# make_pi
def make_pi():
  return [3,1,4]

# common_end
def common_end(a, b):
  return True if a[0]==b[0] or a[len(a)-1]==b[len(b)-1] else False

# sum3
def sum3(nums):
  sum = 0
  for x in nums:
    sum += nums[x]
  return sum

# rotate_left3
def rotate_left3(nums):
  return nums[1:] + nums[:1]

# reverse3
def reverse3(nums):
  return nums[::-1]

# max_end3
def max_end3(nums):
  if nums[0]>nums[len(nums)-1]:
    return nums[0]*3
  else:
    return nums[len(nums)-1]*3

# sum2
def sum2(nums):
  if len(nums)==0:
    return 0
  elif len(nums)<2:
    return nums[0]
  else:
    return nums[0]+nums[1]

# middle_way
def middle_way(a, b):
  return list(a[1], b[1])

# make_ends
def make_ends(nums):
  return nums[:1] + nums[-1:]

# has23
def has23(nums):
  for each in nums:
    if each ==2 or each ==3:
      return True
  return False

