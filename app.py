# Run this app with `python app.py` 

import numpy as np
import pandas as pd 
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output




external_stylesheets = ['https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div(style={'backgroundColor': "color"},children=[
    


                    html.H1(children='Tableau de bord "Prêt à depenser" '),
                    html.Label(['Choisissez un client:'],style={'font-weight': 'bold', "text-align": "left"}),
    
                   

])


        
#app.run_server(mode='external',debug=True, use_reloader=False)        
#app.run_server(mode='inline', port=8069)

if __name__ == '__main__':
    app.run_server(debug=True)