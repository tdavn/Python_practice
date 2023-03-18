import random

A = []
for i in range(0, 50):
    n = random.randint(1, 100)
    A.append(n)

B = []
for i in range(0, 100):
    x = random.randint(1, 500)
    B.append(x)

list1 = []

for i in A:
    for o in B:
        if i == o:
            list1.append(i)

print(f'similarities: {list1}')
print(f'length of similar values: {len(list1)}')
print()

list2 = []

for i in A:
    for o in B:
        if o != i:
            list2.append(o)

for i in list2:
    for o in list2:
        if o == i:
            list2.remove(o)

print(f'diffrences: {list2}')
print(f'length of different values: {len(list2)}')

