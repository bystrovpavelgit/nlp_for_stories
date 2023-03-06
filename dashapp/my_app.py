import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

app = dash.Dash()

# data frame
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Mon", "Mon", "Mon"]
})

fig_names = ['fig1', 'fig2']
fig_dropdown = html.Div([
    dcc.Dropdown(
        id='fig_dropdown',
        options=[{'label': x, 'value': x} for x in fig_names],
        value=None
    )])
fig_plot = html.Div(id='fig_plot')
app.layout = html.Div([fig_dropdown, fig_plot])

@app.callback(
dash.dependencies.Output('fig_plot', 'children'),
[dash.dependencies.Input('fig_dropdown', 'value')])
def update_output(fig_name):
    return name_to_figure(fig_name, df)

def name_to_figure(fig_name, df):
    if fig_name == 'fig1':
        figure = px.scatter(y=[4, 2, 1])
    else: 
        figure = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
    return dcc.Graph(figure=figure)

app.run_server(debug=True, use_reloader=False)


