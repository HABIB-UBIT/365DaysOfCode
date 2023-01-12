a=[2,3,9,7,4,1]
max=0
min=a[0]
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
    elif a[i] < min:
        min=a[i]
print("max =", max)
print("min =", min)



