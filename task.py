# Samvel Antapyan

m = [
            [ 1,  2,  3,  4,  5,  6,  7 ],
            [ 8,  9,  10, 11, 12, 13, 14 ],
            [ 15, 16, 17, 18, 19, 20, 21 ],
            [ 22, 23, 24, 25, 26, 27, 28 ],
            [ 29, 30, 31, 32, 33, 34, 35 ],
            [ 36, 37, 38, 39, 40, 41, 42 ]
        ]
        
columnsCount = 7        
rowsCount = 6

   
newMatrix = [[] for i in range(rowsCount+columnsCount-1)]
 
for i in range(rowsCount):
    for j in range(columnsCount):
        sum=i+j
       
        if(sum%2 ==0):
             # pushing at begining -->
            newMatrix[sum].insert(0,m[i][j])
            # print("begin ", m[i][j])
        else:
 
            # pushing at end of -->
            newMatrix[sum].append(m[i][j])
            # print("end ", m[i][j])
             
for i in newMatrix:
    for j in i:
        print(j)