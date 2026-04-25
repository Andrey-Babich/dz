t1 = (1, 2, 3, 4)
t2 = (3, 4, 5, 6)
t3 = (4, 3, 5)

result = set(t1) & set(t2) & set(t3)
print(result)


t1 = (1, 2, 3)
t2 = (3, 4, 5)
t3 = (5, 6, 1)

u1 = set(t1) - set(t2) - set(t3)
u2 = set(t2) - set(t1) - set(t3)
u3 = set(t3) - set(t1) - set(t2)

print(u1, u2, u3)


t1 = (1, 2, 3)
t2 = (1, 5, 3)
t3 = (1, 8, 3)

result = []

for i in range(min(len(t1), len(t2), len(t3))):
    if t1[i] == t2[i] == t3[i]:
        result.append(t1[i])

print(result)