import sympy as sp


A = sp.Matrix([[2, 1], [1, 3]])


det_A = A.det()
eigenvalues = A.eigenvals()


# The characteristic equation is det(A - λI) = 0
lambda_ = sp.symbols('λ')
I = sp.eye(2)  # Identity matrix
characteristic_eq = (A - lambda_ * I).det()

print("\nCharacteristic equation:")
print(characteristic_eq)


for eigenvalue in eigenvalues:
    print(f"\nVerifying eigenvalue {eigenvalue}:")
    verification = characteristic_eq.subs(lambda_, eigenvalue)
    print(f"Characteristic equation evaluated at λ = {eigenvalue}: {verification}")
    if verification == 0:
        print("Verification successful: The eigenvalue satisfies the characteristic equation.")
    else:
        print("Verification failed: The eigenvalue does not satisfy the characteristic equation.")