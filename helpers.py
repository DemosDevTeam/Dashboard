import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

import plotly.graph_objs as go
import plotly.figure_factory as ff

import dash_table
import pandas as pd
import numpy as np
import scipy

def generateDistplot():
    x1 = np.random.randn(200) - 2 
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2 

    hist_data = [x1, x2, x3]

    group_labels = ['Group 1', 'Group 2', 'Group 3']
    colors = ['#A56CC1', '#A6ACEC', '#63F5EF']

    # Create distplot with curve_type set to 'normal'
    fig = ff.create_distplot(hist_data, group_labels, colors=colors,
                            bin_size=.2, show_rug=False)

    # Add title
    fig['layout'].update(title='Hist and Curve Plot')

    return fig

def generatePopPyramid():
    women_bins = np.array([-600, -623, -653, -650, -670, -578, -541, -411, -322, -230])
    men_bins = np.array([600, 623, 653, 650, 670, 578, 541, 360, 312, 170])

    y = list(range(0, 100, 10))

    layout = go.Layout(yaxis=go.layout.YAxis(title='Age'),
                    xaxis=go.layout.XAxis(
                        range=[-1200, 1200],
                        tickvals=[-1000, -700, -300, 0, 300, 700, 1000],
                        ticktext=[1000, 700, 300, 0, 300, 700, 1000],
                        title='Number'),
                    barmode='overlay',
                    bargap=0.1)

    data = [go.Bar(y=y,
                x=men_bins,
                orientation='h',
                name='Men',
                hoverinfo='x',
                marker=dict(color='powderblue')
                ),
            go.Bar(y=y,
                x=women_bins,
                orientation='h',
                name='Women',
                text=-1 * women_bins.astype('int'),
                hoverinfo='text',
                marker=dict(color='seagreen')
                )]

    figure = go.Figure(
        data=data,
        layout=layout
    )

    return figure
    

def generateBubbleChart():
    data = [
        {
        'x': [1, 3.2, 5.4, 7.6, 9.8, 12.5],
        'y': [1, 3.2, 5.4, 7.6, 9.8, 12.5],
        'mode': 'markers',
        'marker': {
            'color': [120, 125, 130, 135, 140, 145],
            'size': [15, 30, 55, 70, 90, 110],
            'showscale': True
            }
        }
    ]

    figure = go.Figure(
        data=data
    )

    return figure

def generateChloropleth():
    df_sample = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/laucnty16.csv')
    df_sample['State FIPS Code'] = df_sample['State FIPS Code'].apply(lambda x: str(x).zfill(2))
    df_sample['County FIPS Code'] = df_sample['County FIPS Code'].apply(lambda x: str(x).zfill(3))
    df_sample['FIPS'] = df_sample['State FIPS Code'] + df_sample['County FIPS Code']

    colorscale = ["#f7fbff","#ebf3fb","#deebf7","#d2e3f3","#c6dbef","#b3d2e9","#9ecae1",
                "#85bcdb","#6baed6","#57a0ce","#4292c6","#3082be","#2171b5","#1361a9",
                "#08519c","#0b4083","#08306b"]
    endpts = list(np.linspace(1, 12, len(colorscale) - 1))
    fips = df_sample['FIPS'].tolist()
    values = df_sample['Unemployment Rate (%)'].tolist()

    fig = ff.create_choropleth(
        fips=fips, values=values,
        binning_endpoints=endpts,
        colorscale=colorscale,
        show_state_data=False,
        show_hover=True, centroid_marker={'opacity': 0},
        asp=2.9, title='USA by Unemployment %',
        legend_title='% unemployed'
    )

    return fig


### Helper Functions for Plotting and generating Tables
def generateBoxPlot():
    N = 30.     # Number of boxes

    c = ['hsl('+str(h)+',50%'+',50%)' for h in np.linspace(0, 360, N)]

    data = [{
        'y': 3.5*np.sin(np.pi * i/N) + i/N+(1.5+0.5*np.cos(np.pi*i/N))*np.random.rand(10), 
        'type':'box',
        'marker':{'color': c[i]}
        } for i in range(int(N))]

    # format the layout
    layout = {'xaxis': {'showgrid':False,'zeroline':False, 'tickangle':60,'showticklabels':False},
            'yaxis': {'zeroline':False,'gridcolor':'white'},
            'paper_bgcolor': 'rgb(233,233,233)',
            'plot_bgcolor': 'rgb(233,233,233)',
            }
    
    figure = go.Figure(
        data=data,
        layout=layout
    )

    return figure

