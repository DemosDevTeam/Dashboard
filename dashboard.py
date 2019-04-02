import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

import scipy
import pandas as pd

from helpers import *


# TODO: Read-in Mlab data
# Data Maniuplation
# Read in users and videos dataframes and select useful columns, dropping NA values
users = pd.read_csv('data/csv/users.csv', index_col=0)

users = (users[['age', 'children', 'education', 'gender',
                'income', 'marital', 'occupation', 'race']]).dropna()

videos = pd.read_csv('data/csv/videos.csv', index_col=0, encoding='latin1')

# Start Flask Application
server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server, external_stylesheets=[
                'https://codepen.io/chriddyp/pen/bWLwgP.css'])

_app_route = '/dash-core-components/logout_button'

# Create a login route
@app.server.route('/custom-auth/login', methods=['POST'])
def route_login():
    data = flask.request.form
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        flask.abort(401)
        
    # actual implementation should verify the password.
    # Recommended to only keep a hash in database and use something like
    # bcrypt to encrypt the password and check the hashed results.

    # Return a redirect with
    rep = flask.redirect(_app_route)
    
    # store username in a cookie
    # sign session with 
    rep.set_cookie('custom-auth-session', username)
    return rep 

# logout route 
@app.server.route('/custom-auth/logout', methods=['POST'])
def route_logout():
    rep = flask.redirect(_app_route)
    rep.set_cookie('custom-auth-session', '', expires=0)
    return rep

# login form dash component 
login_form = html.Div([
    html.Form([
        dcc.Input(placeholder='username', name='username'),
        dcc.Input(placeholder='password', name='password', type='password'),
        html.Button('Login', type='submit')
    ], action='/custom-auth/login', method='post')
])

#app.layout = html.Div(id='custom-auth-frame')

# @app.callback(Output('custom-auth-frame', 'children'),
#               [Input('custom-auth-frame', 'id')])
# def dynamic_layout(_):
#     session_cookie = flask.request.cookies.get('custom-auth-session')
#     if not session_cookie:
#         # If there's no cookie we need to login.
#         return login_form
#     return html.Div([
#         html.Div('Hello {}'.format(session_cookie)),
#         dcc.LogoutButton(logout_url='/custom-auth/logout')
#     ])


