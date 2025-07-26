a = 2  # L0
b = 1  # L1

print(a)
print(b)

for _ in range(18):  # Ya imprimimos 2 valores, faltan 18
    c = a + b
    print(c)
    a = b
    b = c