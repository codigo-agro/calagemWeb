def calcula_sb(ca, mg, k, na, hal, v1):
    ctctotal = ca + mg + (k/390) + (na/230) + hal
    sb = ca + mg + (k/390) + (na/230)
    v2 = sb/ctctotal*100
    return round(((ctctotal * (v1 - v2))/100), 2)


def calcula_al(ca, mg, al, y, x):
    parte01 = y * al
    parte02 = x - (ca + mg)
    if parte01 == 0 and parte02 > 0:
        return round(parte02, 2)
    elif parte02 <= 0 and parte01 != 0:
        return round(parte01, 2)
    elif parte01 == 0 and parte02 <=0:
        return 'Está amostra não precisa de calagem segundo o método de neutralização de Alíminio'
    else:
        return round((parte01 + parte02), 2)