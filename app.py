from flask import Flask, render_template, request
from functions import *

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/quantidade')
def quantidade():
    return render_template('quantidade.html')


@app.route('/necessidade')
def necessidade():
    return render_template('necessidade.html')


@app.route('/page01')
def page01():
    return render_template('page01.html')


@app.route('/page02')
def page02():
    return render_template('page02.html')


@app.route('/page03')
def page03():
    return render_template('page03.html')


@app.route('/page04')
def page04():
    return render_template('page04.html')


@app.route('/page05')
def page05():
    return render_template('page05.html')


@app.route('/page06')
def page06():
    return render_template('page06.html')


@app.route('/page07')
def page07():
    return render_template('page07.html')


@app.route('/page08')
def page08():
    return render_template('page08.html')


@app.route('/page09')
def page09():
    return render_template('page09.html')


@app.route('/page10')
def page10():
    return render_template('page10.html')


@app.route('/page11')
def page11():
    return render_template('page11.html')

@app.route('/page12')
def page12():
    return render_template('page12.html')

@app.route('/page13')
def page13():
    return render_template('page13.html')


@app.route('/tabela')
def tabela():
    return render_template('tabela.html')


@app.route('/send.data', methods=['POST'])
def send_data():
    # INPUT
    calcio = request.form['calcio']
    magnesio = request.form['magnesio']
    potassio = request.form['potassio']
    sodio = request.form['sodio']
    hidrogeniomaisaluminio = request.form['hidrogenio-mais-aluminio']
    saturacaoporbases = request.form['saturacao-por-bases']

    # OUTPUT
    if calcio == '' or magnesio == '' or potassio == '' or sodio == '' or hidrogeniomaisaluminio == '' \
            or saturacaoporbases == '':
        resultado_sb = str("Você deixou campos vazios no formulário. Tente novamente sempre digitando um número")
        return render_template('page01.html', resultado_sb=resultado_sb)

    else:
        calcio = calcio.replace(',', '.')
        magnesio = magnesio.replace(',', '.')
        potassio = potassio.replace(',', '.')
        sodio = sodio.replace(',', '.')
        hidrogeniomaisaluminio = hidrogeniomaisaluminio.replace(',', '.')
        saturacaoporbases = saturacaoporbases.replace(',', '.')

        calcio = float(calcio)
        magnesio = float(magnesio)
        potassio = float(potassio)
        sodio = float(sodio)
        hidrogeniomaisaluminio = float(hidrogeniomaisaluminio)
        saturacaoporbases = float(saturacaoporbases)

        necessidade_de_calagem = str(calcula_sb(calcio, magnesio, potassio, sodio,
                                                hidrogeniomaisaluminio, saturacaoporbases))

        quantidade_de_calagem = necessidade_de_calagem.replace('.', ',')

        resultado_sb = str(
            'Considerando uma aplicação em área total, numa profundidade de 20 cm, a necessidade de calagem é igual à '
            + quantidade_de_calagem + 't/ha.')

        complemento = str('O próximo passo é clicar no botão abaixo para calcular a quantidade de calcário segundo o '
                          'tipo de aplicação e o PRNT do calcário')

        return render_template('page01_bt.html', resultado_sb=resultado_sb, complemento=complemento)


@app.route('/page.al', methods=['POST'])
def page_al():
    # INPUT
    calcio = request.form['calcio']
    magnesio = request.form['magnesio']
    aluminio = request.form['aluminio']
    argila = request.form['argila']
    chis = request.form['chis']
    prem = request.form['prem']

    # OUTPUT
    if calcio == '' or magnesio == '' or aluminio == '' or chis == '' or (prem == '' and argila == ''):
        resultado_al = str("Você deixou campos vazios no formulário. Tente novamente sempre digitando um número")
        return render_template('page02.html', resultado_al=resultado_al)

    else:
        if prem == '':
            calcio = calcio.replace(',', '.')
            magnesio = magnesio.replace(',', '.')
            aluminio = aluminio.replace(',', '.')
            argila = argila.replace(',', '.')
            chis = chis.replace(',', '.')

            calcio = float(calcio)
            magnesio = float(magnesio)
            aluminio = float(aluminio)
            argila = float(argila)
            chis = float(chis)

            necessidade_de_calagem = str(calcula_al(calcio, magnesio, aluminio, chis, argila, prem))

            quantidade_de_calagem = necessidade_de_calagem.replace('.', ',')

            resultado_al = str(
                'Considerando uma aplicação em área total, numa profundidade de 20 cm, a necessidade de calagem é igual '
                'à ' + quantidade_de_calagem + 't/ha.')

            complemento = str(
                'O próximo passo é clicar no botão abaixo para calcular a quantidade de calcário segundo o '
                'tipo de aplicação e o PRNT do calcário')

            return render_template('page02_bt.html', resultado_al=resultado_al, complemento=complemento)

        elif argila == '':
            calcio = calcio.replace(',', '.')
            magnesio = magnesio.replace(',', '.')
            aluminio = aluminio.replace(',', '.')
            chis = chis.replace(',', '.')
            prem = prem.replace(',', '.')

            calcio = float(calcio)
            magnesio = float(magnesio)
            aluminio = float(aluminio)
            chis = float(chis)
            prem = float(prem)

            necessidade_de_calagem = str(calcula_al(calcio, magnesio, aluminio, chis, argila, prem))

            quantidade_de_calagem = necessidade_de_calagem.replace('.', ',')

            resultado_al = str(
                'Considerando uma aplicação em área total, numa profundidade de 20 cm, a necessidade de calagem é igual à ' + quantidade_de_calagem + ' '
                't/ha.')

            complemento = str('O próximo passo é clicar no botão abaixo para calcular a quantidade de calcário segundo o '
                              'tipo de aplicação e o PRNT do calcário')

            return render_template('page02_bt.html', resultado_al=resultado_al, complemento=complemento)

