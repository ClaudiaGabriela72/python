import requests
from datetime import datetime
import json
from PIL import Image

import pytz
import pycountry_convert as pc


fundo_dia = "#6cc4cc"
fundo_noite = "#484f60"
fundo_tarde = "#bfb86d"
fundo = fundo_dia


def informacao():

    chave = '6e294074ffdf6f93271c99d876c484dd'
    cidade = e_local.get()
    api_link = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(cidade, chave)


    # fazendo chamada da API usando request
    r = requests.get(api_link)
    # convertendo os dados presente na variavel r em dicionario
    dados = r.json()

    print(dados)

    #obtendo zona, pais e horas
    pais_codigo = dados['sys']['country']

    #    zona 
    zona_fuso = pytz.country_timezones[pais_codigo]

    #    pais 
    pais = pytz.country_names[pais_codigo]

    #    data
    zona = pytz.timezone(zona_fuso[0])
    zona_horas = datetime.now(zona)
    zona_horas = zona_horas.strftime("%d %m %Y | %H %M: %S %p")


    #    tempo 
    tempo = dados['main']['temp']
    pressao = dados['main']['pressure']
    humidade = dados['main']['humidity']
    velocidade = dados['wind']['speed']
    descriacao = dados['weather'][0]['description']

    #   mudando informacoes

    def pais_para_continente(i):
        pais_alpha = pc.country_name_to_country_alpha2(i)
        pais_continent_codigo = pc.country_alpha2_to_continent_code(pais_alpha)
        pais_continent_nome = pc.convert_continent_code_to_continent_name(pais_continent_codigo)

        return pais_continent_nome


    continente = pais_para_continente(pais)
    # Logica para mudar a imagem
    
    zona_periodo = datetime.now(zona)
    zona_periodo = zona_periodo.strftime("%H")

    global imagem

    zona_periodo = int(zona_periodo)

    if zona_periodo <= 12:
            imagem = Image.open('projC/imagens/sol_dia.png')
            fundo = fundo_dia
    elif zona_periodo >=13 :
            imagem = Image.open('projC/imagens/sol-63.png')
            fundo = fundo_tarde
    elif zona_periodo >= 18:
            imagem = Image.open('projC/imagens/icons8-lua-cheia-64.png')
            fundo = fundo_noite
    else:
          imagem = Image.open('projC/imagens/icons8-lua-cheia-64.png')
          fundo = fundo_noite