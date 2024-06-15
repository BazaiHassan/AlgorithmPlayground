import time
# The code is about swapping values of two variables
x = int(input("Enter x : "))
y = int(input("Enter y : "))
start = time.time() * 1000
print(f"initial x : {x}, initial y : {y}")
temp = x
x = y
y = temp
print(f"final x : {x}, final y : {y}")
end = time.time() * 1000
print(f"time taken : {end - start}")


