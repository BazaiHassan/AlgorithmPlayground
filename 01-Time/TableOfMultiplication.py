import time

start = time.time() * 1000

n = int(input("Enter a number: "))
w, h = n, n
table = [[1 for x in range(w)] for y in range(h)]
for i in range(n):
    for j in range(w):
        table[i][j] = i*j
end = time.time() * 1000

for i in range(n):
    print(table[i])

print(f"Time taken: {end - start}")

