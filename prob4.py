def gf_add(a, b):
    return a ^ b

def gf_mul(a, b, mod):
    p = 0
    while b:
        if b & 1:
            p ^= a
        high_bit_set = a & 0x80  # For GF(2^8), check the highest bit (0x80 is 10000000 in binary, for x^7)
        a <<= 1
        if high_bit_set:
            a ^= mod  # Apply the irreducible polynomial here to reduce the degree
        b >>= 1
    return p


def gf_degree(a):
    res = 0
    while a:
        a >>= 1
        res += 1
    return res - 1  # Minus 1 to get the correct degree

def gf_invert(a, mod):
    v = mod
    g1 = 1
    g2 = 0
    j = gf_degree(a) - gf_degree(mod)

    while a != 1:
        if j < 0:
            a, v = v, a
            g1, g2 = g2, g1
            j = -j

        a ^= v << j
        g1 ^= g2 << j

        while gf_degree(a) >= gf_degree(mod):
            a ^= mod << (gf_degree(a) - gf_degree(mod))

        j = gf_degree(a) - gf_degree(v)

    return g1

a = 0x49  # 1001001
b = 0x19  # 11001
mod = 0x111  # 100010001

# a*b
# b_inv = gf_invert(b, mod)
result_mul = gf_mul(a, b, mod)

# print("b^-1 =", bin(b_inv)[2:].zfill(8))  
print("a * b =", bin(result_mul)[2:].zfill(8))  

