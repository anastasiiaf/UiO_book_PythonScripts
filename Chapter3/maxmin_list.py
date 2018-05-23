

# Exercise 3.22 Max Min
def max_min(a):
    max_value = a[0]
    min_value = a[0] 
    for i in range(1, len(a)-1):
        max_value = (a[i] if a[i]>max_value else max_value)  
        min_value = (a[i] if a[i]<min_value else min_value)
    return(max_value, min_value)

a = [0,120,1,-25,65,0.3,89,3,-45,-9,10.58,4,2.3,11]
max_value, min_value = max_min(a)
print("Max is %.2f and Min is %.2f " % max_min(a))



n = 3
for i in range(1, 13, 2*n):
    for j in range(0,i, 2):
        for k in range(2,j,1):
            b = i>j>k
            if b:
                print(i, j, k)















