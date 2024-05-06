# sistema fictício utilizado
# https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import pandas as pd
import time

pyautogui.PAUSE = 0.3

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)

# abrir o site do sistema da empresa
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)

# fazer o login
pyautogui.press("tab")
pyautogui.write("loginadmin123")
pyautogui.press("tab")
pyautogui.write("senhaadmin123")
pyautogui.press("enter")
time.sleep(2)

# abrir e importar a base de dados
tabela = pd.read_csv("produtos.csv")
# print(base_de_dados)

# cadastrar os produtos
for linha in tabela.index:
    # clicar no primeiro campo
    pyautogui.click(x=724, y=273)
    # inserir o campo de código a partir da tabela
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    # passar para o próximo campo
    pyautogui.press("tab")
    # inserir próximos campos
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # verificar se a linha possui uma observação
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    # enviar o formulário
    pyautogui.press("enter")
    # scrollar para cima e retomar o processo
    pyautogui.scroll(5000)
