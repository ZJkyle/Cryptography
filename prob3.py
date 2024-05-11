def gf_add(a, b):
    return a ^ b

def gf_mul(a, b, mod=0x13):
    p = 0
    while b:
        if b & 1:
            p ^= a
        high_bit_set = a & 0x8  # Check the high bit (0x8 is 1000 in binary, for x^3)
        a <<= 1
        if high_bit_set:
            a ^= mod
        b >>= 1
    return p

def gf_degree(a):
    res = 0
    while a:
        a >>= 1
        res += 1
    return res - 1  # Minus 1 to get the correct degree

def gf_invert(a, mod=0x13):
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

a = 0x6  # x^2+x = 110 
# b = 0xD  # x^3 + x^2 + 1
mod = 0x13  # x^4 + x + 1, binary 10011

# result_add = gf_add(a, b)
# result_mul = gf_mul(a, b, mod)
a_inv = gf_invert(a, mod)

# print("a + b =", bin(result_add)[2:].zfill(4))  # Format as binary string, padded with zeros
# print("a * b =", bin(result_mul)[2:].zfill(4))  # Format as binary string, padded with zeros
print("a^-1 =", bin(a_inv)[2:].zfill(4))  # Format as binary string, padded with zeros
