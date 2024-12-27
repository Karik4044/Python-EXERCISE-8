import numpy as np

# Function to multiply two matrices A and B
def multiply_matrices(A, B):
    n = len(A)        # Number of rows in A
    m = len(A[0])     # Number of columns in A (and rows in B)
    o = len(B[0])     # Number of columns in B
    
    # Initialize result matrix with zeros (n x o)
    result = [[0 for _ in range(o)] for _ in range(n)]
    
    # Perform matrix multiplication
    for i in range(n):
        for j in range(o):
            for k in range(m):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Input matrices
A = [[1, 2], [3, 4], [5, 6]]  # 3x2 matrix
B = [[7, 8], [9, 10]]         # 2x2 matrix

# Multiply matrices using custom function
result_custom = multiply_matrices(A, B)

# Check result using NumPy's matmul()
result_numpy = np.matmul(A, B)

# Print results
print("Result using custom function:")
for row in result_custom:
    print(row)

print("\nResult using NumPy's matmul():")
print(result_numpy)
