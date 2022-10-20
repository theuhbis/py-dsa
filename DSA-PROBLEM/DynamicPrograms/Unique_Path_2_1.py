#no. of paths a robot can go from [0,0] to the bottom right corner after checking all the blocks
#ex-INPUT--[[0,0,0],[0,1,0],[0,0,0]] OUTPUT--2

def unique_path(matrix,i,j):

    if(i==len(matrix)-1 and j==len(matrix[0])-1):#checking last box

        return 1

    if(isSafe(matrix,i,j)==1):


        right=unique_path(matrix,i,j+1)
        down=unique_path(matrix,i+1,j)


        return(down+right)
    else:
        return 0

def isSafe(matrix,i,j):

    if(i>=len(matrix) or j>=len(matrix[0]) or matrix[i][j]==1):#checking whether the present positio is safe or not
        return 0
    return 1

matrix=[[0,0,0],[0,1,0],[0,0,0]]

if(matrix[len(matrix)-1][len(matrix[0])-1]==1):
    print(0)
elif(len(matrix[0])==1):
    print( 1)
else:
    print(unique_path(matrix,0,0))

#The above solution will show TLE for the large values, I have used this process just to solve it in another technique other then the preferred method
