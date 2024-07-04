the_string = input()
n, q_i = the_string.split()
n = int(n)
q_i = int(q_i)

if 1 <= n <= 100000:
    if 1 <= q_i <= 100000:

        a_string = input()
        a = []
        q = []

        if 1 <= len(a_string.split()) <= 1000000:
            for i in range(len(a_string.split())):
                a.append(int(a_string.split()[i]))

        for j in range(int(q_i)):
            q_string = int(input())
            q.append(q_string)

        if 1 <= len(q) <= 1000000:

            for i in range(len(q)):
                counter = 0
                for j in range(len(a)):
                    if q[i] > a[j]:
                        counter += 1
                print(counter)
