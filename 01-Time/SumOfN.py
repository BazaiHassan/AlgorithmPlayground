import time

start = time.time() * 1000

summation = 0

n = int(input("Sum of numbers from 0 to n = "))

for i in range(n):
    summation = summation + i

print(f"Sum of numbers from 0 to {n} is {summation}")

end = time.time() * 1000

print(f"Time taken is {end - start}")
