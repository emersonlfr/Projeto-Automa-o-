# Passo a passo do projeto
# Passo 1: entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pip install pyautogui
import pyautogui
import time

pyautogui.PAUSE = 1

# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar 1 tecla do teclado

# pyautogui.hotkey = combinacação de teclas
# https://pyautogui.readthedocs.io/en/latest/

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# pausa um pouco maior por conta da conexão
time.sleep(3)

# Passo 2: fazer login
pyautogui.click(x=673, y=404)
pyautogui.write("emailaleatorio@gmail.com")

# escrever senha
pyautogui.press("tab")
pyautogui.write("senha123")
pyautogui.click(x=798, y=573)
time.sleep(3)

# Passo 3: importar base de dados
# pip instalss pandas numpy openpyxl
import pandas # usado para dados
tabela = pandas.read_csv("produtos.csv") # csv arquivo separado por virgulas

print(tabela)

# Passo 4: cadastrar 1 produto
for linha in tabela.index:
    pyautogui.click(x=778, y=301)
    # produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    # preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")
    # enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)

# Passo 5: repetir o processo de cadastro até acabar a base de dados