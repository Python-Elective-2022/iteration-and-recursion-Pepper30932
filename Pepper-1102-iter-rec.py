'''
in function gcd_iterative with variables a and b
      if greater than b
          be lower than b
      otherwise b is less than a
          be less than a
      for iterating lower values
          Checks if the remainder of b and a is equal to zero and the remainder of the bottom and a is equal to zero.
              break out the loop
          another
              is equal to minus 1.

Print the return value from the function.
'''
def gcd_iterative(a, b):
    if a > b:
        lower = b
    else:
        lower = a
    for i in range(lower):
        if b%a == 0 and lower%a == 0:
            break
        else:
            a -= 1
    if a == lower:
        return 1
    else:
        return a

print(gcd_iterative(17, 12))

'''
In function gcd_recursive with variables a and b
      in an if loop if b is less than zero
          return function gcd_recursive with b and the rest of a and b
      restore

Type the return value from gcd_recursive
'''
def gcd_recursive(a, b):
    while(b > 0):
        return gcd_recursive(b,a%b)
    return (a)
    
print(gcd_recursive(45,10))