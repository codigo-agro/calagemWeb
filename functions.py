def calcula_sb(ca, mg, k, na, hal, v2):
    ctctotal = ca + mg + (k/390) + (na/230) + hal
    sb = ca + mg + (k/390) + (na/230)
    v1 = sb/ctctotal*100
    if v1 >= v2:
        return 0
    else:
        return round(((ctctotal * (v2 - v1))/100), 2)

def calcula_al(ca, mg, al, x, arg, prem):
    if prem != '':
        y = 4.002 - (0.125901 * prem) + (0.001205 * (prem**2)) - (0.00000362 * (prem ** 3))
        parte01 = y * al
        parte02 = x - (ca + mg)
        if parte01 <= 0 <= parte02:
            return round(parte02, 2)
        elif parte02 <= 0 <= parte01:
            return round(parte01, 2)
        elif parte01 <= 0 and parte02 <= 0:
            return 0
        else:
            return round((parte01 + parte02), 2)
    elif arg != '':
        y = 0.0302 + (0.06532 * arg) - (0.000257 * (arg ** 2))
        parte01 = y * al
        parte02 = x - (ca + mg)
        if parte01 <= 0 <= parte02:
            return round(parte02, 2)
        elif parte02 <= 0 <= parte01:
            return round(parte01, 2)
        elif parte01 <= 0 and parte02 <= 0:
            return 0
        else:
            return round((parte01 + parte02), 2)

def calcula_alm(ca, mg, k, na, al, mt, x, prem, arg):
    if prem != '':
        y = 4.002 - (0.125901 * prem) + (0.001205 * (prem ** 2)) - (0.00000362 * (prem ** 3))
        t = ca + mg + (k/390) + (na/230) + al
        parte01 = y * (al - (mt * t/100))
        parte02 = x - (ca + mg)
        if parte01 <= 0 <= parte02:
            return round(parte02, 2)
        elif parte02 <= 0 <= parte01:
            return round(parte01, 2)
        elif parte01 <= 0 and parte02 <= 0:
            return 0
        else:
            return round((parte01 + parte02), 2)
    elif arg != '':
        y = 0.0302 + (0.06532 * arg) - (0.000257 * (arg ** 2))
        t = ca + mg + (k / 390) + (na / 230) + al
        parte01 = y * (al - (mt * t / 100))
        parte02 = x - (ca + mg)
        if parte01 <= 0 <= parte02:
            return round(parte02, 2)
        elif parte02 <= 0 <= parte01:
            return round(parte01, 2)
        elif parte01 <= 0 and parte02 <= 0:
            return 0
        else:
            return round((parte01 + parte02), 2)

def guarconi_e_sobreira(ca, mg, k, na, al, hal, v1, mt, x, prem, arg):
    if prem != '':
        y = 4.002 - (0.125901 * prem) + (0.001205 * (prem ** 2)) - (0.00000362 * (prem ** 3))
        ctctotal = ca + mg + (k / 390) + (na / 230) + hal
        t = ca + mg + (k / 390) + (na / 230) + al
        sb = ca + mg + (k / 390) + (na / 230)
        v2 = sb / ctctotal * 100
        ncsb = (ctctotal * (v1 - v2)) / 100

        parte01 = y * (al - (mt * t / 100))
        parte02 = x - (ca + mg)

        met01 = parte01 + parte02
        met02 = ncsb

        if met02 < 0:
            return 0
        elif met02 <= met01 or (met02 >= 0 > met01):
            if met02 < parte02:
                if met01 > ctctotal:
                    return round(ctctotal, 2)
                else:
                    return round(met01, 2)
            elif met02 >= parte02:
                if met02 > ctctotal:
                    return round(ctctotal, 2)
                else:
                    return round(met02, 2)
        elif met01 < met02:
            if met01 <= parte02:
                if met01 > ctctotal:
                    return round(ctctotal, 2)
                else:
                    return round(met01, 2)
            elif met01 > parte02:
                if met01 > ctctotal:
                    return round(ctctotal, 2)
                else:
                    return round(met01, 2)

    elif arg != '':
        y = 0.0302 + (0.06532 * arg) - (0.000257 * (arg ** 2))
        ctctotal = ca + mg + (k / 390) + (na / 230) + hal
        t = ca + mg + (k / 390) + (na / 230) + al
        sb = ca + mg + (k / 390) + (na / 230)
        v2 = sb / ctctotal * 100
        ncsb = (ctctotal * (v1 - v2)) / 100

        parte01 = y * (al - (mt * t / 100))
        parte02 = x - (ca + mg)

        met01 = parte01 + parte02
        met02 = ncsb

        if met02 < 0:
            return 0
        elif met02 <= met01 or (met02 >= 0 > met01):
            if met02 < parte02:
                if met01 > ctctotal:
                    return round(ctctotal, 2)
                else:
                    return round(met01, 2)
            elif met02 >= parte02:
                if met02 > ctctotal:
                    return round(ctctotal, 2)
                else:
                    return round(met02, 2)
        elif met01 < met02:
            if met01 <= parte02:
                if met01 > ctctotal:
                    return round(ctctotal, 2)
                else:
                    return round(met01, 2)
            elif met01 > parte02:
                if met01 > ctctotal:
                    return round(ctctotal, 2)
                else:
                    return round(met01, 2)