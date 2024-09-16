def matrixReshape(mat, r: int, c: int):
    m = len(mat)
    n = len(mat[0])
#       checking if the expected r*c matrix is the same number of values
    if r*c != m*n:
        return mat
#       making matrix of exact dimensions we want
    new_mat = [[0]*c for i in range(r)]
    print(new_mat)
    j_idx = 0 
    i_idx = 0
#       need to traverse old matrix to re-write new matrix
#       traversing rows
    for i in range(m):
#       traverse list in each row
        for j in range(n):
            value = mat[i][j]
#               start reassigning new_mat
            new_mat[i_idx][j_idx] = value
            # print("value: ", value, "i idx: ", i_idx, "j idx: ", j_idx, "new mat: ", new_mat)
# advanced counter: j_idx % c
            # j_idx = (j_idx += 1) % c
            j_idx += 1
            if j_idx % c == 0:
                j_idx = 0
                i_idx += 1
    return new_mat