#no. of paths a robot can go from [0,0] to the bottom right corner after checking all the blocks
#ex-INPUT--[[0,0,0],[0,1,0],[0,0,0]] OUTPUT--2

def unique_path(matrix,solution):

    flag=True
    for i in range(len(matrix[0])):#changing the first row to 1
        if(matrix[0][i]==0 and flag==True):
            solution[0][i]=1
        else:
            solution[0][i]=0
            flag=False

    flag = True
    for i in range(len(matrix)):#changing the first column to 1
        if(matrix[i][0]==0 and flag==True):
            solution[i][0]=1
        else:
            solution[i][0]=0
            flag=False

    for i in range(1,len(matrix)):#calculating the sum of the top and left block
        for j in range(1,len(matrix[0])):
              if(matrix[i][j]==1):
                  solution[i][j]=0
              else:
                  solution[i][j]=solution[i-1][j]+solution[i][j-1]

    return(solution[len(solution)-1][len(solution[0])-1])



matrix=[[0,0,0],[0,1,0],[0,0,0]]
solution=[[0]*len(matrix[0]) for i in range(len(matrix))]

print(unique_path(matrix,solution))

