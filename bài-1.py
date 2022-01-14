print("a:")
a = input("Nhập tên: ")
print(a)

print("b:")
n = int(len(a))
d = dict()
for i in range(1, n + 1):
    d[i] = i * i
print(d)