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

@app.route('/tabela')
def tabela():
    return render_template('tabela.html')

@app.route('/send.data', methods = ['POST'])
def send_data():
    #INPUT
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
                                                                    hidrogeniomaisaluminio,
                                                                    saturacaoporbases))

        quantidade_de_calagem = necessidade_de_calagem.replace('.', ',')

        resultado_sb = str(
            'Considerando uma aplicação em área total, a necessidade de calagem é igual à ' + quantidade_de_calagem + ' '
            't/ha.')

        complemento = str('O cálculo final da quantidade de calcário ainda deve levar em conta o '
            'tipo de aplicação - que pode ser em sulco, na projeção da copa da planta, área total ou cova - '
            ' a profundidade de aplicação e o PRNT do calcário que será utilizado.')

        return render_template('page01.html', resultado_sb=resultado_sb, complemento=complemento)

@app.route('/page.al', methods = ['POST'])
def page_al():
    #INPUT
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
            prem = str('1.0')
        elif argila == '':
            argila = str('1.0')

        calcio = calcio.replace(',', '.')
        magnesio = magnesio.replace(',', '.')
        aluminio = aluminio.replace(',', '.')
        argila_n = argila.replace(',', '.')
        chis = chis.replace(',', '.')
        prem_n = prem.replace(',', '.')

        calcio = float(calcio)
        magnesio = float(magnesio)
        aluminio = float(aluminio)
        argila_n = float(argila_n)
        chis = float(chis)
        prem_n = float(prem_n)

        necessidade_de_calagem = str(calcula_al(calcio, magnesio, aluminio, chis, argila_n, prem_n))

        quantidade_de_calagem = necessidade_de_calagem.replace('.', ',')

        resultado_al = str(
            'Considerando uma aplicação em área total, a necessidade de calagem é igual à ' + quantidade_de_calagem + ' '
            't/ha.')

        complemento = str('O cálculo final da quantidade de calcário ainda deve levar em conta o '
                   'tipo de aplicação - que pode ser em sulco, na projeção da copa da planta, área total ou cova - '
                   ' a profundidade de aplicação e o PRNT do calcário que será utilizado.')

        return render_template('page02.html', resultado_al=resultado_al, complemento=complemento)

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
            prem = str('1.0')
        elif argila == '':
            argila = str('1.0')
        calcio = calcio.replace(',', '.')
        magnesio = magnesio.replace(',', '.')
        potassio = potassio.replace(',', '.')
        sodio = sodio.replace(',', '.')
        aluminio = aluminio.replace(',', '.')
        maxsatu = maxsatu.replace(',', '.')
        argila_n = argila.replace(',', '.')
        chis = chis.replace(',', '.')
        prem_n = prem.replace(',', '.')

        calcio = float(calcio)
        magnesio = float(magnesio)
        potassio = float(potassio)
        sodio = float(sodio)
        aluminio = float(aluminio)
        maxsatu = float(maxsatu)
        argila_n = float(argila_n)
        chis = float(chis)
        prem_n = float(prem_n)

        necessidade_de_calagem = str(calcula_alm(calcio, magnesio,potassio, sodio, aluminio, maxsatu, chis, argila_n, prem_n))

        quantidade_de_calagem = necessidade_de_calagem.replace('.', ',')

        resultado_alm = str(
            'Considerando uma aplicação em área total, a necessidade de calagem é igual à ' + quantidade_de_calagem + ' '
            't/ha.')

        complemento = str('O cálculo final da quantidade de calcário ainda deve levar em conta o '
                   'tipo de aplicação - que pode ser em sulco, na projeção da copa da planta, área total ou cova - '
                   ' a profundidade de aplicação e o PRNT do calcário que será utilizado.')

        return render_template('page03.html', resultado_alm=resultado_alm, complemento=complemento)


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
            prem = str('1.0')
        elif argila == '':
            argila = str('1.0')
        calcio = calcio.replace(',', '.')
        magnesio = magnesio.replace(',', '.')
        potassio = potassio.replace(',', '.')
        sodio = sodio.replace(',', '.')
        aluminio = aluminio.replace(',', '.')
        hidrogeniomaisaluminio = hidrogeniomaisaluminio.replace(',', '.')
        saturacaoporbases = saturacaoporbases.replace(',', '.')
        maxsatu = maxsatu.replace(',', '.')
        argila_n = argila.replace(',', '.')
        chis = chis.replace(',', '.')
        prem_n = prem.replace(',', '.')

        calcio = float(calcio)
        magnesio = float(magnesio)
        potassio = float(potassio)
        sodio = float(sodio)
        aluminio = float(aluminio)
        hidrogeniomaisaluminio = float(hidrogeniomaisaluminio)
        saturacaoporbases = float(saturacaoporbases)
        maxsatu = float(maxsatu)
        argila_n = float(argila_n)
        chis = float(chis)
        prem_n = float(prem_n)

        necessidade_de_calagem = str(guarconi_e_sobreira(calcio, magnesio, potassio, sodio, aluminio, hidrogeniomaisaluminio,
                                                     saturacaoporbases, maxsatu, chis, argila_n, prem_n))

        quantidade_de_calagem = necessidade_de_calagem.replace('.', ',')

        resultado_gc = str(
            'Considerando uma aplicação em área total, a necessidade de calagem é igual à ' + quantidade_de_calagem + ' '
            't/ha.')

        complemento = str('O cálculo final da quantidade de calcário ainda deve levar em conta o '
                   'tipo de aplicação - que pode ser em sulco, na projeção da copa da planta, área total ou cova - '
                   ' a profundidade de aplicação e o PRNT do calcário que será utilizado.')

        return render_template('page04.html', resultado_gc=resultado_gc, complemento=complemento)

if (__name__ == '__main__'):
    app.run(debug=True)