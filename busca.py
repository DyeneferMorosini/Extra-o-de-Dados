from typing import Text
import requests

chave_busca = input(Text('Adicione 1 chave de busca: '))


url = 'https://news.google.com/rss/search?q='

parametros = '&hl=pt-BR&gl=BR&ceid=BR%3Apt-419'
url_final = url + chave_busca + parametros
url_final
print(url_final)
response = requests.get(url_final)
response.status_code
response.content

#Extraindo dados do xml
from xml.etree import ElementTree
conteudo = ElementTree.fromstring(response.content)
type(conteudo)
conteudo.tag
conteudo.find('channel').findtext('title')
canais = conteudo.find('channel')
noticias = list(canais)
len(noticias)
noticias = noticias[8:]
noticias
#print(noticias)
for noticia in noticias:
    print('    ')
    print("Titulo: " + noticia.findtext('title'))
    print("Data da Publicação: " + noticia.findtext('pubDate'))
    print("Link: " + noticia.findtext('link'))
    print("Canal: " + noticia.findtext('source'))
    