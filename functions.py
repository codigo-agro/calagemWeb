def calcula_sb(ca, mg, k, na, hal, v2):
    ctctotal = ca + mg + (k / 390) + (na / 230) + hal
    sb = ca + mg + (k / 390) + (na / 230)
    v1 = sb / ctctotal * 100
    if v1 >= v2:
        return 0
    else:
        return round(((ctctotal * (v2 - v1)) / 100), 2)


def calcula_al(ca, mg, al, x, arg, prem):
    if prem != '':
        y = 4.002 - (0.125901 * prem) + (0.001205 * (prem ** 2)) - (0.00000362 * (prem ** 3))
        parte01 = y * al
        print("parte 01:", parte01)
        parte02 = x - (ca + mg)
        print("parte 02:", parte02)
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
        print('valor de y:', y)
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


def passos(met02, met01, parte02, ctctotal):
    if met02 < 0:
        return 0
    elif met02 <= met01 or (met02 >= 0 > met01):
        if met02 < parte02:
            if met01 > ctctotal:
                return round(ctctotal, 2)
            else:
                return round(met01, 2)
        elif met01 > ctctotal:
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

        met02 = ncsb

        if parte01 <= 0 and parte02 > 0:
            met01 = parte02
            passos(met02, met01, parte02, ctctotal)
        elif parte01 > 0 and parte02 <= 0:
            met01 = parte01
            passos(met02, met01, parte02, ctctotal)
        elif parte01 >= 0 and parte02 >= 0:
            met01 = parte01 + parte02
            passos(met02, met01, parte02, ctctotal)
        elif parte01 < 0 and parte02 < 0:
            met01 = 0
            passos(met02, met01, parte02, ctctotal)

    elif arg != '':
        y = 0.0302 + (0.06532 * arg) - (0.000257 * (arg ** 2))
        ctctotal = ca + mg + (k / 390) + (na / 230) + hal
        t = ca + mg + (k / 390) + (na / 230) + al
        sb = ca + mg + (k / 390) + (na / 230)
        v2 = sb / ctctotal * 100
        ncsb = (ctctotal * (v1 - v2)) / 100

        parte01 = y * (al - (mt * t / 100))
        parte02 = x - (ca + mg)

        met02 = ncsb

        if parte01 <= 0 and parte02 > 0:
            met01 = parte02
            passos(met02, met01, parte02, ctctotal)
        elif parte01 > 0 and parte02 <= 0:
            met01 = parte01
            passos(met02, met01, parte02, ctctotal)
        elif parte01 >= 0 and parte02 >= 0:
            met01 = parte01 + parte02
            passos(met02, met01, parte02, ctctotal)
        elif parte01 < 0 and parte02 < 0:
            met01 = 0
            passos(met02, met01, parte02, ctctotal)


def por_berco(nc, pf, lg, cp, prnt):
    volume = pf * lg * cp
    qc = (nc * volume) / 2000000000 * 1000000 * (100 / prnt)
    return round(qc, 2)


def por_sulco(nc, pf, lg, ep, prnt):
    num_linhas = 100 / ep
    comprimento_linhas = num_linhas * 100 * 100
    vol_sulco = comprimento_linhas * ((lg * pf) / 2)
    vol_cem_cm = vol_sulco / comprimento_linhas * 100
    qc = (nc * vol_cem_cm) / 2000000000 * 1000000 * (100 / prnt)
    return round(qc, 2)


def por_planta(nc, pf, ep, el, sp, prnt):
    vol = 100 * 100 * pf / 100
    num_plantas = 10000 / (ep * el)
    qc = ((nc * vol) / 2000 * (sp / 100) * (100 / prnt)) * 1000000 / num_plantas
    return round(qc, 2)


def area_total(nc, pf, prnt):
    qc = nc * (pf / 20) * (100 / prnt)
    return round(qc, 2)
