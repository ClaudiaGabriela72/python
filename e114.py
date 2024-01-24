import urllib
import urllib.request
try:
    site = urllib.request.urlopen('https://www.youtube.com.br')
except:
    print('Erro, esse site nao pode ser acessado')
