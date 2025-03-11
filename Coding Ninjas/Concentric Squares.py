#https://www.naukri.com/code360/problems/ninja-and-the-number-pattern-i_6581959

#Print only- T(n): O(n), S(n): O(1)
def getNumberPattern(n: int) -> None:
    # Write your solution here.
    size=2*n-1
    matrix=[[0]*size for i in range(size)]

    for i in range(size):
        for j in range(size):                      
             # Initialising the top, down, left and right indices of a cell.
             top = i;
             bottom = j;
             right = size-j-1;
             left = size-i-1;
             print(n- min(min(top,bottom), min(left,right)), end='');

        print()

'''
#Using matrix storage- T(n): O(n), S(n): O(n)
def getNumberPattern(n: int) -> None:
    # Write your solution here.
    size=2*n-1
    matrix=[[0]*size for i in range(size)]

    for i in range(n):
        for j in range(i,size-i):
            matrix[i][j]=matrix[j][i]=matrix[j][size-i-1]=matrix[size-i-1][j]=n-i

    for r in matrix:
        for c in r:
            print(c,end='')
        print()
'''
