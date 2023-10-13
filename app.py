from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

# acessar o site desejado
# https://www.amazon.com.br/hz/wishlist/ls/W27T8V17NR1Q?ref_=wl_share
driver = webdriver.Chrome()
driver.get("https://www.inpower.com.br/pesquisa?t=notebook+gamer#/marca-acer")

# Para deixar o site aberto
# input() 

# Localização da informação na página
# tag a // class a-link-normal
# formato: //tag[@atributo='valorDoAtributo']

# Localiza o título do livros
titulos = driver.find_elements(By.XPATH, "//h3[@class='name']")

# for titulo in titulos:
#     print(titulo.text)

# Localiza o preço do livros
precos = driver.find_elements(By.XPATH, "//span[@class='instant-price']") 
# for preco in precos:
#     print(preco.text)

# cria a planilha do excel
planilha = openpyxl.Workbook()

# cria a página/aba no excel
planilha.create_sheet('planilha-produtos')

# seleciona a aba
planilha_produtos = planilha['planilha-produtos']

# cria as colunas
planilha_produtos['A1'].value = 'Título'
planilha_produtos['B1'].value = 'Preço'

# insere as informações na planilha
for titulo, preco in zip(titulos, precos):
    planilha_produtos.append([titulo.text, preco.text])

#salva e nomeia a planilha
planilha.save('planilha-produtos.xlsx')