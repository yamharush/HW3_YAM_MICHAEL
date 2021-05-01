def isHaveDominantDiagonal(m, n):
    '''
    isHaveDominantDiagonal function
    :param m: matrix
    :param n: size of the matrix
    :return: True if the matrix have dominant diagonal, False if she haven't
    '''
    # for each row
    for i in range(0, n):
        sum = 0
        for j in range(0, n):
            sum = sum + abs(m[i][j])
        sum = sum - abs(m[i][i])
        # checking if diagonal
        # element is less than
        # sum of non-diagonal
        # element.
        if (abs(m[i][i]) < sum):
            print("the matrix doesn't have dominant diagonal!")
            return False
    print("the matrix have dominant diagonal!")
    return True

def jacobi_method(matrix,vector):
    x0=0
    y0=0    #start from the guess 0,0,0
    z0=0
    counter=1
    e=0.00001 #the epsilon
    condition = True
    while condition:
        x1 = (vector[0][0]-matrix[0][1]*y0-matrix[0][2]*z0)/matrix[0][0]
        y1 = (vector[1][0]-matrix[1][0]*x0 - matrix[1][2]*z0)/matrix[1][1]
        z1 = (vector[2][0]-matrix[2][0]*x0-matrix[2][1]*y0)/matrix[2][2]
        print('%d\t%0.6f\t%0.6f\t%0.6f\n' % (counter, x1, y1, z1))
        e1 = abs(x0 - x1)
        counter += 1
        x0 = x1
        y0 = y1
        z0 = z1
        condition = e1 > e
    print('\nSolution: x=%0.6f, y=%0.6f and z = %0.6f\n' % (x1, y1, z1))

def gaussSeidel_method(matrix,vector):
    x0=0
    y0=0  #start from the guess 0,0,0
    z0=0
    counter=1
    e=0.00001 #the epsilon
    condition = True
    while condition:
        x1 = (vector[0][0]-matrix[0][1]*y0-matrix[0][2]*z0)/matrix[0][0]
        y1 = (vector[1][0]-matrix[1][0]*x1 - matrix[1][2]*z0)/matrix[1][1]
        z1 = (vector[2][0]-matrix[2][0]*x1-matrix[2][1]*y1)/matrix[2][2]
        print('%d\t%0.6f\t%0.6f\t%0.6f\n' % (counter, x1, y1, z1))
        e1 = abs(x0 - x1)
        counter += 1
        x0 = x1
        y0 = y1
        z0 = z1
        condition = e1 > e
    print('\nSolution: x=%0.6f, y=%0.6f and z = %0.6f\n' % (x1, y1, z1))

# Driver Code
n = 3
m = [[4, 2, 0],
     [2, 10, 4],
     [0, 4, 5]]

b=[[2],[6],[5]]

isHaveDominantDiagonal(m,n)
choise=(input("in which method do you want to get the solution?\n1-Jacobi\n2-Gauss–Seidel\n"))
if choise=='1':
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Jacobi method-->")
    jacobi_method(m,b)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

else:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Gauss Seidel method-->")
    gaussSeidel_method(m,b)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
