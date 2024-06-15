import time

n = int(input())
start = round(time.time() * 1000)

# your code...
s = 0
for i in range(n):
    s = (s + i) % 1000000007

finish = round(time.time() * 1000)
print(s)
print((finish - start) / 1000)
