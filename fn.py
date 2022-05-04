def array_front9(nums):
  i=0
  while i<4 and len(nums)>1:
    if nums[i]==9:
      return True
    i+=1
  return False

  array_front9([])
