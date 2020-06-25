from flask import Flask, render_template, request
from functions import *

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/page01')
def page01():
    return render_template('page01.html')

@app.route('/page02')
def page02():
    return render_template('page02.html')

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
                                                                    saturacaoporbases,))

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
    ipsilon = request.form['ipsilon']
    chis = request.form['chis']

    # OUTPUT
    if calcio == '' or magnesio == '' or aluminio == '' or ipsilon == '' or chis == '':
        resultado_al = str("Você deixou campos vazios no formulário. Tente novamente sempre digitando um número")
        return render_template('page02.html', resultado_al=resultado_al)

    else:
        calcio = calcio.replace(',', '.')
        magnesio = magnesio.replace(',', '.')
        aluminio = aluminio.replace(',', '.')
        ipsilon = ipsilon.replace(',', '.')
        chis = chis.replace(',', '.')

        calcio = float(calcio)
        magnesio = float(magnesio)
        aluminio = float(aluminio)
        ipsilon = float(ipsilon)
        chis = float(chis)

        necessidade_de_calagem = str(calcula_al(calcio, magnesio, aluminio, ipsilon,
                                                                    chis))

        quantidade_de_calagem = necessidade_de_calagem.replace('.', ',')

        resultado_al = str(
            'Considerando uma aplicação em área total, a necessidade de calagem é igual à ' + quantidade_de_calagem + ' '
            't/ha.')

        complemento = str('O cálculo final da quantidade de calcário ainda deve levar em conta o '
                   'tipo de aplicação - que pode ser em sulco, na projeção da copa da planta, área total ou cova - '
                   ' a profundidade de aplicação e o PRNT do calcário que será utilizado.')

        return render_template('page02.html', resultado_al=resultado_al, complemento=complemento)


if (__name__ == '__main__'):
    app.run(debug=True)