# Specify Dash Layout
app.layout = html.Div(
    children=[
        html.Div(id='custom-auth-frame'),
        html.Div(
            className='wrapper',
            children=[
                html.Div(
                    className='sidebar',
                    style={'data-color': 'red'},
                    children=[
                        html.Div(
                            className='logo',
                            children=[
                                html.A(
                                    'ACTA Solutions',
                                    className='simple-text logo-normal',
                                    style=dict(
                                        textAlign='center',
                                        color='#000000'),
                                    ),   
                                ]
                        ),
                        html.Div(
                            className='sidebar-wrapper',
                            children=[
                                html.Ul(
                                    className='nav',
                                    children=[
                                        html.Li(
                                            className='active',
                                            children=[
                                                html.A(
                                                    href="../examples/dashboard.html",
                                                    children=[
                                                        html.I(
                                                            className="now-ui-icons design_app"),
                                                        html.P("Dashboard")
                                                    ]
                                                )
                                            ]
                                        ),
                                        # html.Li(
                                        #     children=[
                                        #         html.A(
                                        #             href="../examples/icons.html",
                                        #             children=[
                                        #                 html.I(className="now-ui-icons education_atom"),
                                        #                 html.P("Icons")
                                        #             ]
                                        #         )
                                        #     ]
                                        # ),
                                        # html.Li(
                                        #     children=[
                                        #         html.A(
                                        #             href="../examples/map.html",
                                        #             children=[
                                        #                 html.I(className="now-ui-icons location_map-big"),
                                        #                 html.P("Maps")
                                        #             ]
                                        #         )
                                        #     ]
                                        # ),
                                        # html.Li(
                                        #     children=[
                                        #         html.A(
                                        #             href="../notifications.html",
                                        #             children=[
                                        #                 html.I(className="now-ui-icons ui-1_bell-53"),
                                        #                 html.P("Notifications")
                                        #             ]
                                        #         )
                                        #     ]
                                        # ),
                                        html.Li(
                                            children=[
                                                html.A(
                                                    href="../examples/user.html",
                                                    children=[
                                                        html.I(
                                                            className="now-ui-icons users_single-02"),
                                                        html.P("City Profile")
                                                    ]
                                                )
                                            ]
                                        ),
                                        html.Li(
                                            children=[
                                                html.A(
                                                    href="../examples/tables.html",
                                                    children=[
                                                        html.I(
                                                            className="now-ui-icons design_bullet-list-67"),
                                                        html.P("Data Summary")
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                        # html.A("test")
                    ],
                ),
                html.Div(
                    className='main-panel',
                    children=[
                        html.H1('Sample City Page',
                        style=dict(
                            textAlign='center',
                            color='#000000'),
                        ),
                        # TODO: Sentiment graph goes here
                        
                        # 3 Extra content plots
                        html.Div(
                            className='row',
                            children=[
                                    dcc.Graph(
                                        id='plot1',
                                        figure=generatePieChart(users, 'age')),
                                    dcc.Graph(
                                        id='plot2',
                                        figure=generatePieChart(users, 'race')),    
                                    dcc.Graph(
                                        id='plot3',
                                        figure=generatePieChart(users, 'income')
                                    )                                                                    
                                # html.Div(
                                #     className='col-lg-4',
                                #     children=[
                                #         html.Div(
                                #             className='card card-chart',
                                #             children=[
                                #                 html.Div(
                                #                     className='card-header',
                                #                     children=[
                                #                         html.H5('Type1'),
                                #                         html.H4('Plot1'),
                                #                     ]
                                #                 )
                                #             ]
                                #         )
                                #     ]
                                # ),
                        # html.Div(
                        #     className='col-lg-4',
                        #     children=[
                        #         html.Div(
                        #             className='card card-chart',
                        #             children=[
                        #                 html.Div(
                        #                     className='card-header',
                        #                     children=[
                        #                         html.H5(
                        #                             'Type2'),
                        #                         html.H4(
                        #                             'Plot2'),
                        #                         dcc.Graph(
                        #                             id='plot2',
                        #                             figure=generatePieChart(users, 'income')),
                        #                         html.Div()
                        #                         ]
                        #                     )
                        #                 ]
                        #             )
                        #         ]
                        #     ),
                        # html.Div(
                        #     className='col-lg-4',
                        #     children=[
                        #         html.Div(
                        #             className='card card-chart',
                        #             children=[
                        #                 html.Div(
                        #                     className='card-header',
                        #                     children=[
                        #                         html.H5(
                        #                             'Type3'),
                        #                         html.H4('Plot3'),
                        #                         dcc.Graph(
                        #                             id='plot3',
                        #                             figure=generatePieChart(users, 'race')),
                        #                         ]
                        #                     )
                        #                 ]
                        #             )
                        #         ]
                        #     ),
                        ]
                    ),

                    # User demographics Table
                    html.H4(
                        'User  Demographics',
                        style=dict(
                            textAlign='center'
                        )
                    ),
                    #generateChloropleth(),
                    generateUserTableSummary(users),

                    html.Br(),
                    dcc.Graph(id='plot4',
                        figure=(generateCategoricalPlot(20, 3))    
                    ),

                    dcc.Graph(id='plot5',
                        figure=generateLinePlot()
                    ),

                    dcc.Graph(id='plot6',
                        figure=generateBubbleChart()
                    ),

                    dcc.Graph(id='plot7',
                        figure=generateBoxPlot()    
                    ),

                    dcc.Graph(id='plot8',
                        figure=generatePopPyramid()    
                    ),

                    # dcc.Graph(id='plot8',
                    #     figure=generateDistplot()
                    # ),

                    dcc.RadioItems(
                        id='groupingDropdown',
                        options=[
                            {'label': 'Age', 'value': 'age'},
                            {'label': 'Children', 'value': 'children'},
                            {'label': 'Education', 'value': 'education'},
                            {'label': 'Gender', 'value': 'gender'},
                            {'label': 'Income', 'value': 'income'},
                            {'label': 'Marital', 'value': 'marital'},
                            {'label': 'Occupation', 'value': 'occupation'},
                            {'label': 'Race', 'value': 'race'}
                        ],
                        value='age',
                        labelStyle={
                            'display': 'inline-block',
                            'align-items': 'center',
                            #'justify-content': 'center'
                            }
                        ),
                    html.Br(),
                    dcc.Graph(id='mainBar'),

                    html.H4(
                        'Video Feedback',
                        style=dict(
                            textAlign='center'
                        )),


                    # TODO: Add video table summary
                    #generateVideoTableSummary(videos)
                    ]
                )
            ]
        ),
    ]
)

# Add Core JS Files
app.scripts.append_script({
    "external_url": "../assets/js/core/jquery.min.js",
    "external_url": "../assets/js/core/popper.min.js",
    "external_url": "../assets/js/core/bootstrap.min.js",
    "external_url": "../assets/js/plugins/perfect-scrollbar.jquery.min.js",
    "external_url": "../assets/js/plugins/chartjs.min.js",
    "external_url": "../assets/js/plugins/bootstrap-notify.js",
    "external_url": "../assets/js/now-ui-dashboard.js?v=1.0.1",
    "external_url" : """
        $(document).ready(function() {
        // Javascript method's body can be found in assets/js/demos.js

        demo.initDashboardPageCharts();});
        """
})  

@app.callback(Output('custom-auth-frame', 'children'),
              [Input('custom-auth-frame', 'id')])
def dynamic_layout(_):
    session_cookie = flask.request.cookies.get('custom-auth-session')
    if not session_cookie:
        # If there's no cookie we need to login.
        return login_form
    return html.Div([
        html.Div('Hello {}'.format(session_cookie)),
        dcc.LogoutButton(logout_url='/custom-auth/logout')
    ])
    
@app.callback(Output('mainBar', 'figure'),  
    [Input('groupingDropdown', 'value')])
def makeBarChart(value):
    uniqueUsers = pd.DataFrame(users.groupby(by=value).count())
    
    def titleSuffix(x):
        return {
            'age' : 'Age',
            'children' : 'Number of Children',
            'education' : 'Educational Attainment',
            'gender' : 'Gender',
            'income' : 'Income',
            'marital' : 'Marital Status',
            'occupation' : 'Occupation',
            'race' : 'Race'
        }[x]

    figure = go.Figure(
        data=[
            go.Bar(
                x=uniqueUsers.index.tolist(),
                y=uniqueUsers.iloc[:, 0].tolist(),
                marker=dict(
                    color='rgb(0,50,255)',
                    line=dict(
                        color='rgb(8,48,200)',
                        width=1.5
                        ),
                    ),
            )
        ],
        layout=go.Layout(
            title="Users Grouped by " + titleSuffix(value),
            font=dict(
                family='Times New Roman',
                size=22,
                color='#7f7f7f'),
            xaxis=dict(
                title='Category',
                titlefont=dict(
                    family='Times New Roman',
                    size=18
                )
            ),

            yaxis=dict(
                title='Count',
                titlefont=dict(
                    family='Times New Roman',
                    size=18,
                ),              
            )
        )
    )

    return figure


# Start Dash Application
if __name__ == '__main__':
    app.run_server(debug=True, port=8050, host='127.0.0.1')
    app.run_server(debug=True)