# Generate violin data plot
def generateCategoricalPlot(N, numCats):

    randX = np.linspace(0, 1, numCats)
    data = []

    for i in range(0, 1): 
        trace = {
            "type": "violin",
            "x" : randX,
            #"y" : np.random.multinomial(N, [1/numCats]*numCats, size=1),
            "y" : np.random.randn(N) + (.5 * i),
            "name" : "Category " + str(i), 
            "box" : {
                "visible" : True
            },
            "meanline" : {
                "visible" : True
            }
        } 

        data.append(trace) 

    figure = go.Figure(
        data=data,
        layout= dict(
            title="", 
            yaxis=dict(
                zeroline=False
            )
        )
    )

    return figure



# Generate general line plot (with random data)
def generateLinePlot():
    N = 200
    randX = np.linspace(0, 1, N)

    randY1 = np.random.randn(N) + 5
    randY2 = np.random.randn(N) + 10 
    randY3 = np.random.randn(N) + 15

    title = 'Sentiment over Time'

    trace1 = go.Scatter(
        x=randX,
        y=randY1,
        name='Policy One'
    )

    trace2 = go.Scatter(
        x=randX,
        y=randY2,
        name='Policy Two'
    )

    trace3 = go.Scatter(
        x=randX,
        y=randY3,
        name='Policy Three'
    )

    data = [trace1, trace2, trace3]

    figure = go.Figure(
        data=data
    )

    return figure




# Generate general piechart

def generatePieChart(dataframe, group):
    uniqueUsers = pd.DataFrame(dataframe.groupby(by=group).count())

    labels = uniqueUsers.index.tolist()
    values = uniqueUsers.iloc[:, 0].tolist()

    figure = go.Figure(
        data=[
            go.Pie(
            labels=labels,
            values=values,
            domain= dict(
                x=[0, 1],
                y=[0, 1]
                ),
            )
        ],
        layout=dict(
            title='Citizen Percentage by ' + group.capitalize(),
            font=dict(
                family='Times New Roman',
                size=15,
                color='#7f7f7f'),        
            autosize=False,
            height=350,
            width=500,
            legend=dict(
                #x=-0,
                # y=0,
                orientation='h',
                xanchor='center',
                #yanchor='bottom'
                
            ),
            yaxis=dict(
                title='Count',
                titlefont=dict(
                family='Times New Roman',
                    size=18
                    ),
                #linecolor='black',
                mirror=True,
                ticks='outside',
                showline=True,  
                ),
            xaxis=dict(
                #linecolor='black',
                mirror=True,
                ticks='outside',
                showline=True,  
            )
        )

    )

    return figure 


# Generate HTML for the Users dataset 
def generateUserTableSummary(dataframe):
    table = dash_table.DataTable(
        data=dataframe.to_dict("rows"),
        id='userTable',
        columns=[{"name": i, "id": i} for i in dataframe.columns],
        style_as_list_view=True,
        style_cell={
            'padding': '5px'
            },
        style_header={
            'backgroundColor': 'white',
            'fontWeight': 'bold'
        },
        style_cell_conditional=[{
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(248, 248, 248)'
        }]
    )

    return table

# Generate HTML for the Videos dataset
# TODO: Fix
def generateVideoTableSummary(dataframe, max_rows=10):
    dataframe = pd.DataFrame(dataframe.items())
    table = dash_table.DataTable(
        data=dataframe.to_dict("rows"),
        id='videoTable',
        columns=[{"name": i, "id": i} for i in dataframe.columns],
        style_as_list_view=True,
        style_cell={
            'padding': '5px'
            },
        style_header={
            'backgroundColor': 'white',
            'fontWeight': 'bold'
        },
        style_cell_conditional=[{
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(248, 248, 248)'
        }]
    )

    return table   