# it looks like any int = sum of at most four squares?

ub = 10000
A = set([x*x for x in range(ub) if x*x < ub])
print(A)

twice = {a+b for a in A for b in A if a+b<ub}
# print(A|twice)
thrice = {a+b+c for a in A for b in A for c in A if a+b+c<ub}
# print(A|twice|thrice)
four = {a+b+c+d for a in A for b in A for c in A for d in A if a+b+c+d<ub}
# print(A|twice|thrice|four)
candidate = A|twice|thrice|four
for k in range(ub):
    if k not in candidate:
        print(f"{k} missing")
        break
else:
    print('All present')
