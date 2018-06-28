print('-----Number 1-----')
num_list = [1, 3, 54, 23, 556]
print(sum(num_list))

print('-----Number 2-----')
print(max(num_list))

print('-----Number 3-----')
print(min(num_list))

print('-----Number 4-----')
for x in num_list:
    if x % 2 == 0:
        print(x)

print('-----Number 5-----')
num_list = [1, -3, 54, -23, 556]
for x in num_list:
    if x > 0:
        print(x)

print('-----Number 6-----')
new_num_list = []
for x in num_list:
    if x > 0:
        new_num_list.append(x)
print(new_num_list)

print('-----Number 7-----')
my_new_num_list = []
for x in num_list:
    my_new_num_list.append(x * 4)
print(my_new_num_list)

print('-----Number 8-----')
l1 = [2, 4, 5]
l2 = [2, 3, 6]
l3 = []

for x in range(len(l1)):
    l3.append(l1[x] * l2[x])
print(l3)

print('-----Number 9-----')
a = [2, -2] 
a1 = [4, -8]
arrayA = []


b = [3, 6]
b1 = [-7, 4]
arrayB = []

arrayC = []

arrayA.append(a)
arrayA.append(a1)

arrayB.append(b)
arrayB.append(b1)

arrayCC = []

for r in range(0,2):
    for c in range(0,2):
        arrayCC.append(arrayA[r][c] + arrayB[r][c])

    arrayC.append(arrayCC)
    arrayCC = []
print(arrayC)

print('-----Number 10-----')

arrayCC = []

for r in range(0,2):
    for c in range(0,2):
        arrayCC.append(arrayA[r][c] + arrayB[r][c])

    arrayC.append(arrayCC)
    arrayCC = []
print(arrayC)

print('-----Number 11-----')
array1 = [1, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9, 9, 10]
array2 = []

for x in array1:
    if x not in array2:
        array2.append(x)
print(array2)







