nums = [1,2,3,4,7,9,11,15]


def simpleTwoSum(array,target):
 for number in array[:]:
  if number >= target:
   array.remove(number)
 for i in array[:]:
   if array[-1] + array[i] < target:
    array.remove(i)
   else:
    return(array[-1],array[i])
  
   
   
def quickerTwoSum(array,target):
 newArray = []
 for number in array:
  if target - number in newArray:
   return(target - number, number)
  newArray.append(number)



print("slowerTwoSum: ", simpleTwoSum(nums,9))
print("quickerTwoSum: ", quickerTwoSum(nums,9))
