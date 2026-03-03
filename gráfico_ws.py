import dash 
from dash import html
import pandas as pd 
import plotly.express as px
from config import *

df = pd.read_csv(saidaCSV, quotechar = "'")
df = df.sort_values(by= 'Nota', ascending= True)

fig = px.bar(
    df, 
    x = 'Nota',
    y = 'Titulo',
    orientation = 'h',
    labels = {'nota':'Nota do Filme', 'titulo': 'Titulo do Filme'},
    title = 'Notas dos Filmes'
)

app = dash.Dash()
app.layout = html.Div([
    html.H1("Gráfico de notas dos filmes", style = {'text-align':'center'}),
    html.Div([
        html.Iframe(
            srcDoc =fig.to_html(),
            width = '100%',
            heeight = '600px',
            style = {'border': 'none'}
        )
    ], style={'padding':'15px'})
])
if __name__ == '__main__':
    app.run(debug=True)