for i in range (1,6):    # rows = 5 ,pyramid
    for k in range (1,6-i):
        print(" ",end=" ")
    for j in range (1,2*i):
        print("*",end=" ")
    print( )
for i in range (4,0,-1):  # rows=4, revers pyramid              
    for j in range (1,6-i):
        print(" ",end=" ")
    for k in range (1,2*i):
        print("*",end=" ")
    print( )
