n = int(input("Enter the number of rows: "))
for i in range(4, n*1 , n+3 , 5 ):
    for j in range(i):
        print('* ⭐' , end='🎉')
    print()