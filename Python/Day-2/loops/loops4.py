# print
# 1 
# 2 3 
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
n=int(input("Enter the number of rows :: "  ))
count=1
for i in range(n):
    for j in range(i):
        print( count ,end=" ")
        count+=1
    print()