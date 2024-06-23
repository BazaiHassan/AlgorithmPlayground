import time

start = time.time() * 1000

n = int(input("Enter a number: "))
finish = True
numberOfDigits = 0
while finish:
    if n % 10 != 0:
        numberOfDigits += 1
        n = int(n / 10)
        print(n)
    else:
        finish = False

print(f"Number of digits: {numberOfDigits}")

end = time.time() * 1000

print(f"Time taken: {end - start}")