@app.route('/page.alm', methods = ['POST'])
def page_alm():
    #INPUT
    calcio = request.form['calcio']
    magnesio = request.form['magnesio']
    potassio = request.form['potassio']
    sodio = request.form['sodio']
    aluminio = request.form['aluminio']
    maxsatu = request.form['maxima-sat-aluminio']
    argila = request.form['argila']
    chis = request.form['chis']
    prem = request.form['prem']

    # OUTPUT
    if calcio == '' or magnesio == '' or potassio == '' or sodio == '' or aluminio == '' or maxsatu == '' or chis == '' \
            or (prem == '' and argila == ''):
        resultado_alm = str("Você deixou campos vazios no formulário. Tente novamente sempre digitando um número")
        return render_template('page03.html', resultado_alm=resultado_alm)

    else:
        if prem == '':
            calcio = calcio.replace(',', '.')
            magnesio = magnesio.replace(',', '.')
            potassio = potassio.replace(',', '.')
            sodio = sodio.replace(',', '.')
            aluminio = aluminio.replace(',', '.')
            maxsatu = maxsatu.replace(',', '.')
            chis = chis.replace(',', '.')
            argila = argila.replace(',', '.')

            calcio = float(calcio)
            magnesio = float(magnesio)
            potassio = float(potassio)
            sodio = float(sodio)
            aluminio = float(aluminio)
            maxsatu = float(maxsatu)
            chis = float(chis)
            argila = float(argila)

            necessidade_de_calagem = str(
                calcula_alm(calcio, magnesio, potassio, sodio, aluminio, maxsatu, chis, prem, argila))

            quantidade_de_calagem = necessidade_de_calagem.replace('.', ',')

            resultado_alm = str(
                'Considerando uma aplicação em área total, numa profundidade de 20 cm, a necessidade de calagem é igual '
                'à ' + quantidade_de_calagem + ' t/ha.')

            complemento = str(
                'O próximo passo é clicar no botão abaixo para calcular a quantidade de calcário segundo o '
                'tipo de aplicação e o PRNT do calcário')

            return render_template('page03_bt.html', resultado_alm=resultado_alm, complemento=complemento)

        elif argila == '':
            calcio = calcio.replace(',', '.')
            magnesio = magnesio.replace(',', '.')
            potassio = potassio.replace(',', '.')
            sodio = sodio.replace(',', '.')
            aluminio = aluminio.replace(',', '.')
            maxsatu = maxsatu.replace(',', '.')
            chis = chis.replace(',', '.')
            prem = prem.replace(',', '.')

            calcio = float(calcio)
            magnesio = float(magnesio)
            potassio = float(potassio)
            sodio = float(sodio)
            aluminio = float(aluminio)
            maxsatu = float(maxsatu)
            chis = float(chis)
            prem = float(prem)

            necessidade_de_calagem = str(calcula_alm(calcio, magnesio,potassio, sodio, aluminio, maxsatu, chis,  prem, argila))

            quantidade_de_calagem = necessidade_de_calagem.replace('.', ',')

            resultado_alm = str(
                'Considerando uma aplicação em área total, numa profundidade de 20 cm, a necessidade de calagem é igual à ' + quantidade_de_calagem + ' '
                't/ha.')

            complemento = str('O próximo passo é clicar no botão abaixo para calcular a quantidade de calcário segundo o '
                              'tipo de aplicação e o PRNT do calcário')

            return render_template('page03_bt.html', resultado_alm=resultado_alm, complemento=complemento)


