import time

x = int(input("Enter x : "))
y = int(input("Enter y : "))
z = int(input("Enter z : "))

start = time.time() * 1000
max_num = x
if x > y:
    if x > z:
        max_num = x
    else:
        max_num = z
else:
    if y > z:
        max_num = y
    else:
        max_num = z

print(f"Max number is {max_num}")
end = time.time() * 1000
print(f"Time taken is {end - start}")
