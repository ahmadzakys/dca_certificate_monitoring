######-----Import Dash-----#####
import dash
from dash import dcc
from dash import html, callback, dash_table
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import pandas as pd
import numpy as np

from datetime import date
from dateutil.relativedelta import relativedelta

import plotly.graph_objects as go

dash.register_page(__name__, name='Graphs') # '/' is home page

##-----page 3

## -----LAYOUT-----
layout = html.Div([
                html.Br(),
                        html.P(children=html.Strong('MONITORING CERTIFICATE'),
                               style={'textAlign': 'center', 'fontSize': 27, 'background-color':'#F1F4F4','color':'#242947','font-family':'Verdana'}),
                dcc.Tabs([
                    ##### TAB BARGE
                    dcc.Tab(label='Tug Boat', children=[
                        html.Br(),
                
                        ## --ROW1--
                        dbc.Row([
                            dbc.Col([
                                html.Br(),
                                html.P(children=[html.Strong('NAT & TONNAGE')], 
                                    style={'textAlign': 'center', 'fontSize': 22, 'background-color':'#F1F4F4','color':'#2a3f5f','font-family':'Verdana'}),

                                dbc.Row([###### NAT & TONNAGE Summary
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Summary')],
                                                                style={'textAlign': 'center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-info-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-secondary',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=5),
                                    ###### NAT & TONNAGE Alerts
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Alerts')],
                                                                style={'textAlign': 'Center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-exclamation-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-warning',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center"),

                                dbc.Row([
                                    ###### NAT & TONNAGE Bar Plot
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(dcc.Graph(id='nat&tonnage_tb_bar'))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=5),
                                    ###### NAT & TONNAGE Alerts Table
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(html.Div(dash_table.DataTable(id="data_nat&tonnage_tb_alerts",
                                                                                    columns=[{'name':'Vessel','id': 'Vessel'},
                                                                                                {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                                    style_as_list_view=True,
                                                                                    style_header={'backgroundColor': 'white',
                                                                                                    'fontWeight': 'bold'
                                                                                                },
                                                                                    style_cell_conditional=[{'if': {'column_id': 'Vessel'},
                                                                                                                'width': '30%'},
                                                                                                                {'if': {'column_id': 'Remaining Days'},
                                                                                                                'width': '70%'},
                                                                                                                {'textAlign': 'center'}
                                                                                                            ],
                                                                                    style_cell={'font-family':'Verdana',
                                                                                                'fontSize': 13,
                                                                                                'color':'#2a3f5f',},
                                                                                    css=[{
                                                                                        'selector': '.dash-table-tooltip',
                                                                                        'rule': 'background-color: grey; font-family: monospace; color: white',
                                                                                        #    'rule': 'background-color: white; font-family: monospace; color: #2a3f5f;',
                                                                                        }],
                                                                                    tooltip_delay=0,
                                                                                    tooltip_duration=None
                                                                                    )))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center")
                            ], xs=4),

                            dbc.Col([
                                html.Br(),
                                html.P(children=[html.Strong('SOLAS')], 
                                    style={'textAlign': 'center', 'fontSize': 22, 'background-color':'#F1F4F4','color':'#2a3f5f','font-family':'Verdana'}),

                                dbc.Row([###### SOLAS Summary
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Summary')],
                                                                style={'textAlign': 'center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-info-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-secondary',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=5),
                                    ###### SOLAS Alerts
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Alerts')],
                                                                style={'textAlign': 'Center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-exclamation-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-warning',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center"),

                                dbc.Row([
                                    ###### SOLAS Bar Plot
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(dcc.Graph(id='solas_tb_bar'))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=5),
                                    ###### SOLAS Alerts Table
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(html.Div(dash_table.DataTable(id="data_solas_tb_alerts",
                                                                                    columns=[{'name':'Vessel','id': 'Vessel'},
                                                                                                {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                                    style_as_list_view=True,
                                                                                    style_header={'backgroundColor': 'white',
                                                                                                    'fontWeight': 'bold'
                                                                                                },
                                                                                    style_cell_conditional=[{'if': {'column_id': 'Vessel'},
                                                                                                                'width': '30%'},
                                                                                                                {'if': {'column_id': 'Remaining Days'},
                                                                                                                'width': '70%'},
                                                                                                                {'textAlign': 'center'}
                                                                                                            ],
                                                                                    style_cell={'font-family':'Verdana',
                                                                                                'fontSize': 13,
                                                                                                'color':'#2a3f5f',},
                                                                                    css=[{
                                                                                        'selector': '.dash-table-tooltip',
                                                                                        'rule': 'background-color: white; font-family: Verdana; color: #2a3f5f;'}],
                                                                                    tooltip_delay=0,
                                                                                    tooltip_duration=None
                                                                                    )))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center")
                            ], xs=4),                    

                            dbc.Col([
                                html.Br(),
                                html.P(children=[html.Strong('POLLUTION')], 
                                    style={'textAlign': 'center', 'fontSize': 22, 'background-color':'#F1F4F4','color':'#2a3f5f','font-family':'Verdana'}),

                                dbc.Row([###### POLLUTION Summary
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Summary')],
                                                                style={'textAlign': 'center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-info-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-secondary',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=5),
                                    ###### POLLUTION Alerts
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Alerts')],
                                                                style={'textAlign': 'Center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-exclamation-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-warning',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center"),

                                dbc.Row([
                                    ###### POLLUTION Bar Plot
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(dcc.Graph(id='pollution_tb_bar'))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=5),
                                    ###### POLLUTION Alerts Table
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(html.Div(dash_table.DataTable(id="data_pollution_tb_alerts",
                                                                                    columns=[{'name':'Vessel','id': 'Vessel'},
                                                                                                {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                                    style_as_list_view=True,
                                                                                    style_header={'backgroundColor': 'white',
                                                                                                    'fontWeight': 'bold'
                                                                                                },
                                                                                    style_cell_conditional=[{'if': {'column_id': 'Vessel'},
                                                                                                                'width': '30%'},
                                                                                                                {'if': {'column_id': 'Remaining Days'},
                                                                                                                'width': '70%'},
                                                                                                                {'textAlign': 'center'}
                                                                                                            ],
                                                                                    style_cell={'font-family':'Verdana',
                                                                                                'fontSize': 13,
                                                                                                'color':'#2a3f5f',},
                                                                                    css=[{
                                                                                        'selector': '.dash-table-tooltip',
                                                                                        'rule': 'background-color: white; font-family: Verdana; color: #2a3f5f;'}],
                                                                                    tooltip_delay=0,
                                                                                    tooltip_duration=None
                                                                                    )))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center")
                            ], xs=4),
                        ]),

                        ## --ROW2--
                        dbc.Row([
                            dbc.Col([
                                html.Br(),
                                html.P(children=[html.Strong('CLASS')], 
                                    style={'textAlign': 'center', 'fontSize': 22, 'background-color':'#F1F4F4','color':'#2a3f5f','font-family':'Verdana'}),

                                dbc.Row([###### CLASS Summary
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Summary')],
                                                                style={'textAlign': 'center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-info-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-secondary',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=5),
                                    ###### CLASS Alerts
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Alerts')],
                                                                style={'textAlign': 'Center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-exclamation-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-warning',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center"),

                                dbc.Row([
                                    ###### CLASS Bar Plot
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(dcc.Graph(id='class_tb_bar'))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=5),
                                    ###### CLASS Alerts Table
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(html.Div(dash_table.DataTable(id="data_class_tb_alerts",
                                                                                    columns=[{'name':'Vessel','id': 'Vessel'},
                                                                                                {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                                    style_as_list_view=True,
                                                                                    style_header={'backgroundColor': 'white',
                                                                                                    'fontWeight': 'bold'
                                                                                                },
                                                                                    style_cell_conditional=[{'if': {'column_id': 'Vessel'},
                                                                                                                'width': '30%'},
                                                                                                                {'if': {'column_id': 'Remaining Days'},
                                                                                                                'width': '70%'},
                                                                                                                {'textAlign': 'center'}
                                                                                                            ],
                                                                                    style_cell={'font-family':'Verdana',
                                                                                                'fontSize': 13,
                                                                                                'color':'#2a3f5f',},
                                                                                    css=[{
                                                                                        'selector': '.dash-table-tooltip',
                                                                                        'rule': 'background-color: white; font-family: Verdana; color: #2a3f5f;'}],
                                                                                    tooltip_delay=0,
                                                                                    tooltip_duration=None
                                                                                    )))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center")
                            ], xs=4),

                            dbc.Col([
                                html.Br(),
                                html.P(children=[html.Strong('INSURANCE')], 
                                    style={'textAlign': 'center', 'fontSize': 22, 'background-color':'#F1F4F4','color':'#2a3f5f','font-family':'Verdana'}),

                                dbc.Row([###### INSURANCE Summary
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Summary')],
                                                                style={'textAlign': 'center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-info-square', style={
                                                                                        "color": "#F1F4F4",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-secondary',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=5),
                                    ###### INSURANCE Alerts
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Alerts')],
                                                                style={'textAlign': 'Center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-exclamation-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-warning',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center"),

                                dbc.Row([
                                    ###### INSURANCE Bar Plot
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(dcc.Graph(id='insurance_tb_bar'))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=5),
                                    ###### INSURANCE Alerts Table
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(html.Div(dash_table.DataTable(id="data_insurance_tb_alerts",
                                                                                    columns=[{'name':'Vessel','id': 'Vessel'},
                                                                                                {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                                    style_as_list_view=True,
                                                                                    style_header={'backgroundColor': 'white',
                                                                                                    'fontWeight': 'bold'
                                                                                                },
                                                                                    style_cell_conditional=[{'if': {'column_id': 'Vessel'},
                                                                                                                'width': '30%'},
                                                                                                                {'if': {'column_id': 'Remaining Days'},
                                                                                                                'width': '70%'},
                                                                                                                {'textAlign': 'center'}
                                                                                                            ],
                                                                                    style_cell={'font-family':'Verdana',
                                                                                                'fontSize': 13,
                                                                                                'color':'#2a3f5f',},
                                                                                    css=[{
                                                                                        'selector': '.dash-table-tooltip',
                                                                                        'rule': 'background-color: white; font-family: Verdana; color: #2a3f5f;'}],
                                                                                    tooltip_delay=0,
                                                                                    tooltip_duration=None
                                                                                    )))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center")
                            ], xs=4),

                            dbc.Col([
                                html.Br(),
                                html.P(children=[html.Strong('LSA & FFA')], 
                                    style={'textAlign': 'center', 'fontSize': 22, 'background-color':'#F1F4F4','color':'#2a3f5f','font-family':'Verdana'}),

                                dbc.Row([###### LSA & FFA Summary
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Summary')],
                                                                style={'textAlign': 'center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-info-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-secondary',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=5),
                                    ###### LSA & FFA Alerts
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Alerts')],
                                                                style={'textAlign': 'Center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-exclamation-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-warning',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center"),

                                dbc.Row([
                                    ###### LSA & FFA Bar Plot
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(dcc.Graph(id='lsa&fa_tb_bar'))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=5),
                                    ###### LSA & FFA Alerts Table
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(html.Div(dash_table.DataTable(id="data_lsa&fa_tb_alerts",
                                                                                    columns=[{'name':'Vessel','id': 'Vessel'},
                                                                                                {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                                    style_as_list_view=True,
                                                                                    style_header={'backgroundColor': 'white',
                                                                                                    'fontWeight': 'bold'
                                                                                                },
                                                                                    style_cell_conditional=[{'if': {'column_id': 'Vessel'},
                                                                                                                'width': '30%'},
                                                                                                                {'if': {'column_id': 'Remaining Days'},
                                                                                                                'width': '70%'},
                                                                                                                {'textAlign': 'center'}
                                                                                                            ],
                                                                                    style_cell={'font-family':'Verdana',
                                                                                                'fontSize': 13,
                                                                                                'color':'#2a3f5f',},
                                                                                    css=[{
                                                                                        'selector': '.dash-table-tooltip',
                                                                                        'rule': 'background-color: white; font-family: Verdana; color: #2a3f5f;'}],
                                                                                    tooltip_delay=0,
                                                                                    tooltip_duration=None
                                                                                    )))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center")
                            ], xs=4),
                        ]),

                        ## --ROW3--
                        dbc.Row([
                            dbc.Col([
                                html.Br(),
                                html.P(children=[html.Strong('HEALTH')], 
                                    style={'textAlign': 'center', 'fontSize': 22, 'background-color':'#F1F4F4','color':'#2a3f5f','font-family':'Verdana'}),

                                dbc.Row([###### HEALTH Summary
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Summary')],
                                                                style={'textAlign': 'center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-info-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-secondary',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=5),
                                    ###### HEALTH Alerts
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Alerts')],
                                                                style={'textAlign': 'Center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-exclamation-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-warning',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center"),

                                dbc.Row([
                                    ###### HEALTH Plot
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(dcc.Graph(id='health_tb_bar'))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=5),
                                    ###### HEALTH Table
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(html.Div(dash_table.DataTable(id="data_health_tb_alerts",
                                                                                    columns=[{'name':'Vessel','id': 'Vessel'},
                                                                                                {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                                    style_as_list_view=True,
                                                                                    style_header={'backgroundColor': 'white',
                                                                                                    'fontWeight': 'bold'
                                                                                                },
                                                                                    style_cell_conditional=[{'if': {'column_id': 'Vessel'},
                                                                                                                'width': '30%'},
                                                                                                                {'if': {'column_id': 'Remaining Days'},
                                                                                                                'width': '70%'},
                                                                                                                {'textAlign': 'center'}
                                                                                                            ],
                                                                                    style_cell={'font-family':'Verdana',
                                                                                                'fontSize': 13,
                                                                                                'color':'#2a3f5f',},
                                                                                    css=[{
                                                                                        'selector': '.dash-table-tooltip',
                                                                                        'rule': 'background-color: white; font-family: Verdana; color: #2a3f5f;'}],
                                                                                    tooltip_delay=0,
                                                                                    tooltip_duration=None
                                                                                    )))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center")
                            ], xs=4),

                            dbc.Col([
                                html.Br(),
                                html.P(children=[html.Strong('OTHERS')], 
                                    style={'textAlign': 'center', 'fontSize': 22, 'background-color':'#F1F4F4','color':'#2a3f5f','font-family':'Verdana'}),

                                dbc.Row([###### OTHERS Summary
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Summary')],
                                                                style={'textAlign': 'center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-info-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-secondary',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=5),
                                    ###### OTHERS Alerts
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Alerts')],
                                                                style={'textAlign': 'Center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-exclamation-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-warning',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center"),

                                dbc.Row([
                                    ###### OTHERS Plot
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(dcc.Graph(id='others_tb_bar'))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=5),
                                    ###### OTHERS Alerts Table
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(html.Div(dash_table.DataTable(id="data_others_tb_alerts",
                                                                                    columns=[{'name':'Vessel','id': 'Vessel'},
                                                                                                {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                                    style_as_list_view=True,
                                                                                    style_header={'backgroundColor': 'white',
                                                                                                    'fontWeight': 'bold'
                                                                                                },
                                                                                    style_cell_conditional=[{'if': {'column_id': 'Vessel'},
                                                                                                                'width': '30%'},
                                                                                                                {'if': {'column_id': 'Remaining Days'},
                                                                                                                'width': '70%'},
                                                                                                                {'textAlign': 'center'}
                                                                                                            ],
                                                                                    style_cell={'font-family':'Verdana',
                                                                                                'fontSize': 13,
                                                                                                'color':'#2a3f5f',},
                                                                                    page_action="native",
                                                                                    page_current= 0,
                                                                                    page_size= 4,
                                                                                    css=[{
                                                                                        'selector': '.dash-table-tooltip',
                                                                                        'rule': 'background-color: white; font-family: Verdana; color: #2a3f5f;'}],
                                                                                    tooltip_delay=0,
                                                                                    tooltip_duration=None
                                                                                    )))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center")
                            ], xs=4),
                        ]),
                    ]),

                    ##### TAB BARGE
                    dcc.Tab(label='Barge', children=[
                        html.Br(),
                        ## --ROW1--
                        dbc.Row([
                            dbc.Col([
                                html.Br(),
                                html.P(children=[html.Strong('NAT & TONNAGE')], 
                                    style={'textAlign': 'center', 'fontSize': 22, 'background-color':'#F1F4F4','color':'#2a3f5f','font-family':'Verdana'}),

                                dbc.Row([###### NAT & TONNAGE Summary
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Summary')],
                                                                style={'textAlign': 'center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-info-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-secondary',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=5),
                                    ###### NAT & TONNAGE Alerts
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Alerts')],
                                                                style={'textAlign': 'Center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-exclamation-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-warning',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center"),

                                dbc.Row([
                                    ###### NAT & TONNAGE Bar Plot
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(dcc.Graph(id='nat&tonnage_ba_bar'))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=5),
                                    ###### NAT & TONNAGE Alerts Table
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(html.Div(dash_table.DataTable(id="data_nat&tonnage_ba_alerts",
                                                                                    columns=[{'name':'Vessel','id': 'Vessel'},
                                                                                                {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                                    style_as_list_view=True,
                                                                                    style_header={'backgroundColor': 'white',
                                                                                                    'fontWeight': 'bold'
                                                                                                },
                                                                                    style_cell_conditional=[{'if': {'column_id': 'Vessel'},
                                                                                                                'width': '30%'},
                                                                                                                {'if': {'column_id': 'Remaining Days'},
                                                                                                                'width': '70%'},
                                                                                                                {'textAlign': 'center'}
                                                                                                            ],
                                                                                    style_cell={'font-family':'Verdana',
                                                                                                'fontSize': 13,
                                                                                                'color':'#2a3f5f',},
                                                                                    css=[{
                                                                                        'selector': '.dash-table-tooltip',
                                                                                        'rule': 'background-color: grey; font-family: monospace; color: white',
                                                                                        #    'rule': 'background-color: white; font-family: monospace; color: #2a3f5f;',
                                                                                        }],
                                                                                    tooltip_delay=0,
                                                                                    tooltip_duration=None
                                                                                    )))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center")
                            ], xs=4),

                            dbc.Col([
                                html.Br(),
                                html.P(children=[html.Strong('SOLAS')], 
                                    style={'textAlign': 'center', 'fontSize': 22, 'background-color':'#F1F4F4','color':'#2a3f5f','font-family':'Verdana'}),

                                dbc.Row([###### SOLAS Summary
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Summary')],
                                                                style={'textAlign': 'center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-info-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-secondary',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=5),
                                    ###### SOLAS Alerts
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Alerts')],
                                                                style={'textAlign': 'Center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-exclamation-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-warning',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center"),

                                dbc.Row([
                                    ###### SOLAS Bar Plot
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(dcc.Graph(id='solas_ba_bar'))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=5),
                                    ###### SOLAS Alerts Table
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(html.Div(dash_table.DataTable(id="data_solas_ba_alerts",
                                                                                    columns=[{'name':'Vessel','id': 'Vessel'},
                                                                                                {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                                    style_as_list_view=True,
                                                                                    style_header={'backgroundColor': 'white',
                                                                                                    'fontWeight': 'bold'
                                                                                                },
                                                                                    style_cell_conditional=[{'if': {'column_id': 'Vessel'},
                                                                                                                'width': '30%'},
                                                                                                                {'if': {'column_id': 'Remaining Days'},
                                                                                                                'width': '70%'},
                                                                                                                {'textAlign': 'center'}
                                                                                                            ],
                                                                                    style_cell={'font-family':'Verdana',
                                                                                                'fontSize': 13,
                                                                                                'color':'#2a3f5f',},
                                                                                    css=[{
                                                                                        'selector': '.dash-table-tooltip',
                                                                                        'rule': 'background-color: white; font-family: Verdana; color: #2a3f5f;'}],
                                                                                    tooltip_delay=0,
                                                                                    tooltip_duration=None
                                                                                    )))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center")
                            ], xs=4),   

                            dbc.Col([
                                html.Br(),
                                html.P(children=[html.Strong('CLASS')], 
                                    style={'textAlign': 'center', 'fontSize': 22, 'background-color':'#F1F4F4','color':'#2a3f5f','font-family':'Verdana'}),

                                dbc.Row([###### CLASS Summary
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Summary')],
                                                                style={'textAlign': 'center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-info-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-secondary',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=5),
                                    ###### CLASS Alerts
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Alerts')],
                                                                style={'textAlign': 'Center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-exclamation-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-warning',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center"),

                                dbc.Row([
                                    ###### CLASS Bar Plot
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(dcc.Graph(id='class_ba_bar'))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=5),
                                    ###### CLASS Alerts Table
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(html.Div(dash_table.DataTable(id="data_class_ba_alerts",
                                                                                    columns=[{'name':'Vessel','id': 'Vessel'},
                                                                                                {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                                    style_as_list_view=True,
                                                                                    style_header={'backgroundColor': 'white',
                                                                                                    'fontWeight': 'bold'
                                                                                                },
                                                                                    style_cell_conditional=[{'if': {'column_id': 'Vessel'},
                                                                                                                'width': '30%'},
                                                                                                                {'if': {'column_id': 'Remaining Days'},
                                                                                                                'width': '70%'},
                                                                                                                {'textAlign': 'center'}
                                                                                                            ],
                                                                                    style_cell={'font-family':'Verdana',
                                                                                                'fontSize': 13,
                                                                                                'color':'#2a3f5f',},
                                                                                    css=[{
                                                                                        'selector': '.dash-table-tooltip',
                                                                                        'rule': 'background-color: white; font-family: Verdana; color: #2a3f5f;'}],
                                                                                    tooltip_delay=0,
                                                                                    tooltip_duration=None
                                                                                    )))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center")
                            ], xs=4),    
                        ]),             

                            

                        ## --ROW2--
                        dbc.Row([
                            dbc.Col([
                                html.Br(),
                                html.P(children=[html.Strong('INSURANCE')], 
                                    style={'textAlign': 'center', 'fontSize': 22, 'background-color':'#F1F4F4','color':'#2a3f5f','font-family':'Verdana'}),

                                dbc.Row([###### INSURANCE Summary
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Summary')],
                                                                style={'textAlign': 'center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-info-square', style={
                                                                                        "color": "#F1F4F4",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-secondary',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=5),
                                    ###### INSURANCE Alerts
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Alerts')],
                                                                style={'textAlign': 'Center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-exclamation-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-warning',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center"),

                                dbc.Row([
                                    ###### INSURANCE Bar Plot
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(dcc.Graph(id='insurance_ba_bar'))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=5),
                                    ###### INSURANCE Alerts Table
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(html.Div(dash_table.DataTable(id="data_insurance_ba_alerts",
                                                                                    columns=[{'name':'Vessel','id': 'Vessel'},
                                                                                                {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                                    style_as_list_view=True,
                                                                                    style_header={'backgroundColor': 'white',
                                                                                                    'fontWeight': 'bold'
                                                                                                },
                                                                                    style_cell_conditional=[{'if': {'column_id': 'Vessel'},
                                                                                                                'width': '30%'},
                                                                                                                {'if': {'column_id': 'Remaining Days'},
                                                                                                                'width': '70%'},
                                                                                                                {'textAlign': 'center'}
                                                                                                            ],
                                                                                    style_cell={'font-family':'Verdana',
                                                                                                'fontSize': 13,
                                                                                                'color':'#2a3f5f',},
                                                                                    css=[{
                                                                                        'selector': '.dash-table-tooltip',
                                                                                        'rule': 'background-color: white; font-family: Verdana; color: #2a3f5f;'}],
                                                                                    tooltip_delay=0,
                                                                                    tooltip_duration=None
                                                                                    )))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center")
                            ], xs=4),

                            dbc.Col([
                                html.Br(),
                                html.P(children=[html.Strong('HEALTH')], 
                                    style={'textAlign': 'center', 'fontSize': 22, 'background-color':'#F1F4F4','color':'#2a3f5f','font-family':'Verdana'}),

                                dbc.Row([###### HEALTH Summary
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Summary')],
                                                                style={'textAlign': 'center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-info-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-secondary',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=5),
                                    ###### HEALTH Alerts
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Alerts')],
                                                                style={'textAlign': 'Center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-exclamation-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-warning',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center"),

                                dbc.Row([
                                    ###### HEALTH Plot
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(dcc.Graph(id='health_ba_bar'))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=5),
                                    ###### HEALTH Table
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(html.Div(dash_table.DataTable(id="data_health_ba_alerts",
                                                                                    columns=[{'name':'Vessel','id': 'Vessel'},
                                                                                                {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                                    style_as_list_view=True,
                                                                                    style_header={'backgroundColor': 'white',
                                                                                                    'fontWeight': 'bold'
                                                                                                },
                                                                                    style_cell_conditional=[{'if': {'column_id': 'Vessel'},
                                                                                                                'width': '30%'},
                                                                                                                {'if': {'column_id': 'Remaining Days'},
                                                                                                                'width': '70%'},
                                                                                                                {'textAlign': 'center'}
                                                                                                            ],
                                                                                    style_cell={'font-family':'Verdana',
                                                                                                'fontSize': 13,
                                                                                                'color':'#2a3f5f',},
                                                                                    css=[{
                                                                                        'selector': '.dash-table-tooltip',
                                                                                        'rule': 'background-color: white; font-family: Verdana; color: #2a3f5f;'}],
                                                                                    tooltip_delay=0,
                                                                                    tooltip_duration=None
                                                                                    )))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center")
                            ], xs=4),

                            dbc.Col([
                                html.Br(),
                                html.P(children=[html.Strong('OTHERS')], 
                                    style={'textAlign': 'center', 'fontSize': 22, 'background-color':'#F1F4F4','color':'#2a3f5f','font-family':'Verdana'}),

                                dbc.Row([###### OTHERS Summary
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Summary')],
                                                                style={'textAlign': 'center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-info-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-secondary',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=5),
                                    ###### OTHERS Alerts
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Alerts')],
                                                                style={'textAlign': 'Center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-exclamation-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-warning',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center"),

                                dbc.Row([
                                    ###### OTHERS Plot
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(dcc.Graph(id='others_ba_bar'))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=5),
                                    ###### OTHERS Alerts Table
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(html.Div(dash_table.DataTable(id="data_others_ba_alerts",
                                                                                    columns=[{'name':'Vessel','id': 'Vessel'},
                                                                                                {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                                    style_as_list_view=True,
                                                                                    style_header={'backgroundColor': 'white',
                                                                                                    'fontWeight': 'bold'
                                                                                                },
                                                                                    style_cell_conditional=[{'if': {'column_id': 'Vessel'},
                                                                                                                'width': '30%'},
                                                                                                                {'if': {'column_id': 'Remaining Days'},
                                                                                                                'width': '70%'},
                                                                                                                {'textAlign': 'center'}
                                                                                                            ],
                                                                                    style_cell={'font-family':'Verdana',
                                                                                                'fontSize': 13,
                                                                                                'color':'#2a3f5f',},
                                                                                    page_action="native",
                                                                                    page_current= 0,
                                                                                    page_size= 4,
                                                                                    css=[{
                                                                                        'selector': '.dash-table-tooltip',
                                                                                        'rule': 'background-color: white; font-family: Verdana; color: #2a3f5f;'}],
                                                                                    tooltip_delay=0,
                                                                                    tooltip_duration=None
                                                                                    )))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center")
                            ], xs=4)    
                        ]),
                    ]),

                    ##### TAB CTS
                    dcc.Tab(label='CTS', children=[
                        html.Br(),

                        ## --ROW1--
                        dbc.Row([
                            dbc.Col([
                                html.Br(),
                                html.P(children=[html.Strong('NAT & TONNAGE')], 
                                    style={'textAlign': 'center', 'fontSize': 22, 'background-color':'#F1F4F4','color':'#2a3f5f','font-family':'Verdana'}),

                                dbc.Row([###### NAT & TONNAGE Summary
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Summary')],
                                                                style={'textAlign': 'center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-info-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-secondary',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=5),
                                    ###### NAT & TONNAGE Alerts
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Alerts')],
                                                                style={'textAlign': 'Center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-exclamation-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-warning',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center"),

                                dbc.Row([
                                    ###### NAT & TONNAGE Bar Plot
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(dcc.Graph(id='nat&tonnage_cts_bar'))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=5),
                                    ###### NAT & TONNAGE Alerts Table
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(html.Div(dash_table.DataTable(id="data_nat&tonnage_cts_alerts",
                                                                                    columns=[{'name':'Vessel','id': 'Vessel'},
                                                                                                {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                                    style_as_list_view=True,
                                                                                    style_header={'backgroundColor': 'white',
                                                                                                    'fontWeight': 'bold'
                                                                                                },
                                                                                    style_cell_conditional=[{'if': {'column_id': 'Vessel'},
                                                                                                                'width': '30%'},
                                                                                                                {'if': {'column_id': 'Remaining Days'},
                                                                                                                'width': '70%'},
                                                                                                                {'textAlign': 'center'}
                                                                                                            ],
                                                                                    style_cell={'font-family':'Verdana',
                                                                                                'fontSize': 13,
                                                                                                'color':'#2a3f5f',},
                                                                                    css=[{
                                                                                        'selector': '.dash-table-tooltip',
                                                                                        'rule': 'background-color: grey; font-family: monospace; color: white',
                                                                                        #    'rule': 'background-color: white; font-family: monospace; color: #2a3f5f;',
                                                                                        }],
                                                                                    tooltip_delay=0,
                                                                                    tooltip_duration=None
                                                                                    )))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center")
                            ], xs=4),

                            dbc.Col([
                                html.Br(),
                                html.P(children=[html.Strong('SOLAS')], 
                                    style={'textAlign': 'center', 'fontSize': 22, 'background-color':'#F1F4F4','color':'#2a3f5f','font-family':'Verdana'}),

                                dbc.Row([###### SOLAS Summary
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Summary')],
                                                                style={'textAlign': 'center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-info-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-secondary',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=5),
                                    ###### SOLAS Alerts
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Alerts')],
                                                                style={'textAlign': 'Center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-exclamation-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-warning',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center"),

                                dbc.Row([
                                    ###### SOLAS Bar Plot
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(dcc.Graph(id='solas_cts_bar'))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=5),
                                    ###### SOLAS Alerts Table
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(html.Div(dash_table.DataTable(id="data_solas_cts_alerts",
                                                                                    columns=[{'name':'Vessel','id': 'Vessel'},
                                                                                                {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                                    style_as_list_view=True,
                                                                                    style_header={'backgroundColor': 'white',
                                                                                                    'fontWeight': 'bold'
                                                                                                },
                                                                                    style_cell_conditional=[{'if': {'column_id': 'Vessel'},
                                                                                                                'width': '30%'},
                                                                                                                {'if': {'column_id': 'Remaining Days'},
                                                                                                                'width': '70%'},
                                                                                                                {'textAlign': 'center'}
                                                                                                            ],
                                                                                    style_cell={'font-family':'Verdana',
                                                                                                'fontSize': 13,
                                                                                                'color':'#2a3f5f',},
                                                                                    css=[{
                                                                                        'selector': '.dash-table-tooltip',
                                                                                        'rule': 'background-color: white; font-family: Verdana; color: #2a3f5f;'}],
                                                                                    tooltip_delay=0,
                                                                                    tooltip_duration=None
                                                                                    )))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center")
                            ], xs=4),                    

                            dbc.Col([
                                html.Br(),
                                html.P(children=[html.Strong('POLLUTION')], 
                                    style={'textAlign': 'center', 'fontSize': 22, 'background-color':'#F1F4F4','color':'#2a3f5f','font-family':'Verdana'}),

                                dbc.Row([###### POLLUTION Summary
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Summary')],
                                                                style={'textAlign': 'center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-info-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-secondary',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=5),
                                    ###### POLLUTION Alerts
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Alerts')],
                                                                style={'textAlign': 'Center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-exclamation-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-warning',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center"),

                                dbc.Row([
                                    ###### POLLUTION Bar Plot
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(dcc.Graph(id='pollution_cts_bar'))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=5),
                                    ###### POLLUTION Alerts Table
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(html.Div(dash_table.DataTable(id="data_pollution_cts_alerts",
                                                                                    columns=[{'name':'Vessel','id': 'Vessel'},
                                                                                                {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                                    style_as_list_view=True,
                                                                                    style_header={'backgroundColor': 'white',
                                                                                                    'fontWeight': 'bold'
                                                                                                },
                                                                                    style_cell_conditional=[{'if': {'column_id': 'Vessel'},
                                                                                                                'width': '30%'},
                                                                                                                {'if': {'column_id': 'Remaining Days'},
                                                                                                                'width': '70%'},
                                                                                                                {'textAlign': 'center'}
                                                                                                            ],
                                                                                    style_cell={'font-family':'Verdana',
                                                                                                'fontSize': 13,
                                                                                                'color':'#2a3f5f',},
                                                                                    css=[{
                                                                                        'selector': '.dash-table-tooltip',
                                                                                        'rule': 'background-color: white; font-family: Verdana; color: #2a3f5f;'}],
                                                                                    tooltip_delay=0,
                                                                                    tooltip_duration=None
                                                                                    )))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center")
                            ], xs=4),
                        ]),

                        ## --ROW2--
                        dbc.Row([
                            dbc.Col([
                                html.Br(),
                                html.P(children=[html.Strong('CLASS')], 
                                    style={'textAlign': 'center', 'fontSize': 22, 'background-color':'#F1F4F4','color':'#2a3f5f','font-family':'Verdana'}),

                                dbc.Row([###### CLASS Summary
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Summary')],
                                                                style={'textAlign': 'center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-info-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-secondary',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=5),
                                    ###### CLASS Alerts
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Alerts')],
                                                                style={'textAlign': 'Center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-exclamation-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-warning',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center"),

                                dbc.Row([
                                    ###### CLASS Bar Plot
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(dcc.Graph(id='class_cts_bar'))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=5),
                                    ###### CLASS Alerts Table
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(html.Div(dash_table.DataTable(id="data_class_cts_alerts",
                                                                                    columns=[{'name':'Vessel','id': 'Vessel'},
                                                                                                {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                                    style_as_list_view=True,
                                                                                    style_header={'backgroundColor': 'white',
                                                                                                    'fontWeight': 'bold'
                                                                                                },
                                                                                    style_cell_conditional=[{'if': {'column_id': 'Vessel'},
                                                                                                                'width': '30%'},
                                                                                                                {'if': {'column_id': 'Remaining Days'},
                                                                                                                'width': '70%'},
                                                                                                                {'textAlign': 'center'}
                                                                                                            ],
                                                                                    style_cell={'font-family':'Verdana',
                                                                                                'fontSize': 13,
                                                                                                'color':'#2a3f5f',},
                                                                                    css=[{
                                                                                        'selector': '.dash-table-tooltip',
                                                                                        'rule': 'background-color: white; font-family: Verdana; color: #2a3f5f;'}],
                                                                                    tooltip_delay=0,
                                                                                    tooltip_duration=None
                                                                                    )))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center")
                            ], xs=4),

                            dbc.Col([
                                html.Br(),
                                html.P(children=[html.Strong('INSURANCE')], 
                                    style={'textAlign': 'center', 'fontSize': 22, 'background-color':'#F1F4F4','color':'#2a3f5f','font-family':'Verdana'}),

                                dbc.Row([###### INSURANCE Summary
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Summary')],
                                                                style={'textAlign': 'center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-info-square', style={
                                                                                        "color": "#F1F4F4",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-secondary',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=5),
                                    ###### INSURANCE Alerts
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Alerts')],
                                                                style={'textAlign': 'Center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-exclamation-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-warning',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center"),

                                dbc.Row([
                                    ###### INSURANCE Bar Plot
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(dcc.Graph(id='insurance_cts_bar'))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=5),
                                    ###### INSURANCE Alerts Table
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(html.Div(dash_table.DataTable(id="data_insurance_cts_alerts",
                                                                                    columns=[{'name':'Vessel','id': 'Vessel'},
                                                                                                {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                                    style_as_list_view=True,
                                                                                    style_header={'backgroundColor': 'white',
                                                                                                    'fontWeight': 'bold'
                                                                                                },
                                                                                    style_cell_conditional=[{'if': {'column_id': 'Vessel'},
                                                                                                                'width': '30%'},
                                                                                                                {'if': {'column_id': 'Remaining Days'},
                                                                                                                'width': '70%'},
                                                                                                                {'textAlign': 'center'}
                                                                                                            ],
                                                                                    style_cell={'font-family':'Verdana',
                                                                                                'fontSize': 13,
                                                                                                'color':'#2a3f5f',},
                                                                                    css=[{
                                                                                        'selector': '.dash-table-tooltip',
                                                                                        'rule': 'background-color: white; font-family: Verdana; color: #2a3f5f;'}],
                                                                                    tooltip_delay=0,
                                                                                    tooltip_duration=None
                                                                                    )))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center")
                            ], xs=4),

                            dbc.Col([
                                html.Br(),
                                html.P(children=[html.Strong('LSA & FFA')], 
                                    style={'textAlign': 'center', 'fontSize': 22, 'background-color':'#F1F4F4','color':'#2a3f5f','font-family':'Verdana'}),

                                dbc.Row([###### LSA & FFA Summary
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Summary')],
                                                                style={'textAlign': 'center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-info-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-secondary',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=5),
                                    ###### LSA & FFA Alerts
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Alerts')],
                                                                style={'textAlign': 'Center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-exclamation-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-warning',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center"),

                                dbc.Row([
                                    ###### LSA & FFA Bar Plot
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(dcc.Graph(id='lsa&fa_cts_bar'))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=5),
                                    ###### LSA & FFA Alerts Table
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(html.Div(dash_table.DataTable(id="data_lsa&fa_cts_alerts",
                                                                                    columns=[{'name':'Vessel','id': 'Vessel'},
                                                                                                {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                                    style_as_list_view=True,
                                                                                    style_header={'backgroundColor': 'white',
                                                                                                    'fontWeight': 'bold'
                                                                                                },
                                                                                    style_cell_conditional=[{'if': {'column_id': 'Vessel'},
                                                                                                                'width': '30%'},
                                                                                                                {'if': {'column_id': 'Remaining Days'},
                                                                                                                'width': '70%'},
                                                                                                                {'textAlign': 'center'}
                                                                                                            ],
                                                                                    style_cell={'font-family':'Verdana',
                                                                                                'fontSize': 13,
                                                                                                'color':'#2a3f5f',},
                                                                                    css=[{
                                                                                        'selector': '.dash-table-tooltip',
                                                                                        'rule': 'background-color: white; font-family: Verdana; color: #2a3f5f;'}],
                                                                                    tooltip_delay=0,
                                                                                    tooltip_duration=None
                                                                                    )))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center")
                            ], xs=4),
                        ]),

                        ## --ROW3--
                        dbc.Row([
                            dbc.Col([
                                html.Br(),
                                html.P(children=[html.Strong('HEALTH')], 
                                    style={'textAlign': 'center', 'fontSize': 22, 'background-color':'#F1F4F4','color':'#2a3f5f','font-family':'Verdana'}),

                                dbc.Row([###### HEALTH Summary
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Summary')],
                                                                style={'textAlign': 'center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-info-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-secondary',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=5),
                                    ###### HEALTH Alerts
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Alerts')],
                                                                style={'textAlign': 'Center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-exclamation-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-warning',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center"),

                                dbc.Row([
                                    ###### HEALTH Plot
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(dcc.Graph(id='health_cts_bar'))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=5),
                                    ###### HEALTH Table
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(html.Div(dash_table.DataTable(id="data_health_cts_alerts",
                                                                                    columns=[{'name':'Vessel','id': 'Vessel'},
                                                                                                {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                                    style_as_list_view=True,
                                                                                    style_header={'backgroundColor': 'white',
                                                                                                    'fontWeight': 'bold'
                                                                                                },
                                                                                    style_cell_conditional=[{'if': {'column_id': 'Vessel'},
                                                                                                                'width': '30%'},
                                                                                                                {'if': {'column_id': 'Remaining Days'},
                                                                                                                'width': '70%'},
                                                                                                                {'textAlign': 'center'}
                                                                                                            ],
                                                                                    style_cell={'font-family':'Verdana',
                                                                                                'fontSize': 13,
                                                                                                'color':'#2a3f5f',},
                                                                                    css=[{
                                                                                        'selector': '.dash-table-tooltip',
                                                                                        'rule': 'background-color: white; font-family: Verdana; color: #2a3f5f;'}],
                                                                                    tooltip_delay=0,
                                                                                    tooltip_duration=None
                                                                                    )))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center")
                            ], xs=4),

                            dbc.Col([
                                html.Br(),
                                html.P(children=[html.Strong('OTHERS')], 
                                    style={'textAlign': 'center', 'fontSize': 22, 'background-color':'#F1F4F4','color':'#2a3f5f','font-family':'Verdana'}),

                                dbc.Row([###### OTHERS Summary
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Summary')],
                                                                style={'textAlign': 'center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-info-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-secondary',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=5),
                                    ###### OTHERS Alerts
                                    dbc.Col([
                                        dbc.CardGroup([
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.P(children=[html.Strong('Alerts')],
                                                                style={'textAlign': 'Center', 
                                                                    'fontSize': 16, 
                                                                    'background-color':'#F1F4F4',
                                                                    'color':'#2a3f5f',
                                                                    'font-family':'Verdana'}),
                                                    ]
                                                ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px", 'background':'#F1F4F4'}
                                            ),
                                            dbc.Card(
                                                html.Div(className='bi bi-exclamation-square', style={
                                                                                        "color": "white",
                                                                                        "textAlign": "center",
                                                                                        "fontSize": 30,
                                                                                        "margin": "auto",
                                                                                    }),
                                                className='bg-warning',
                                                color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                            ),
                                        ],),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center"),

                                dbc.Row([
                                    ###### OTHERS Plot
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(dcc.Graph(id='others_cts_bar'))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=5),
                                    ###### OTHERS Alerts Table
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody(html.Div(dash_table.DataTable(id="data_others_cts_alerts",
                                                                                    columns=[{'name':'Vessel','id': 'Vessel'},
                                                                                                {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                                    style_as_list_view=True,
                                                                                    style_header={'backgroundColor': 'white',
                                                                                                    'fontWeight': 'bold'
                                                                                                },
                                                                                    style_cell_conditional=[{'if': {'column_id': 'Vessel'},
                                                                                                                'width': '30%'},
                                                                                                                {'if': {'column_id': 'Remaining Days'},
                                                                                                                'width': '70%'},
                                                                                                                {'textAlign': 'center'}
                                                                                                            ],
                                                                                    style_cell={'font-family':'Verdana',
                                                                                                'fontSize': 13,
                                                                                                'color':'#2a3f5f',},
                                                                                    page_action="native",
                                                                                    page_current= 0,
                                                                                    page_size= 4,
                                                                                    css=[{
                                                                                        'selector': '.dash-table-tooltip',
                                                                                        'rule': 'background-color: white; font-family: Verdana; color: #2a3f5f;'}],
                                                                                    tooltip_delay=0,
                                                                                    tooltip_duration=None
                                                                                    )))
                                        ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px", 'background':'#F1F4F4'}),
                                    ], xs=7),
                                ], className="g-0 d-flex align-items-center")
                            ], xs=4),
                        ]),
                    ]),
                ],
                style={
                    'font-family':'Verdana',
                    'font-size': '20px',
                    'display': 'inlineBlock', 
                    'height': '8vh', 
                    'border-radius': '4px',
                    'font-weight': 'bold'
                    },
                colors={
                    "border":"white",
                    "primary": "#242947",
                    "background": "#F1F4F4",}),


    html.Br(),
    html.Footer('DCA',
            style={'textAlign': 'center', 
                'fontSize': 20, 
                'background-color':'#2a3f5f',
                'color':'white'})
    ], style={
        'paddingLeft':'10px',
        'paddingRight':'10px',
    })

#### Callback Auto Update Chart & Data
@callback(
    [
    Output('nat&tonnage_tb_bar', 'figure'),
    Output('data_nat&tonnage_tb_alerts', 'data'),

    Output('solas_tb_bar', 'figure'),
    Output('data_solas_tb_alerts', 'data'),

    Output('pollution_tb_bar', 'figure'),
    Output('data_pollution_tb_alerts', 'data'),

    Output('class_tb_bar', 'figure'),
    Output('data_class_tb_alerts', 'data'),

    Output('insurance_tb_bar', 'figure'),
    Output('data_insurance_tb_alerts', 'data'),

    Output('lsa&fa_tb_bar', 'figure'),
    Output('data_lsa&fa_tb_alerts', 'data'),

    Output('health_tb_bar', 'figure'),
    Output('data_health_tb_alerts', 'data'),

    Output('others_tb_bar', 'figure'),
    Output('data_others_tb_alerts', 'data'),


    Output('nat&tonnage_ba_bar', 'figure'),
    Output('data_nat&tonnage_ba_alerts', 'data'),

    Output('solas_ba_bar', 'figure'),
    Output('data_solas_ba_alerts', 'data'),

    Output('class_ba_bar', 'figure'),
    Output('data_class_ba_alerts', 'data'),

    Output('insurance_ba_bar', 'figure'),
    Output('data_insurance_ba_alerts', 'data'),

    Output('health_ba_bar', 'figure'),
    Output('data_health_ba_alerts', 'data'),

    Output('others_ba_bar', 'figure'),
    Output('data_others_ba_alerts', 'data'),


    Output('nat&tonnage_cts_bar', 'figure'),
    Output('data_nat&tonnage_cts_alerts', 'data'),

    Output('solas_cts_bar', 'figure'),
    Output('data_solas_cts_alerts', 'data'),

    Output('pollution_cts_bar', 'figure'),
    Output('data_pollution_cts_alerts', 'data'),

    Output('class_cts_bar', 'figure'),
    Output('data_class_cts_alerts', 'data'),

    Output('insurance_cts_bar', 'figure'),
    Output('data_insurance_cts_alerts', 'data'),

    Output('lsa&fa_cts_bar', 'figure'),
    Output('data_lsa&fa_cts_alerts', 'data'),

    Output('health_cts_bar', 'figure'),
    Output('data_health_cts_alerts', 'data'),

    Output('others_cts_bar', 'figure'),
    Output('data_others_cts_alerts', 'data'),
    ],
    Input('store', 'data')
)
def update_charts(data):
    ######################
    # Pre Processing
    ######################
    # Tug Boat
    ######################
    df_tb = pd.DataFrame(data['Tugboat'])

    ### datetime variable
    col = df_tb.columns
    col = list(col)

    no_date = ['NO', 'NAMA KAPAL', 'YEARD OF BUILD', 'SURAT UKUR INTERNATIONAL (INTERNATIONAL TONNAGE CERTIFICATE)', 
            '3/6/12 BULAN', ]
    col = [x for x in col if x not in no_date]

    ### apply datetime to selected variable
    df_tb = df_tb.replace(r'^\s*$', np.nan, regex=True)
    df_tb[col] = df_tb[col].apply(pd.to_datetime, format='%d %B %Y')

    ### remove unnecessary variable
    col_del = ['NO', 'YEARD OF BUILD', 'SURAT UKUR INTERNATIONAL (INTERNATIONAL TONNAGE CERTIFICATE)',
            '3/6/12 BULAN', 'NOTA DINAS 1', 'NOTA DINAS 2']
    col_stay = [x for x in df_tb.columns if x not in col_del]

    ### set new data frame
    df_tb = df_tb[col_stay]

    ### define which variable is for others
    df_tb['Others'] = df_tb[['SERTIFIKAT NASIONAL SISTEM ANTI TERITIP (CERTIFICATE FOULING SISTEM)',
                                        'DOKUMEN PENGAWAKAN MINIMUM (MINIMUM SAFE MANNING DOCUMENT)',
                                        'SERTIFIKAT SIKR (SURAT IZIN STASIUN RADIO KAPAL LAUT)',
                                        'IJIN PENGOPERASIAN KAPAL DALAM NEGERI (RPT) (DOMESTIC VESSEL OPERATING PERMIT)']].min(axis=1)
    # New dataframe for remaining days
    diff_tb = ['SURAT LAUT/ PAS TAHUNAN (CERTIFICATE OF NATIONALITY)',
                'SERT. KESELAMATAN KONSTRUKSI KAPAL (CERTIFICATE OF SHIP SAFETY CONSTRUCTION)',
                'SERT. PENCEGAHAN PENCEMARAN MINYAK (CERTIFICATE OF INTERNATIONAL OIL POLLUTION PREVENTION (IOPP))',
                'NEXT ANNUAL',
                'SERTIFIKAT JAMINAN GANTI RUGI PENCEMARAN MINYAK',
                'SERTIFIKAT PEMERIKSAAN RAKIT PENYELAMATAN (CERTIFICATE OF LIFERAFT INSPECTION)',
                'SERTIFIKAT BEBAS TINDAKAN SANITASI KAPAL (SHIP SANITATION CONTROL EXEMPTON CERTIFICATE)',
                'Others'
                ]

    df_diff_tb = df_tb[['NAMA KAPAL']+diff_tb].copy()

    # Add new variable for remaining days
    diff_tb_name = ['Nationality & Tonnage Remain Days', 
                    'SOLAS Remain Days', 
                    'Pollution Remain Days', 
                    'Class Remain Days', 
                    'Insurance Remain Days',
                    'LSA & FFA Remain Days',
                    'Health Remain Days',
                    'Others Remain Days']

    for (i,j) in zip(diff_tb, diff_tb_name):
        df_diff_tb[j] = (df_diff_tb[i]-pd.to_datetime('today')).dt.days

    # Add new variable for remaining days (Months, Days)
    diff_tb_name2 = ['Nationality & Tonnage Remain Days2', 
                    'SOLAS Remain Days2', 
                    'Pollution Remain Days2', 
                    'Class Remain Days2', 
                    'Insurance Remain Days2',
                    'LSA & FFA Remain Days2',
                    'Health Remain Days2',
                    'Others Remain Days2']

    # Function for calculating remaining days
    def date_diff(var):
        remaining =[]
        for i in var:
            if i is pd.NaT:
                remaining.append(pd.Timestamp('NaT'))
            else :
                delta = relativedelta(i, pd.to_datetime('today'))
                remaining.append((str(delta.days)+ ' days'))
        return(remaining)

    for i,j in zip(diff_tb, diff_tb_name2):
        df_diff_tb[j] = date_diff(df_diff_tb[i])
    
    df_diff_tb.rename(columns={
            'SURAT LAUT/ PAS TAHUNAN (CERTIFICATE OF NATIONALITY)':'Nationality & Tonnage',
            'SERT. KESELAMATAN KONSTRUKSI KAPAL (CERTIFICATE OF SHIP SAFETY CONSTRUCTION)':'SOLAS',
            'SERT. PENCEGAHAN PENCEMARAN MINYAK (CERTIFICATE OF INTERNATIONAL OIL POLLUTION PREVENTION (IOPP))':'Pollution',
            'NEXT ANNUAL':'Class',
            'SERTIFIKAT JAMINAN GANTI RUGI PENCEMARAN MINYAK':'Insurance',
            'SERTIFIKAT PEMERIKSAAN RAKIT PENYELAMATAN (CERTIFICATE OF LIFERAFT INSPECTION)':'LSA & FFA',
            'SERTIFIKAT BEBAS TINDAKAN SANITASI KAPAL (SHIP SANITATION CONTROL EXEMPTON CERTIFICATE)':'Health',
            'Others':'Others',
        }, inplace=True)
    
    ######################
    # Barge
    ######################
    df_ba = pd.DataFrame(data['Barge'])

    ### datetime variable
    col_ba = df_ba.columns
    col_ba = list(col_ba)

    no_date = ['NO', 'NAMA KAPAL', 'YEARD OF BUILD', 'SURAT UKUR INTERNATIONAL (INTERNATIONAL TONNAGE CERTIFICATE)', 
            '3/6/12 BULAN', ]
    col_ba = [x for x in col_ba if x not in no_date]

    ### apply datetime to selected variable
    df_ba = df_ba.replace(r'^\s*$', np.nan, regex=True)
    df_ba[col_ba] = df_ba[col_ba].apply(pd.to_datetime, format='%d %B %Y')

    ### remove unnecessary variable
    col_del_ba = ['NO', 'YEARD OF BUILD', 'SURAT UKUR INTERNATIONAL (INTERNATIONAL TONNAGE CERTIFICATE)',
                  '3/6/12 BULAN', 'NOTA DINAS 1', 'NOTA DINAS 2']
    col_stay_ba = [x for x in df_ba.columns if x not in col_del_ba]

    ### set new data frame
    df_ba = df_ba[col_stay_ba]

    ### define which variable is for others
    df_ba['Others'] = df_ba[['SERTIFIKAT NASIONAL SISTEM ANTI TERITIP (CERTIFICATE FOULING SYSTEM)',
                            'IJIN PENGOPERASIAN KAPAL DALAM NEGERI (RPT) (DOMESTIC VESSEL OPERATING PERMIT)']].min(axis=1)
    
    # New dataframe for remaining days
    diff_ba = ['SURAT LAUT/ PAS TAHUNAN (CERTIFICATE OF NATIONALITY)',
                'SERT. KESELAMATAN KONSTRUKSI KAPAL (CERTIFICATE OF SHIP SAFETY CONSTRUCTION)',
                'NEXT ANNUAL',
                'SERTIFIKAT ASURANSI (CERTIFICATE OF INSURANCE)',
                'SERTIFIKAT BEBAS TINDAKAN SANITASI KAPAL (SHIP SANITATION CONTROL EXEMPTON CERTIFICATE)',
                'Others'
                ]

    df_diff_ba = df_ba[['NAMA KAPAL']+diff_ba].copy()

    # Add new variable for remaining days
    diff_ba_name = ['Nationality & Tonnage Remain Days', 
                    'SOLAS Remain Days', 
                    'Class Remain Days', 
                    'Insurance Remain Days',
                    'Health Remain Days',
                    'Others Remain Days']

    for (i,j) in zip(diff_ba, diff_ba_name):
        df_diff_ba[j] = (df_diff_ba[i]-pd.to_datetime('today')).dt.days

    # Add new variable for remaining days (Months, Days)
    diff_ba_name2 = ['Nationality & Tonnage Remain Days2', 
                    'SOLAS Remain Days2', 
                    'Class Remain Days2', 
                    'Insurance Remain Days2',
                    'Health Remain Days2',
                    'Others Remain Days2']

    # Function for calculating remaining days
    def date_diff(var):
        remaining =[]
        for i in var:
            if i is pd.NaT:
                remaining.append(pd.Timestamp('NaT'))
            else :
                delta = relativedelta(i, pd.to_datetime('today'))
                remaining.append((str(delta.days)+ ' days'))
        return(remaining)

    for i,j in zip(diff_ba, diff_ba_name2):
        df_diff_ba[j] = date_diff(df_diff_ba[i])
    
    df_diff_ba.rename(columns={
            'SURAT LAUT/ PAS TAHUNAN (CERTIFICATE OF NATIONALITY)':'Nationality & Tonnage',
            'SERT. KESELAMATAN KONSTRUKSI KAPAL (CERTIFICATE OF SHIP SAFETY CONSTRUCTION)':'SOLAS',
            'NEXT ANNUAL':'Class',
            'SERTIFIKAT ASURANSI (CERTIFICATE OF INSURANCE)':'Insurance',
            'SERTIFIKAT BEBAS TINDAKAN SANITASI KAPAL (SHIP SANITATION CONTROL EXEMPTON CERTIFICATE)':'Health',
            'Others':'Others',
        }, inplace=True)
    
    ######################
    # CTS
    ######################
    df_cts = pd.DataFrame(data['CTS'])

    ### datetime variable
    col = df_cts.columns
    col = list(col)

    no_date_cts = ['NO', 'NAMA KAPAL', 'YEARD OF BUILD', 'SURAT UKUR INTERNATIONAL (INTERNATIONAL TONNAGE CERTIFICATE)', 
            '3/6/12 BULAN', ]
    col = [x for x in col if x not in no_date_cts]

    ### apply datetime to selected variable
    df_cts = df_cts.replace(r'^\s*$', np.nan, regex=True)
    df_cts[col] = df_cts[col].apply(pd.to_datetime, format='%d %B %Y')

    ### remove unnecessary variable
    col_del_cts = ['NO','INTERMEDATE SURVEY','SPESIAL SURVEY',"INTERMEDATE SURVEY2",'SPESIAL SURVEY2','INTERMEDATE SURVEY3',
            'SPESIAL SURVEY3', 'SURAT UKUR INTERNATIONAL (INTERNATIONAL TONNAGE CERTIFICATE)',
            '3/6/12 BULAN', 'NEXT RENEWAL SYABANDAR','NOTA DINAS 1', 'NOTA DINAS 2',
            'NEXT ANNUAL', 'REMOVAL OF WRECKS1', 'HULL & MACHINE', 'CERTIFIACATE DOCUMENT OF COMPLAINCE', ]
    col_stay_cts = [x for x in df_cts.columns if x not in col_del_cts]

    ### set new data frame
    df_cts = df_cts[col_stay_cts]

    ### define which variable is for others
    df_cts['Others'] = df_cts[['SERTIFIKAT NASIONAL SISTEM ANTI TERITIP (CERTIFICATE FOULING SISTEM)',
                                'DOKUMEN PENGAWAKAN MINIMUM (MINIMUM SAFE MANNING DOCUMENT)',
                                # 'SERTIFIKAT SIKR (SURAT IZIN STASIUN RADIO KAPAL LAUT)',
                                # 'IJIN PENGOPERASIAN KAPAL DALAM NEGERI (RPT) (DOMESTIC VESSEL OPERATING PERMIT)'
                                ]].min(axis=1)
    # New dataframe for remaining days
    diff_cts = ['SURAT LAUT/ PAS TAHUNAN (CERTIFICATE OF NATIONALITY)',
                'SERT. KESELAMATAN KONSTRUKSI KAPAL (CERTIFICATE OF SHIP SAFETY CONSTRUCTION)',
                'SERT. PENCEGAHAN PENCEMARAN MINYAK (CERTIFICATE OF INTERNATIONAL OIL POLLUTION PREVENTION (IOPP))',
                'SERT. GARIS MUAT INTERNASIONAL (CERTIFICATE OF LOAD LINE)',
                'SERTIFIKAT JAMINAN GANTI RUGI PENCEMARAN MINYAK',
                'SERTIFIKAT PEMERIKSAAN RAKIT PENYELAMATAN (CERTIFICATE OF LIFERAFT INSPECTION)',
                'SERTIFIKAT BEBAS TINDAKAN SANITASI KAPAL (SHIP SANITATION CONTROL EXEMPTON CERTIFICATE)',
                'Others'
                ]

    df_diff_cts = df_cts[['NAMA KAPAL']+diff_cts].copy()

    # Add new variable for remaining days
    diff_cts_name = ['Nationality & Tonnage Remain Days', 
                    'SOLAS Remain Days', 
                    'Pollution Remain Days', 
                    'Class Remain Days', 
                    'Insurance Remain Days',
                    'LSA & FFA Remain Days',
                    'Health Remain Days',
                    'Others Remain Days']

    for (i,j) in zip(diff_cts, diff_cts_name):
        df_diff_cts[j] = (df_diff_cts[i]-pd.to_datetime('today')).dt.days

    # Add new variable for remaining days (Months, Days)
    diff_cts_name2 = ['Nationality & Tonnage Remain Days2', 
                    'SOLAS Remain Days2', 
                    'Pollution Remain Days2', 
                    'Class Remain Days2', 
                    'Insurance Remain Days2',
                    'LSA & FFA Remain Days2',
                    'Health Remain Days2',
                    'Others Remain Days2']

    # Function for calculating remaining days
    def date_diff(var):
        remaining =[]
        for i in var:
            if i is pd.NaT:
                remaining.append(pd.Timestamp('NaT'))
            else :
                delta = relativedelta(i, pd.to_datetime('today'))
                remaining.append((str(delta.days)+ ' days'))
        return(remaining)

    for i,j in zip(diff_cts, diff_cts_name2):
        df_diff_cts[j] = date_diff(df_diff_cts[i])
    
    df_diff_cts.rename(columns={
            'SURAT LAUT/ PAS TAHUNAN (CERTIFICATE OF NATIONALITY)':'Nationality & Tonnage',
            'SERT. KESELAMATAN KONSTRUKSI KAPAL (CERTIFICATE OF SHIP SAFETY CONSTRUCTION)':'SOLAS',
            'SERT. PENCEGAHAN PENCEMARAN MINYAK (CERTIFICATE OF INTERNATIONAL OIL POLLUTION PREVENTION (IOPP))':'Pollution',
            'SERT. GARIS MUAT INTERNASIONAL (CERTIFICATE OF LOAD LINE)':'Class',
            'SERTIFIKAT JAMINAN GANTI RUGI PENCEMARAN MINYAK':'Insurance',
            'SERTIFIKAT PEMERIKSAAN RAKIT PENYELAMATAN (CERTIFICATE OF LIFERAFT INSPECTION)':'LSA & FFA',
            'SERTIFIKAT BEBAS TINDAKAN SANITASI KAPAL (SHIP SANITATION CONTROL EXEMPTON CERTIFICATE)':'Health',
            'Others':'Others',
        }, inplace=True)
        
    ## DataFrame For Classification
    nat_tonnage_tb_expired, nat_tonnage_tb_alerts, nat_tonnage_tb_ok = nat_tonnage_classify(df_diff_tb)
    solas_tb_expired, solas_tb_alerts, solas_tb_ok = solas_classify(df_diff_tb)
    pollution_tb_expired, pollution_tb_alerts, pollution_tb_ok = pollution_classify(df_diff_tb)
    class_tb_expired, class_tb_alerts, class_tb_ok = class_classify(df_diff_tb)
    insurance_tb_expired, insurance_tb_alerts, insurance_tb_ok = insurance_classify(df_diff_tb)
    lsa_fa_tb_expired, lsa_fa_tb_alerts, lsa_fa_tb_ok = lsa_ffa_classify(df_diff_tb)
    health_tb_expired, health_tb_alerts, health_tb_ok = health_classify(df_diff_tb)
    others_tb_expired, others_tb_alerts, others_tb_ok = others_classify(df_diff_tb)

    nat_tonnage_ba_expired, nat_tonnage_ba_alerts, nat_tonnage_ba_ok = nat_tonnage_classify(df_diff_ba)
    solas_ba_expired, solas_ba_alerts, solas_ba_ok = solas_classify(df_diff_ba)
    class_ba_expired, class_ba_alerts, class_ba_ok = class_classify(df_diff_ba)
    insurance_ba_expired, insurance_ba_alerts, insurance_ba_ok = insurance_classify(df_diff_ba)
    health_ba_expired, health_ba_alerts, health_ba_ok = health_classify(df_diff_ba)
    others_ba_expired, others_ba_alerts, others_ba_ok = others_classify(df_diff_ba)

    nat_tonnage_cts_expired, nat_tonnage_cts_alerts, nat_tonnage_cts_ok = nat_tonnage_classify(df_diff_cts)
    solas_cts_expired, solas_cts_alerts, solas_cts_ok = solas_classify(df_diff_cts)
    pollution_cts_expired, pollution_cts_alerts, pollution_cts_ok = pollution_classify(df_diff_cts)
    class_cts_expired, class_cts_alerts, class_cts_ok = class_classify(df_diff_cts)
    insurance_cts_expired, insurance_cts_alerts, insurance_cts_ok = insurance_classify(df_diff_cts)
    lsa_fa_cts_expired, lsa_fa_cts_alerts, lsa_fa_cts_ok = lsa_ffa_classify(df_diff_cts)
    health_cts_expired, health_cts_alerts, health_cts_ok = health_classify(df_diff_cts)
    others_cts_expired, others_cts_alerts, others_cts_ok = others_classify(df_diff_cts)

    ## DataFrame to dash table
    data_nat_tonnage_tb_alerts = nat_tonnage_tb_alerts.to_dict('records')
    data_solas_tb_alerts = solas_tb_alerts.to_dict('records')
    data_pollution_tb_alerts = pollution_tb_alerts.to_dict('records')
    data_class_tb_alerts = class_tb_alerts.to_dict('records')
    data_insurance_tb_alerts = insurance_tb_alerts.to_dict('records')
    data_lsa_fa_tb_alerts = lsa_fa_tb_alerts.to_dict('records')
    data_health_tb_alerts = health_tb_alerts.to_dict('records')
    data_others_tb_alerts = others_tb_alerts.to_dict('records')

    data_nat_tonnage_ba_alerts = nat_tonnage_ba_alerts.to_dict('records')
    data_solas_ba_alerts = solas_ba_alerts.to_dict('records')
    data_class_ba_alerts = class_ba_alerts.to_dict('records')
    data_insurance_ba_alerts = insurance_ba_alerts.to_dict('records')
    data_health_ba_alerts = health_ba_alerts.to_dict('records')
    data_others_ba_alerts = others_ba_alerts.to_dict('records')

    data_nat_tonnage_cts_alerts = nat_tonnage_cts_alerts.to_dict('records')
    data_solas_cts_alerts = solas_cts_alerts.to_dict('records')
    data_pollution_cts_alerts = pollution_cts_alerts.to_dict('records')
    data_class_cts_alerts = class_cts_alerts.to_dict('records')
    data_insurance_cts_alerts = insurance_cts_alerts.to_dict('records')
    data_lsa_fa_cts_alerts = lsa_fa_cts_alerts.to_dict('records')
    data_health_cts_alerts = health_cts_alerts.to_dict('records')
    data_others_cts_alerts = others_cts_alerts.to_dict('records')

    ## DataFrame to Bar Plot data
    len_nat_tonnage_tb = [len(nat_tonnage_tb_ok), len(nat_tonnage_tb_alerts), len(nat_tonnage_tb_expired)]
    len_solas_tb = [len(solas_tb_ok), len(solas_tb_alerts), len(solas_tb_expired)]
    len_pollution_tb = [len(pollution_tb_ok), len(pollution_tb_alerts), len(pollution_tb_expired)]
    len_class_tb = [len(class_tb_ok), len(class_tb_alerts), len(class_tb_expired)]
    len_insurance_tb = [len(insurance_tb_ok), len(insurance_tb_alerts), len(insurance_tb_expired)]
    len_lsa_fa_tb = [len(lsa_fa_tb_ok), len(lsa_fa_tb_alerts), len(lsa_fa_tb_expired)]
    len_health_tb = [len(health_tb_ok), len(health_tb_alerts), len(health_tb_expired)]
    len_others_tb = [len(others_tb_ok), len(others_tb_alerts), len(others_tb_expired)]

    len_nat_tonnage_ba = [len(nat_tonnage_ba_ok), len(nat_tonnage_ba_alerts), len(nat_tonnage_ba_expired)]
    len_solas_ba = [len(solas_ba_ok), len(solas_ba_alerts), len(solas_ba_expired)]
    len_class_ba = [len(class_ba_ok), len(class_ba_alerts), len(class_ba_expired)]
    len_insurance_ba = [len(insurance_ba_ok), len(insurance_ba_alerts), len(insurance_ba_expired)]
    len_health_ba = [len(health_ba_ok), len(health_ba_alerts), len(health_ba_expired)]
    len_others_ba = [len(others_ba_ok), len(others_ba_alerts), len(others_ba_expired)]

    len_nat_tonnage_cts = [len(nat_tonnage_cts_ok), len(nat_tonnage_cts_alerts), len(nat_tonnage_cts_expired)]
    len_solas_cts = [len(solas_cts_ok), len(solas_cts_alerts), len(solas_cts_expired)]
    len_pollution_cts = [len(pollution_cts_ok), len(pollution_cts_alerts), len(pollution_cts_expired)]
    len_class_cts = [len(class_cts_ok), len(class_cts_alerts), len(class_cts_expired)]
    len_insurance_cts = [len(insurance_cts_ok), len(insurance_cts_alerts), len(insurance_cts_expired)]
    len_lsa_fa_cts = [len(lsa_fa_cts_ok), len(lsa_fa_cts_alerts), len(lsa_fa_cts_expired)]
    len_health_cts = [len(health_cts_ok), len(health_cts_alerts), len(health_cts_expired)]
    len_others_cts = [len(others_cts_ok), len(others_cts_alerts), len(others_cts_expired)]
    condition = ['Ok', 'Alerts', 'Expired']

    ## Barplot summary
    nat_tonnage_tb_bar3 = bar_plot(len_nat_tonnage_tb, condition)
    solas_tb_bar3 = bar_plot(len_solas_tb, condition)
    pollution_tb_bar3 = bar_plot(len_pollution_tb, condition)
    class_tb_bar3 = bar_plot(len_class_tb, condition)
    insurance_tb_bar3 = bar_plot(len_insurance_tb, condition)
    lsa_fa_tb_bar3 = bar_plot(len_lsa_fa_tb, condition)
    health_tb_bar3 = bar_plot(len_health_tb, condition)
    others_tb_bar3 = bar_plot(len_others_tb, condition)

    nat_tonnage_ba_bar3 = bar_plot(len_nat_tonnage_ba, condition)
    solas_ba_bar3 = bar_plot(len_solas_ba, condition)
    class_ba_bar3 = bar_plot(len_class_ba, condition)
    insurance_ba_bar3 = bar_plot(len_insurance_ba, condition)
    health_ba_bar3 = bar_plot(len_health_ba, condition)
    others_ba_bar3 = bar_plot(len_others_ba, condition)

    nat_tonnage_cts_bar3 = bar_plot(len_nat_tonnage_cts, condition)
    solas_cts_bar3 = bar_plot(len_solas_cts, condition)
    pollution_cts_bar3 = bar_plot(len_pollution_cts, condition)
    class_cts_bar3 = bar_plot(len_class_cts, condition)
    insurance_cts_bar3 = bar_plot(len_insurance_cts, condition)
    lsa_fa_cts_bar3 = bar_plot(len_lsa_fa_cts, condition)
    health_cts_bar3 = bar_plot(len_health_cts, condition)
    others_cts_bar3 = bar_plot(len_others_cts, condition)
    
    return nat_tonnage_tb_bar3, data_nat_tonnage_tb_alerts,\
            solas_tb_bar3, data_solas_tb_alerts,\
            pollution_tb_bar3, data_pollution_tb_alerts,\
            class_tb_bar3, data_class_tb_alerts,\
            insurance_tb_bar3, data_insurance_tb_alerts,\
            lsa_fa_tb_bar3, data_lsa_fa_tb_alerts,\
            health_tb_bar3, data_health_tb_alerts,\
            others_tb_bar3, data_others_tb_alerts,\
            nat_tonnage_ba_bar3, data_nat_tonnage_ba_alerts,\
            solas_ba_bar3, data_solas_ba_alerts,\
            class_ba_bar3, data_class_ba_alerts,\
            insurance_ba_bar3, data_insurance_ba_alerts,\
            health_ba_bar3, data_health_ba_alerts,\
            others_ba_bar3, data_others_ba_alerts,\
            nat_tonnage_cts_bar3, data_nat_tonnage_cts_alerts,\
            solas_cts_bar3, data_solas_cts_alerts,\
            pollution_cts_bar3, data_pollution_cts_alerts,\
            class_cts_bar3, data_class_cts_alerts,\
            insurance_cts_bar3, data_insurance_cts_alerts,\
            lsa_fa_cts_bar3, data_lsa_fa_cts_alerts,\
            health_cts_bar3, data_health_cts_alerts,\
            others_cts_bar3, data_others_cts_alerts,


######################
# Plot Function
######################
## 1. 'Nationality & Tonnage Remain Days'
def nat_tonnage_classify(df):
    
    expired = pd.DataFrame()
    alerts = pd.DataFrame()
    ok = pd.DataFrame()

    for i in range(len(df['Nationality & Tonnage Remain Days'])) :
        if df['Nationality & Tonnage Remain Days'][i] < 0 :
            expired = expired.append({'Vessel': df.iloc[:,0][i],
                                    'Remaining Days': df.loc[:,'Nationality & Tonnage Remain Days2'][i],
                                    'Due Date': df.loc[:,'Nationality & Tonnage'][i]}, ignore_index=True)
        elif df['Nationality & Tonnage Remain Days'][i] < 30 :
            alerts = alerts.append({'Vessel': df.iloc[:,0][i],
                                     'Remaining Days': df.loc[:,'Nationality & Tonnage Remain Days2'][i],
                                     'Due Date': df.loc[:,'Nationality & Tonnage'][i]}, ignore_index=True)
        else :
            ok = ok.append({'Vessel': df.iloc[:,0][i],
                            'Remaining Days': df.loc[:,'Nationality & Tonnage Remain Days2'][i],
                            'Due Date': df.loc[:,'Nationality & Tonnage'][i]}, ignore_index=True)
    return(expired, alerts, ok)

## 2. 'SOLAS Remain Days'
def solas_classify(df):
    
    expired = pd.DataFrame()
    alerts = pd.DataFrame()
    ok = pd.DataFrame()

    for i in range(len(df['SOLAS Remain Days'])) :
        if df['SOLAS Remain Days'][i] < 0 :
            expired = expired.append({'Vessel': df.iloc[:,0][i],
                                    'Remaining Days': df.loc[:,'SOLAS Remain Days2'][i],
                                    'Due Date': df.loc[:,'SOLAS'][i]}, ignore_index=True)
        elif df['SOLAS Remain Days'][i] < 30 :
            alerts = alerts.append({'Vessel': df.iloc[:,0][i],
                                     'Remaining Days': df.loc[:,'SOLAS Remain Days2'][i],
                                     'Due Date': df.loc[:,'SOLAS'][i]}, ignore_index=True)
        else :
            ok = ok.append({'Vessel': df.iloc[:,0][i],
                            'Remaining Days': df.loc[:,'SOLAS Remain Days2'][i],
                            'Due Date': df.loc[:,'SOLAS'][i]}, ignore_index=True)
    return(expired, alerts, ok)

## 3. 'Pollution Remain Days'
def pollution_classify(df):
    
    expired = pd.DataFrame()
    alerts = pd.DataFrame()
    ok = pd.DataFrame()

    for i in range(len(df['Pollution Remain Days'])) :
        if df['Pollution Remain Days'][i] < 0 :
            expired = expired.append({'Vessel': df.iloc[:,0][i],
                                    'Remaining Days': df.loc[:,'Pollution Remain Days2'][i],
                                    'Due Date': df.loc[:,'Pollution'][i]}, ignore_index=True)
        elif df['Pollution Remain Days'][i] < 30 :
            alerts = alerts.append({'Vessel': df.iloc[:,0][i],
                                     'Remaining Days': df.loc[:,'Pollution Remain Days2'][i],
                                     'Due Date': df.loc[:,'Pollution'][i]}, ignore_index=True)
        else :
            ok = ok.append({'Vessel': df.iloc[:,0][i],
                            'Remaining Days': df.loc[:,'Pollution Remain Days2'][i],
                            'Due Date': df.loc[:,'Pollution'][i]}, ignore_index=True)
    return(expired, alerts, ok)

## 4. 'Class Remain Days'
def class_classify(df):
    
    expired = pd.DataFrame()
    alerts = pd.DataFrame()
    ok = pd.DataFrame()

    for i in range(len(df['Class Remain Days'])) :
        if df['Class Remain Days'][i] < 0 :
            expired = expired.append({'Vessel': df.iloc[:,0][i],
                                    'Remaining Days': df.loc[:,'Class Remain Days2'][i],
                                    'Due Date': df.loc[:,'Class'][i]}, ignore_index=True)
        elif df['Class Remain Days'][i] < 30 :
            alerts = alerts.append({'Vessel': df.iloc[:,0][i],
                                     'Remaining Days': df.loc[:,'Class Remain Days2'][i],
                                     'Due Date': df.loc[:,'Class'][i]}, ignore_index=True)
        else :
            ok = ok.append({'Vessel': df.iloc[:,0][i],
                            'Remaining Days': df.loc[:,'Class Remain Days2'][i],
                            'Due Date': df.loc[:,'Class'][i]}, ignore_index=True)
    return(expired, alerts, ok)

## 5. 'Insurance Remain Days'
def insurance_classify(df):
    
    expired = pd.DataFrame()
    alerts = pd.DataFrame()
    ok = pd.DataFrame()

    for i in range(len(df['Insurance Remain Days'])) :
        if df['Insurance Remain Days'][i] < 0 :
            expired = expired.append({'Vessel': df.iloc[:,0][i],
                                    'Remaining Days': df.loc[:,'Insurance Remain Days2'][i],
                                    'Due Date': df.loc[:,'Insurance'][i]}, ignore_index=True)
        elif df['Insurance Remain Days'][i] < 30 :
            alerts = alerts.append({'Vessel': df.iloc[:,0][i],
                                     'Remaining Days': df.loc[:,'Insurance Remain Days2'][i],
                                     'Due Date': df.loc[:,'Insurance'][i]}, ignore_index=True)
        else :
            ok = ok.append({'Vessel': df.iloc[:,0][i],
                            'Remaining Days': df.loc[:,'Insurance Remain Days2'][i],
                            'Due Date': df.loc[:,'Insurance'][i]}, ignore_index=True)
    return(expired, alerts, ok)

## 6. 'LSA & FFA Remain Days'
def lsa_ffa_classify(df):
    
    expired = pd.DataFrame()
    alerts = pd.DataFrame()
    ok = pd.DataFrame()

    for i in range(len(df['LSA & FFA Remain Days'])) :
        if df['LSA & FFA Remain Days'][i] < 0 :
            expired = expired.append({'Vessel': df.iloc[:,0][i],
                                    'Remaining Days': df.loc[:,'LSA & FFA Remain Days2'][i],
                                    'Due Date': df.loc[:,'LSA & FFA'][i]}, ignore_index=True)
        elif df['LSA & FFA Remain Days'][i] < 30 :
            alerts = alerts.append({'Vessel': df.iloc[:,0][i],
                                     'Remaining Days': df.loc[:,'LSA & FFA Remain Days2'][i],
                                     'Due Date': df.loc[:,'LSA & FFA'][i]}, ignore_index=True)
        else :
            ok = ok.append({'Vessel': df.iloc[:,0][i],
                            'Remaining Days': df.loc[:,'LSA & FFA Remain Days2'][i],
                            'Due Date': df.loc[:,'LSA & FFA'][i]}, ignore_index=True)
    return(expired, alerts, ok)

## 7. 'Health Remain Days'
def health_classify(df):
    
    expired = pd.DataFrame()
    alerts = pd.DataFrame()
    ok = pd.DataFrame()

    for i in range(len(df['Health Remain Days'])) :
        if df['Health Remain Days'][i] < 0 :
            expired = expired.append({'Vessel': df.iloc[:,0][i],
                                    'Remaining Days': df.loc[:,'Health Remain Days2'][i],
                                    'Due Date': df.loc[:,'Health'][i]}, ignore_index=True)
        elif df['Health Remain Days'][i] < 30 :
            alerts = alerts.append({'Vessel': df.iloc[:,0][i],
                                     'Remaining Days': df.loc[:,'Health Remain Days2'][i],
                                     'Due Date': df.loc[:,'Health'][i]}, ignore_index=True)
        else :
            ok = ok.append({'Vessel': df.iloc[:,0][i],
                            'Remaining Days': df.loc[:,'Health Remain Days2'][i],
                            'Due Date': df.loc[:,'Health'][i]}, ignore_index=True)
    return(expired, alerts, ok)

## 8. 'Others Remain Days'
def others_classify(df):
    
    expired = pd.DataFrame()
    alerts = pd.DataFrame()
    ok = pd.DataFrame()

    for i in range(len(df['Others Remain Days'])) :
        if df['Others Remain Days'][i] < 0 :
            expired = expired.append({'Vessel': df.iloc[:,0][i],
                                    'Remaining Days': df.loc[:,'Others Remain Days2'][i],
                                    'Due Date': df.loc[:,'Others'][i]}, ignore_index=True)
        elif df['Others Remain Days'][i] < 30 :
            alerts = alerts.append({'Vessel': df.iloc[:,0][i],
                                     'Remaining Days': df.loc[:,'Others Remain Days2'][i],
                                     'Due Date': df.loc[:,'Others'][i]}, ignore_index=True)
        else :
            ok = ok.append({'Vessel': df.iloc[:,0][i],
                            'Remaining Days': df.loc[:,'Others Remain Days2'][i],
                            'Due Date': df.loc[:,'Others'][i]}, ignore_index=True)
    return(expired, alerts, ok)


## 9. Bar Plot
def bar_plot(len, condition) :
    fig = go.Figure(go.Bar(y=len,
                            x=condition,
                            text=len,
                            marker_color=['#02b875','#f0ad4e','#d9534f']))
    fig.update_layout({'height':185, 
                        'width':160,
                        'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                        'margin' : {'t':3, 'b':3, 'l':3, 'r':3}})

    return fig

## 10. Tooltip
def tooltip_table(df):
    if df.empty == True :
        tooltip = []
    else :
        df['Last Date'] = df['Last Date'].dt.strftime('%d/%m/%Y')
        df['Due Date'] =  df['Due Date'].dt.strftime('%d/%m/%Y')
        tooltip =[{
            'Remaining Days': {'value': 'Last Date: {}  \nDue Date: {}'.format(row['Last Date'], row['Due Date']), 'type': 'markdown', },
        } for row in df.to_dict('records')]
    return tooltip




    