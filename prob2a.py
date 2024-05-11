import galois

# Define the finite field
GF = galois.GF(2**8)

# Define the polynomial x^4 + 1
poly = galois.Poly([1, 0, 0, 0, 1], field=GF)

# Check if the polynomial is irreducible
is_irreducible = poly.is_irreducible()
print(f"The polynomial x^4 + 1 is {'irreducible' if is_irreducible else 'reducible'} over GF(2^8).")

# If reducible, attempt to factor it
if not is_irreducible:
    factor = poly.factors()
    print("Factors:", factor)