@app.route('/page.gc', methods = ['POST'])
def page_gc():
    #INPUT
    calcio = request.form['calcio']
    magnesio = request.form['magnesio']
    potassio = request.form['potassio']
    sodio = request.form['sodio']
    aluminio = request.form['aluminio']
    hidrogeniomaisaluminio = request.form['hidrogenio-mais-aluminio']
    saturacaoporbases = request.form['saturacao-por-bases']
    maxsatu = request.form['maxima-sat-aluminio']
    argila = request.form['argila']
    chis = request.form['chis']
    prem = request.form['prem']

    # OUTPUT
    if calcio == '' or magnesio == '' or chis == '' or potassio == '' or sodio == '' or aluminio == ''\
            or hidrogeniomaisaluminio == '' or saturacaoporbases == '' or maxsatu == '' or chis == '' \
            or (prem == '' and argila == ''):
        resultado_gc = str("Você deixou campos vazios no formulário. Tente novamente sempre digitando um número")
        return render_template('page04.html', resultado_gc=resultado_gc)

    else:
        if prem == '':
            calcio = calcio.replace(',', '.')
            magnesio = magnesio.replace(',', '.')
            potassio = potassio.replace(',', '.')
            sodio = sodio.replace(',', '.')
            aluminio = aluminio.replace(',', '.')
            hidrogeniomaisaluminio = hidrogeniomaisaluminio.replace(',', '.')
            saturacaoporbases = saturacaoporbases.replace(',', '.')
            maxsatu = maxsatu.replace(',', '.')
            argila = argila.replace(',', '.')
            chis = chis.replace(',', '.')

            calcio = float(calcio)
            magnesio = float(magnesio)
            potassio = float(potassio)
            sodio = float(sodio)
            aluminio = float(aluminio)
            hidrogeniomaisaluminio = float(hidrogeniomaisaluminio)
            saturacaoporbases = float(saturacaoporbases)
            maxsatu = float(maxsatu)
            argila = float(argila)
            chis = float(chis)

            necessidade_de_calagem = str(
                guarconi_e_sobreira(calcio, magnesio, potassio, sodio, aluminio, hidrogeniomaisaluminio,
                                    saturacaoporbases, maxsatu, chis, prem, argila))

            quantidade_de_calagem = necessidade_de_calagem.replace('.', ',')

            resultado_gc = str(
                'Considerando uma aplicação em área total, numa profundidade de 20 cm, a necessidade de calagem é igual à ' + quantidade_de_calagem + ' '
                                                                                                                                                      't/ha.')

            complemento = str(
                'O próximo passo é clicar no botão abaixo para calcular a quantidade de calcário segundo o '
                'tipo de aplicação e o PRNT do calcário')

            return render_template('page04_bt.html', resultado_gc=resultado_gc, complemento=complemento)

        elif argila == '':
            calcio = calcio.replace(',', '.')
            magnesio = magnesio.replace(',', '.')
            potassio = potassio.replace(',', '.')
            sodio = sodio.replace(',', '.')
            aluminio = aluminio.replace(',', '.')
            hidrogeniomaisaluminio = hidrogeniomaisaluminio.replace(',', '.')
            saturacaoporbases = saturacaoporbases.replace(',', '.')
            maxsatu = maxsatu.replace(',', '.')
            chis = chis.replace(',', '.')
            prem = prem.replace(',', '.')

            calcio = float(calcio)
            magnesio = float(magnesio)
            potassio = float(potassio)
            sodio = float(sodio)
            aluminio = float(aluminio)
            hidrogeniomaisaluminio = float(hidrogeniomaisaluminio)
            saturacaoporbases = float(saturacaoporbases)
            maxsatu = float(maxsatu)
            chis = float(chis)
            prem = float(prem)

            necessidade_de_calagem = str(guarconi_e_sobreira(calcio, magnesio, potassio, sodio, aluminio, hidrogeniomaisaluminio,
                                                         saturacaoporbases, maxsatu, chis, prem, argila))

            quantidade_de_calagem = necessidade_de_calagem.replace('.', ',')

            resultado_gc = str(
                'Considerando uma aplicação em área total, numa profundidade de 20 cm, a necessidade de calagem é igual à ' + quantidade_de_calagem + ' '
                't/ha.')

            complemento = str('O próximo passo é clicar no botão abaixo para calcular a quantidade de calcário segundo o '
                              'tipo de aplicação e o PRNT do calcário')

            return render_template('page04_bt.html', resultado_gc=resultado_gc, complemento=complemento)

