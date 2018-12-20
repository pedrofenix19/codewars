def whoIsNext(names, r):
    s = 0
    n = 1
    p = len(names)
    while(s + p * pow(2,n - 1) < r):
        s += p * pow(2,n - 1)
        n += 1

    j = (r - s - 1) // pow(2,n-1)
    print(f"r={r},s={s},n={n},j={j}")
    return names[j]

names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
r = 53
r = 7230702951
res = "Sheldon"
for i in range(1,100):
    a = whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], i)
    print(a + "\n")