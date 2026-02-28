#  __  .__   __. ____    ____  __       _______. _______ .______    __      
# |  | |  \ |  | \   \  /   / |  |     /       ||   ____||   _  \  |  |     
# |  | |   \|  |  \   \/   /  |  |    |   (----`|  |__   |  |_)  | |  |     
# |  | |  . `  |   \      /   |  |     \   \    |   __|  |   _  <  |  |     
# |  | |  |\   |    \    /    |  | .----)   |   |  |____ |  |_)  | |  `----.
# |__| |__| \__|     \__/     |__| |_______/    |_______||______/  |_______|
#                                                                           
#  _______         _______.  ______ .______          ___      .______       
# |   ____|       /       | /      ||   _  \        /   \     |   _  \      
# |  |__         |   (----`|  ,----'|  |_)  |      /  ^  \    |  |_)  |     
# |   __|         \   \    |  |     |      /      /  /_\  \   |   ___/      
# |  |____    .----)   |   |  `----.|  |\  \----./  _____  \  |  |          
# |_______|   |_______/     \______|| _| `._____/__/     \__\ | _|          
#                                                                           
# .___  ___.   ______   ____    ____  __   _______     _______.             
# |   \/   |  /  __  \  \   \  /   / |  | |   ____|   /       |             
# |  \  /  | |  |  |  |  \   \/   /  |  | |  |__     |   (----`             
# |  |\/|  | |  |  |  |   \      /   |  | |   __|     \   \                 
# |  |  |  | |  `--'  |    \    /    |  | |  |____.----)   |                
# |__|  |__|  \______/      \__/     |__| |_______|_______/                 
#
# Versão:1.0
# Data: 27/02/2026
# Autor: Yuri Melito Fernandes
#
import requests
import pandas as pd
import time
import random 
import sqlite3
from bs4 import BeautilfulSoup
import datetime
from config import *


for pagina in range(1, paginasLimite + 1): 
# "paginaLimite '+ 1' para a pagina não desconfiar do bot"
    url = f"{baseURL}?page={pagina}"
    print(f'Colentando dados da pagina {pagina} \n URL: {url}')
    resposta = requests.get(url, headers = headers)

    if resposta.status_code != 200:
        print(f'Erro ao carregar a pagina {pagina}. Codigo do erro é: {resposta.status_code}')

    soup = BeautilfulSoup(resposta.text, "html.parser")
    cards = soup.find_all("div", class_= "card entity-card entity-card-list cf")

    for card in cards:
        try:
            # tentar capturar o titulo do filme e o hiperlink da pagina do filme
            titulo_tag = card.find('a', class_="meta-title-link")
            titulo = titulo_tag.text.strip() if titulo_tag else "N/A"
            link = "https://www.adorocinema.com/filmes/" + titulo_tag['href'] if titulo_tag else None 

            # capturar a nota do filme
            nota_tag = card.find("span", class_="stareval-note")
            nota = nota_tag.text.strip().replace(",",".")  if nota_tag else "N/A"

            if link: 
                filme_resposta = requests.get(link, headers=headers)

                if filme_resposta.status_code == 200:
                    filme_soup = BeautilfulSoup(filme_resposta.text, "html.parser")

                diretor_tag = filme_soup.find("div", class_="meta-body-item meta-body-direction meta-body-online")
                if diretor_tag:
                    diretor = (
                        diretor_tag.text
                        .strip()
                        .replace('Direção','')
                        .replace(',','')
                        .replace('|','')
                        .replace('\n','')
                        .replace('\r','')
                    )
                    genero_block = filme_soup.find('div', class_='meta-body-info')
            if genero_block:
                genero_link = genero_block. find_all('a')
                generos = [g.text.strip() for g in genero_link]
                categoria = ", ".join(generos[:3] if generos else "N/A")
            else:
                categoria = "N/A" 

        except Exception as erro:
            print(f"Erro ao processar o filme {titulo}. Erro: {erro}")