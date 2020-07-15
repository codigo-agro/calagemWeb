prem = 6.6
ca = 2
mg = 1.08
al = 3
mt = 25
x = 3.5
na = 5
k = 68


y = 4.002 - (0.125901 * prem) + (0.001205 * (prem ** 2)) - (0.00000362 * (prem ** 3))
t = ca + mg + (k/390) + (na/230) + al
parte01 = y * (al - (mt * t/100))
parte02 = x - (ca + mg)

print('valor de y:', y)
print('valor de y:', t)
print('valor de y:', parte01)
print('valor de y:', parte02)

if parte01 <= 0 <= parte02:
    print(round(parte02, 2))
elif parte02 <= 0 <= parte01:
    print(round(parte01, 2))
elif parte01 <= 0 and parte02 <= 0:
    print(0)
else:
    print(round((parte01 + parte02), 2))
