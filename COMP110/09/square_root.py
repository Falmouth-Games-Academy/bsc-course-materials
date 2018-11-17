square_root = {}
for i in range(30):
    square_root[i*i] = i

for key, value in square_root.items():
    print("The square root of", key, "is", value)
