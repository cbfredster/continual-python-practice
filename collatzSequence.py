
M = []

def collatz(n):	
    M.append(n)
    if n == 1:
        return
    if n % 2 == 0:
        return(collatz(int(n/2)))
    if n % 2 != 0:
        return(collatz((3*n+1)))


n = input("Submit a number to the Collatz Sequence algorithm:")

try:
    n = float(n)
    if n.is_integer() == True and n > 0:
        n = int(n) 	
        collatz(n)
        print(M)
    else: 	
        print("Error, must be a positive whole number.")
except:
    print("Error, must be a number.")

