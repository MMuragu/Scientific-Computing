import numpy as np

def dot_product(a, b):
    try:
        if len(a) != len(b):
            raise ValueError("Vectors must have same length")
        arr_a = np.array(a)
        arr_b = np.array(b)
        return np.dot(arr_a, arr_b)
    except ValueError as e:
        return str(e)

# Example usage:
print(dot_product([1, 2, 3], [4, 5, 6]))  # 32
print(dot_product([1, 2], [3]))           # Error message