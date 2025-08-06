import random

### PREREQUISITE VARIABLES
length = int(input("How long should the list be? "))
missingNumber = random.randint(1,length)


### DEFINING FUNCTIONS
def createMissingList(missingNumber,length):
 A = []
 for e in range(1, length+1):
  if e != missingNumber:
    A.append(e)
 return A

B = createMissingList(missingNumber, length)      

def findMissingNumber(B):   
 n = len(B)+1
 expectedSum = n*(n+1)//2
 realSum = sum(B)
 return (expectedSum - realSum)


print("The generated list missing a number: ", B)
print("Actual missing number: ", missingNumber)
print("Number found to be missing: ", findMissingNumber(B))
  