@app.route('/page_berco', methods = ['POST'])
def page_berco():
    #INPUT
    nc = request.form['nc']
    pf = request.form['pf']
    lg = request.form['lg']
    cp = request.form['cp']
    prnt = request.form['prnt']

    # OUTPUT
    if (nc == '' or pf == '' or lg == '' or cp == '' or prnt == ''):
        resultado_berco = str("Você deixou campos vazios no formulário. Tente novamente sempre digitando um número")
        return render_template('page06.html', resultado_berco=resultado_berco)

    else:
        nc = nc.replace(',', '.')
        pf = pf.replace(',', '.')
        lg = lg.replace(',', '.')
        cp = cp.replace(',', '.')
        prnt = prnt.replace(',', '.')

        nc = float(nc)
        pf = float(pf)
        lg = float(lg)
        cp = float(cp)
        prnt = float(prnt)


        necessidade_de_calagem = str(por_berco(nc, pf, lg, cp, prnt))

        quantidade_de_calagem = necessidade_de_calagem.replace('.', ',')

        resultado_berco = str(
            'Considerando uma aplicação em cova a quantidade de calcário a ser aplicada é igual à '
            + quantidade_de_calagem + ' '
            'g/cova.')

        return render_template('page06.html', resultado_berco=resultado_berco)

@app.route('/page_sulco', methods = ['POST'])
def page_sulco():
    #INPUT
    nc = request.form['nc']
    pf = request.form['pf']
    lg = request.form['lg']
    ep = request.form['ep']
    prnt = request.form['prnt']

    # OUTPUT
    if (nc == '' or pf == '' or lg == '' or ep == '' or prnt == ''):
        resultado_sulco = str("Você deixou campos vazios no formulário. Tente novamente sempre digitando um número")
        return render_template('page07.html', resultado_sulco=resultado_sulco)

    else:
        nc = nc.replace(',', '.')
        pf = pf.replace(',', '.')
        lg = lg.replace(',', '.')
        ep = ep.replace(',', '.')
        prnt = prnt.replace(',', '.')



        nc = float(nc)
        pf = float(pf)
        lg = float(lg)
        ep = float(ep)
        prnt = float(prnt)


        necessidade_de_calagem = str(por_sulco(nc, pf, lg, ep, prnt))

        quantidade_de_calagem = necessidade_de_calagem.replace('.', ',')

        resultado_sulco = str(
            'Considerando uma aplicação em sulco a quantidade de calcário a ser aplicada é igual à '
            + quantidade_de_calagem + ' '
            'g/m de sulco.')

        return render_template('page07.html', resultado_sulco=resultado_sulco)

@app.route('/page_planta', methods = ['POST'])
def page_planta():
    #INPUT
    nc = request.form['nc']
    pf = request.form['pf']
    el = request.form['el']
    ep = request.form['ep']
    sp = request.form['sp']
    prnt = request.form['prnt']

    # OUTPUT
    if (nc == '' or pf == '' or el == '' or ep == '' or sp == '' or prnt == ''):
        resultado_planta = str("Você deixou campos vazios no formulário. Tente novamente sempre digitando um número")
        return render_template('page08.html', resultado_planta=resultado_planta)

    else:
        nc = nc.replace(',', '.')
        pf = pf.replace(',', '.')
        el = el.replace(',', '.')
        ep = ep.replace(',', '.')
        sp = sp.replace(',', '.')
        prnt = prnt.replace(',', '.')



        nc = float(nc)
        pf = float(pf)
        el = float(el)
        ep = float(ep)
        sp = float(sp)
        prnt = float(prnt)


        necessidade_de_calagem = str(por_planta(nc, pf, el, ep, sp, prnt))

        quantidade_de_calagem = necessidade_de_calagem.replace('.', ',')

        resultado_planta = str(
            'Considerando uma aplicação na projeção da copa da planta a quantidade de calcário a ser aplicada é igual à '
            + quantidade_de_calagem + ' '
            'g/planta.')

        return render_template('page08.html', resultado_planta = resultado_planta)

@app.route('/page_area_total', methods = ['POST'])
def page_area_total():
    #INPUT
    nc = request.form['nc']
    pf = request.form['pf']
    prnt = request.form['prnt']

    # OUTPUT
    if (nc == '' or pf == '' or prnt == ''):
        resultado_area_total = str("Você deixou campos vazios no formulário. Tente novamente sempre digitando um número")
        return render_template('page09.html', resultado_area_total = resultado_area_total)

    else:
        nc = nc.replace(',', '.')
        pf = pf.replace(',', '.')
        prnt = prnt.replace(',', '.')

        nc = float(nc)
        pf = float(pf)
        prnt = float(prnt)

        necessidade_de_calagem = str(area_total(nc, pf, prnt))

        quantidade_de_calagem = necessidade_de_calagem.replace('.', ',')

        resultado_area_total = str(
            'Considerando uma aplicação em area total a quantidade de calcário a ser aplicada é igual à '
            + quantidade_de_calagem + ' '
            't/ha.')

        return render_template('page09.html', resultado_area_total=resultado_area_total)

if (__name__ == '__main__'):
    app.run(debug=True)

