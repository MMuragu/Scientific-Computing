import sympy as sp


P, e, N = sp.symbols('P e N')


C = P**e % N
print("Encryption function:")
print(f"C = {C}")


d = pow(P, -1, N)
print("\nModular inverse of P (decryption key):")
print(f"d = {d}")


P_val = 7
e_val = 3
N_val = 33

C_val = (P_val**e_val) % N_val
print(f"\nCiphertext C for P = {P_val}, e = {e_val}, N = {N_val}:")
print(f"C = {C_val}")