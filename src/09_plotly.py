from dash import Dash,html,dcc,Output,Input
import pandas as pd
import plotly.express as px


df = pd.read_csv('data/08_with_iso.csv')


app = Dash()

app.layout = ([
    html.Div(children="Covid_19 map"),
    html.Hr(),

    dcc.RadioItems(options=['TotalCases', 'TotalDeaths', 'TotalRecovered'],
                value='TotalCases',
                id='controls_and_radio_item',
                inline=True,
                style = {
                         'left': '0%',        
                         'top': '90%',          
                        'font-size': '20px',  
                }
                ),

        dcc.Graph(id='controls_and_gragh', style={'margin-left':'50px','margin-top':'0px'}
                 )

])


def set_color(x):
    if x == 'TotalCases':
        return 'RdPu'
    if x == 'TotalDeaths':
        return 'OrRd'
    if x == 'TotalRecovered':
        return 'YlGn'


@app.callback(
    Output("controls_and_gragh", component_property= "figure"),
    Input("controls_and_radio_item", component_property= "value"))



def display_choropleth(col_chosen):

    fig = px.choropleth(
        df,
        locations='ISO3', 
        color=col_chosen,
        hover_name='Country',
        color_continuous_scale= set_color(col_chosen)
            
    )
    fig.update_layout(width=1200, height=800)
    fig.update_layout(
     title={
         'text': f"COVID-19 {col_chosen} by Country",
         'font': {'family': 'TimeNewRoman',
                 'color': 'black',
                 'size': 27
                 },
         'xanchor': 'left',
         'x': 0.3,    
         'y': 0.90,
        
            }
 )


    return fig

app.run(debug=True)
