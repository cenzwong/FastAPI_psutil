# gunicorn -w 1 -b 0.0.0.0:8087 main:server --chdir ./app
# worker must be one

import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque

import requests

X = deque(maxlen=20)
X.append(1)
Y = deque(maxlen=20)
Y.append(1)


app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(children=[
    html.H1('Hello GL200'),

    html.Div(
    [
        dcc.Input(id="address", type="text", placeholder="address"),
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=1*1000,
            n_intervals=0
        ),
    ]
    )

])



@app.callback(Output('live-graph', 'figure'),
              [Input('graph-update', 'n_intervals'), Input('address', 'value')])
def update_graph_scatter(input_data, in_address):
    in_address = "172.16.10.250:8000" if in_address == None else in_address
    X.append(X[-1]+1)
    Y.append(float(requests.get("http://"+in_address+"/api/built-in/psutil/CPU/cpu_percent?percpu=false").text))
    # Y.append(random.random())

    data = plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y),
            name='Scatter',
            mode= 'lines+markers'
            )

    return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),
                                                yaxis=dict(range=[min(Y),max(Y)]), title="CPU_percentage")}


if __name__ == '__main__':
    # app.run_server(host='0.0.0.0', port=8082, debug=True)
    app.run_server(debug=True)
