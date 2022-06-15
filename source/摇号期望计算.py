p = 0.05
q = 0.01
max = int(95/7) + 1
n = 1
s = 0
d3 = 1
while p < 1:
    d1= n*p
    if n > 1:
        d2 = (1-t)
        d3 = d3 * d2
    s = s + d3*d1
    t = p
    p = p + q
    n = n+ 1
print(s)
print(n)