import datetime


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chorome/114.0 Safari/537.36'
}
baseURL = "https://www.adorocinema.com/filmes/melhores/"
filmes = []
data_hoje = datetime.date.today().strftime("%d-%m-%Y")
inicio = datetime.datetime.now()
card_temp_min = 1
card_temp_max = 3
pag_temp_min = 2
pag_temp_max = 4
paginasLimite = 5 
bancoDados = "filmes.db"
saidaCSV = f"filmes_adorocinema_{data_hoje}.csv"