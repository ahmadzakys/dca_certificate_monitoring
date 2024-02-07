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
import itertools
dash.register_page(__name__,  name='Status') # '/' is home page

##-----page 2

## -----LAYOUT-----
layout = html.Div([
                html.Br(),
                        html.P(children=html.Strong('MONITORING CERTIFICATE'),
                               style={'textAlign': 'center', 'fontSize': 27, 'background-color':'#F1F4F4','color':'#242947','font-family':'Verdana'}),
                dcc.Tabs([
                    dcc.Tab(label='Tug Boat', children=[
                        html.Br(),
                        html.Div(dcc.Dropdown(
                            id='tugboat-dropdown',
                            options=[
                                {'label': 'TB. PERKASA 2', 'value': 'PERKASA2'},
                                {'label': 'TB. PERKASA 3', 'value': 'PERKASA3'},
                                {'label': 'TB. PERKASA 11', 'value': 'PERKASA11'},
                                {'label': 'TB. PERKASA 12', 'value': 'PERKASA12'},
                                {'label': 'TB. PERKASA 13', 'value': 'PERKASA13'},
                                {'label': 'TB. SELWYN 1', 'value': 'SELWYN1'},
                                {'label': 'TB. BERAU 21', 'value': 'BERAU21'},
                                {'label': 'TB. BERAU 22', 'value': 'BERAU22'},
                                {'label': 'TB. TENANG 1601', 'value': 'TENANG1601'},
                                {'label': 'TB. TENANG 1602', 'value': 'TENANG1602'},
                                {'label': 'TB. TENANG 2001', 'value': 'TENANG2001'},
                                {'label': 'TB. BINTANG 1603', 'value': 'BINTANG1603'},
                                {'label': 'TB. BINTANG 2002', 'value': 'BINTANG2002'},
                                {'label': 'TB. BINTANG 2003', 'value': 'BINTANG2003'},
                            ],
                            value='PERKASA2',
                            style={
                                'width':'97.5%',
                                'paddingLeft':'4%',
                                }
                        )),
                        html.Br(),
                        html.Div([dash_table.DataTable(
                            id='tugboat-table',
                            columns=[{'name':'CERTIFICATE','id': 'Certificate'},
                                    {'name':'REMAINING DAYS','id': 'Remaining Days'},
                                    {'name':'EXPIRY DATE','id': 'Expiry Date'},
                                    {'name':'STATUS','id': 'Status'},],
                            merge_duplicate_headers=True,
                            # style_as_list_view=True,
                            style_header={'backgroundColor': '#2a3f5f',
                                        'fontWeight': 'bold',
                                        'color':'white',
                                        'border': '1px solid white',
                                        'textAlign': 'center'
                                    },
                            style_cell_conditional=[{'if': {'column_id': 'Certificate'},
                                                    'textAlign': 'left'},
                                                    {'if': {'column_id': 'Remaining Days'},
                                                    'textAlign': 'center'},
                                                    {'if': {'column_id': 'Expiry Date'},
                                                    'textAlign': 'center'},
                                                    {'if': {'column_id': 'Status'},
                                                    'textAlign': 'center'},
                                                    ],
                            style_cell={'font-family':'Verdana',
                                        'fontSize': 15,
                                        'color':'#2a3f5f'},
                            style_data_conditional=(
                                [
                                    {'if': {'filter_query': '{{{col}}} eq "✔️"'.format(col=col),
                                            'column_id': ['Status', 'Certificate', 'Remaining Days', 'Expiry Date']},
                                    'backgroundColor': '#dfd'} for col in ['Status']
                                ] +
                                [
                                    {'if': {'filter_query': '{{{col}}} eq "🔲"'.format(col=col),
                                            'column_id': ['Status', 'Certificate', 'Remaining Days', 'Expiry Date']},
                                    'backgroundColor': '#dfd'} for col in ['Status']
                                ] +
                                [
                                    {'if': {'filter_query': '{{{col}}} eq "⚠️"'.format(col=col),
                                            'column_id': ['Status', 'Certificate', 'Remaining Days', 'Expiry Date']},
                                    'backgroundColor': '#ffd'} for col in ['Status']
                                ] +
                                [
                                    {'if': {'filter_query': '{{{col}}} eq "❌"'.format(col=col),
                                            'column_id': ['Status', 'Certificate', 'Remaining Days', 'Expiry Date']},
                                    'backgroundColor': '#fdd'} for col in ['Status']
                                ] +
                                [
                                    {'if': {'column_id': 'Certificate',},
                                    'fontWeight': 'bold'},    
                                ]
                                ),
                            css=[{
                                'selector': '.dash-table-tooltip',
                                'rule': 'background-color: white; font-family: Verdana; font-size: 10; color: #2a3f5f;'}],
                            tooltip_delay=0,
                            tooltip_duration=None
                        )], style={
                                'width':'90%',
                                'paddingLeft':'4%',
                                }),
                    ]),
                    dcc.Tab(label='Barge', children=[
                        html.Br(),
                        html.Div(dcc.Dropdown(
                            id='barge-dropdown',
                            options=[
                                {'label': 'BA. PSPM 2', 'value': 'PSPM2'},
                                {'label': 'BA. PSPM 3', 'value': 'PSPM3'},
                                {'label': 'BA. PSPM 11', 'value': 'PSPM11'},
                                {'label': 'BA. PSPM 12', 'value': 'PSPM12'},
                                {'label': 'BA. PSPM 13', 'value': 'PSPM13'},
                                {'label': 'BA. PSPM 21', 'value': 'PSPM21'},
                                {'label': 'BA. PSPM 22', 'value': 'PSPM22'},
                                {'label': 'BA. SOEKAWATI 808', 'value': 'SOEKAWATI808'},
                                {'label': 'BA. SOEKAWATI 909', 'value': 'SOEKAWATI909'},
                                {'label': 'BA. TERANG 3001', 'value': 'TERANG3001'},
                                {'label': 'BA. TERANG 3003', 'value': 'TERANG3003'},
                                {'label': 'BA. TERANG 3005', 'value': 'TERANG3005'},
                                {'label': 'BA. TERANG 2701', 'value': 'TERANG2701'},
                            ],
                            value='PSPM2',
                            style={
                                'width':'95%',
                                'paddingLeft':'8%',
                                }
                        )),
                        html.Br(),
                        html.Div([dash_table.DataTable(
                            id='barge-table',
                            columns=[{'name':'CERTIFICATE','id': 'Certificate'},
                                    {'name':'REMAINING DAYS','id': 'Remaining Days'},
                                    {'name':'EXPIRY DATE','id': 'Expiry Date'},
                                    {'name':'STATUS','id': 'Status'},],
                            merge_duplicate_headers=True,
                            # style_as_list_view=True,
                            style_header={'backgroundColor': '#2a3f5f',
                                        'fontWeight': 'bold',
                                        'color':'white',
                                        'border': '1px solid white',
                                        'textAlign': 'center'
                                    },
                            style_cell_conditional=[{'if': {'column_id': 'Certificate'},
                                                    'textAlign': 'left'},
                                                    {'if': {'column_id': 'Remaining Days'},
                                                    'textAlign': 'center'},
                                                    {'if': {'column_id': 'Expiry Date'},
                                                    'textAlign': 'center'},
                                                    {'if': {'column_id': 'Status'},
                                                    'textAlign': 'center'},
                                                    ],
                            style_cell={'font-family':'Verdana',
                                        'fontSize': 15,
                                        'color':'#2a3f5f'},
                            style_data_conditional=(
                                [
                                    {'if': {'filter_query': '{{{col}}} eq "✔️"'.format(col=col),
                                            'column_id': ['Status', 'Certificate', 'Remaining Days', 'Expiry Date']},
                                    'backgroundColor': '#dfd'} for col in ['Status']
                                ] +
                                [
                                    {'if': {'filter_query': '{{{col}}} eq "🔲"'.format(col=col),
                                            'column_id': ['Status', 'Certificate', 'Remaining Days', 'Expiry Date']},
                                    'backgroundColor': '#dfd'} for col in ['Status']
                                ] +
                                [
                                    {'if': {'filter_query': '{{{col}}} eq "⚠️"'.format(col=col),
                                            'column_id': ['Status', 'Certificate', 'Remaining Days', 'Expiry Date']},
                                    'backgroundColor': '#ffd'} for col in ['Status']
                                ] +
                                [
                                    {'if': {'filter_query': '{{{col}}} eq "❌"'.format(col=col),
                                            'column_id': ['Status', 'Certificate', 'Remaining Days', 'Expiry Date']},
                                    'backgroundColor': '#fdd'} for col in ['Status']
                                ] +
                                [
                                    {'if': {'column_id': 'Certificate',},
                                    'fontWeight': 'bold'},    
                                ]
                                ),
                            css=[{
                                'selector': '.dash-table-tooltip',
                                'rule': 'background-color: white; font-family: Verdana; font-size: 10; color: #2a3f5f;'}],
                            tooltip_delay=0,
                            tooltip_duration=None
                        )], style={
                                'width':'90%',
                                'paddingLeft':'8%',
                                }),
                        
                    ]),
                    dcc.Tab(label='CTS', children=[
                        html.Br(),
                        html.Div(dcc.Dropdown(
                            id='cts-dropdown',
                            options=[
                                {'label': 'BULK SUMATRA', 'value': 'SUMATRA'},
                                {'label': 'BULK KARIMUN', 'value': 'KARIMUN'},
                                {'label': 'BULK NATUNA', 'value': 'NATUNA'},
                                {'label': 'BULK DERAWAN', 'value': 'DERAWAN'},
                                {'label': 'BULK JAVA', 'value': 'JAVA'},
                                {'label': 'BULK DEWATA', 'value': 'DEWATA'},
                                {'label': 'BULK SUMBA', 'value': 'SUMBA'},
                            ],
                            value='SUMATRA',
                            style={
                                'width':'97.5%',
                                'paddingLeft':'4%',
                                }
                        )),
                        html.Br(),
                        html.Div([dash_table.DataTable(
                            id='cts-table',
                            columns=[{'name':'CERTIFICATE','id': 'Certificate'},
                                    {'name':'REMAINING DAYS','id': 'Remaining Days'},
                                    {'name':'EXPIRY DATE','id': 'Expiry Date'},
                                    {'name':'STATUS','id': 'Status'},],
                            merge_duplicate_headers=True,
                            # style_as_list_view=True,
                            style_header={'backgroundColor': '#2a3f5f',
                                        'fontWeight': 'bold',
                                        'color':'white',
                                        'border': '1px solid white',
                                        'textAlign': 'center'
                                    },
                            style_cell_conditional=[{'if': {'column_id': 'Certificate'},
                                                    'textAlign': 'left'},
                                                    {'if': {'column_id': 'Remaining Days'},
                                                    'textAlign': 'center'},
                                                    {'if': {'column_id': 'Expiry Date'},
                                                    'textAlign': 'center'},
                                                    {'if': {'column_id': 'Status'},
                                                    'textAlign': 'center'},
                                                    ],
                            style_cell={'font-family':'Verdana',
                                        'fontSize': 15,
                                        'color':'#2a3f5f'},
                            style_data_conditional=(
                                [
                                    {'if': {'filter_query': '{{{col}}} eq "✔️"'.format(col=col),
                                            'column_id': ['Status', 'Certificate', 'Remaining Days', 'Expiry Date']},
                                    'backgroundColor': '#dfd'} for col in ['Status']
                                ] +
                                [
                                    {'if': {'filter_query': '{{{col}}} eq "🔲"'.format(col=col),
                                            'column_id': ['Status', 'Certificate', 'Remaining Days', 'Expiry Date']},
                                    'backgroundColor': '#dfd'} for col in ['Status']
                                ] +
                                [
                                    {'if': {'filter_query': '{{{col}}} eq "⚠️"'.format(col=col),
                                            'column_id': ['Status', 'Certificate', 'Remaining Days', 'Expiry Date']},
                                    'backgroundColor': '#ffd'} for col in ['Status']
                                ] +
                                [
                                    {'if': {'filter_query': '{{{col}}} eq "❌"'.format(col=col),
                                            'column_id': ['Status', 'Certificate', 'Remaining Days', 'Expiry Date']},
                                    'backgroundColor': '#fdd'} for col in ['Status']
                                ] +
                                [
                                    {'if': {'column_id': 'Certificate',},
                                    'fontWeight': 'bold'},    
                                ]
                                ),
                            css=[{
                                'selector': '.dash-table-tooltip',
                                'rule': 'background-color: white; font-family: Verdana; font-size: 10; color: #2a3f5f;'}],
                            tooltip_delay=0,
                            tooltip_duration=None
                        )], style={
                                'width':'90%',
                                'paddingLeft':'4%',
                                }),
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
    Output('tugboat-table', 'data'),
    Output('barge-table', 'data'),
    Output('cts-table', 'data'),
    ],

    [Input('store', 'data'),
    Input('tugboat-dropdown', 'value'),
    Input('barge-dropdown', 'value'),
    Input('cts-dropdown', 'value')]
)
def update_charts(data, value_tb, value_ba, value_cts):
    ######################
    # Pre Processing
    ######################
    # Tug Boat
    ######################
    df_tb = pd.DataFrame(data['Tugboat'])

    ### datetime variable
    col = df_tb.columns
    col = list(col)

    no_date = ['NO', 'NAMA KAPAL', 'NAMA PEMILIK', 'YEARD OF BUILD', 'SURAT UKUR INTERNATIONAL (INTERNATIONAL TONNAGE CERTIFICATE)', 
            '3/6/12 BULAN', ]
    col = [x for x in col if x not in no_date]

    ### apply datetime to selected variable
    df_tb = df_tb.replace(r'^\s*$', np.nan, regex=True)
    df_tb[col] = df_tb[col].apply(pd.to_datetime, format='%d %B %Y')

    ### remove unnecessary variable
    col_del = ['NO', 'NAMA PEMILIK', 'YEARD OF BUILD', 'SURAT UKUR INTERNATIONAL (INTERNATIONAL TONNAGE CERTIFICATE)',
            '3/6/12 BULAN', 'NOTA DINAS 1', 'NOTA DINAS 2']
    col_stay = [x for x in df_tb.columns if x not in col_del]

    ### set 'NAMA KAPAL' as index
    df_tb = df_tb[df_tb['NAMA PEMILIK'] == 'PT. DCA']
    df_tb = df_tb[col_stay].set_index('NAMA KAPAL')

    ### making new dataframe for remaining days only
    df_tb_days = df_tb.copy()
    for i in df_tb:
        df_tb_days[i] = (df_tb[i]-pd.to_datetime('today')).dt.days

    ### making new dataframe for status with emoji using df_tb_days
    df_tb_status = df_tb_days.copy()
    for i in df_tb_days:
        df_tb_status[i] = df_tb_status[i].apply(lambda x:
                                                '❌' if x < 0 else (
                                                    '⚠️' if x < 30 else(
                                                        '🔲' if pd.isna(x) else '✔️')))
    
    ### making new dataframe for remaining days aggregate within months
    df_tb_months = df_tb.copy()

    # Function for calculating remaining days
    def date_diff(var):
        remaining =[]
        for i in var:
            if i is pd.NaT:
                remaining.append(pd.Timestamp('NaT'))
            else :
                delta = relativedelta(i, pd.to_datetime('today'))
                if (delta.years == 0 and delta.months == 0):
                    remaining.append((str(delta.days)+ ' days'))
                else :
                    res_months = delta.months + (delta.years * 12)
                    remaining.append((str(res_months)+ ' months, '+ str(delta.days)+ ' days'))
        return(remaining)

    for i in df_tb:
        df_tb_months[i] = date_diff(df_tb[i])

    ### seperate all dataframe by 'NAMA KAPAL'
    nama_df = ['PERKASA2','PERKASA3','PERKASA11','PERKASA12','PERKASA13','SELWYN1','BERAU21',
                'BERAU22','TENANG1601','BINTANG1603','BINTANG2003','TENANG2001','TENANG1602',
                'BINTANG2002']
    dict_tb = {}
    for i,j in zip(df_tb.index, nama_df):
        days = pd.DataFrame(df_tb_months.loc[i]).reset_index().rename(columns={'index':'Certificate',
                                                                                i:'Remaining Days'})
        exp = pd.DataFrame(df_tb.loc[i]).reset_index().rename(columns={'index':'Certificate',
                                                                                    i:'Expiry Date'})
        status = pd.DataFrame(df_tb_status.loc[i]).reset_index().rename(columns={'index':'Certificate',
                                                                                    i:'Status'})

        df = days.join(exp['Expiry Date']).join(status['Status'])

        df = df.sort_values(by=['Expiry Date'])
        df['Expiry Date'] = df['Expiry Date'].dt.strftime('%d/%m/%Y')
        dict_tb.update({j:df})

    PERKASA2 = dict_tb['PERKASA2']
    PERKASA3 = dict_tb['PERKASA3']
    PERKASA11 = dict_tb['PERKASA11']
    PERKASA12 = dict_tb['PERKASA12']
    PERKASA13 = dict_tb['PERKASA13']
    SELWYN1 = dict_tb['SELWYN1']
    BERAU21 = dict_tb['BERAU21']
    BERAU22 = dict_tb['BERAU22']
    TENANG1601 = dict_tb['TENANG1601']
    BINTANG1603 = dict_tb['BINTANG1603']
    BINTANG2003 = dict_tb['BINTANG2003']
    TENANG2001 = dict_tb['TENANG2001']
    TENANG1602 = dict_tb['TENANG1602']
    BINTANG2002 = dict_tb['BINTANG2002']

    ######################
    # Barge
    ######################
    df_ba = pd.DataFrame(data['Barge'])

    ### datetime variable
    col_ba = df_ba.columns

    col_ba = list(col_ba)

    no_date = ['NO', 'NAMA KAPAL', 'NAMA PEMILIK', 'YEARD OF BUILD', 'SURAT UKUR INTERNATIONAL (INTERNATIONAL TONNAGE CERTIFICATE)', 
            '3/6/12 BULAN', ]
    col_ba = [x for x in col_ba if x not in no_date]

    ### apply datetime to selected variable
    df_ba = df_ba.replace(r'^\s*$', np.nan, regex=True)
    df_ba[col_ba] = df_ba[col_ba].apply(pd.to_datetime, format='%d %B %Y')

    ### remove unnecessary variable
    col_del_ba = ['NO', 'NAMA PEMILIK','YEARD OF BUILD', 'SURAT UKUR INTERNATIONAL (INTERNATIONAL TONNAGE CERTIFICATE)',
                  '3/6/12 BULAN', 'NOTA DINAS 1', 'NOTA DINAS 2']
    col_stay_ba = [x for x in df_ba.columns if x not in col_del_ba]

    ### set 'NAMA KAPAL' as index
    df_ba = df_ba[df_ba['NAMA PEMILIK'] == 'PT. DCA']
    df_ba = df_ba[col_stay_ba].set_index('NAMA KAPAL')

    ### making new dataframe for remaining days only
    df_ba_days = df_ba.copy()
    for i in df_ba:
        df_ba_days[i] = (df_ba[i]-pd.to_datetime('today')).dt.days

    ### making new dataframe for status with emoji using df_tb_days
    df_ba_status = df_ba_days.copy()
    for i in df_ba_days:
        df_ba_status[i] = df_ba_status[i].apply(lambda x:
                                                '❌' if x < 0 else (
                                                    '⚠️' if x < 30 else(
                                                        '🔲' if pd.isna(x) else '✔️')))
    
    ### making new dataframe for remaining days aggregate within months
    df_ba_months = df_ba.copy()

    # Function for calculating remaining days
    def date_diff(var):
        remaining =[]
        for i in var:
            if i is pd.NaT:
                remaining.append(pd.Timestamp('NaT'))
            else :
                delta = relativedelta(i, pd.to_datetime('today'))
                if (delta.years == 0 and delta.months == 0):
                    remaining.append((str(delta.days)+ ' days'))
                else :
                    res_months = delta.months + (delta.years * 12)
                    remaining.append((str(res_months)+ ' months, '+ str(delta.days)+ ' days'))
        return(remaining)

    for i in df_ba:
        df_ba_months[i] = date_diff(df_ba_months[i])

    ### seperate all dataframe by 'NAMA KAPAL'
    nama_df_ba = ['PSPM2', 'PSPM3', 'PSPM11', 'PSPM12', 'PSPM13', 'PSPM21', 
                  'PSPM22', 'SOEKAWATI808', 'SOEKAWATI909', 'TERANG3001', 'TERANG3003',
                  'TERANG3005', 'TERANG2701']
    dict_ba = {}
    for i,j in zip(df_ba.index, nama_df_ba):
        days_ba = pd.DataFrame(df_ba_months.loc[i]).reset_index().rename(columns={'index':'Certificate',
                                                                                i:'Remaining Days'})
        exp_ba = pd.DataFrame(df_ba.loc[i]).reset_index().rename(columns={'index':'Certificate',
                                                                                    i:'Expiry Date'})
        status_ba = pd.DataFrame(df_ba_status.loc[i]).reset_index().rename(columns={'index':'Certificate',
                                                                                    i:'Status'})

        df = days_ba.join(exp_ba['Expiry Date']).join(status_ba['Status'])

        df = df.sort_values(by=['Expiry Date'])
        df['Expiry Date'] = df['Expiry Date'].dt.strftime('%d/%m/%Y')
        dict_ba.update({j:df})

    PSPM2 = dict_ba['PSPM2']
    PSPM3 = dict_ba['PSPM3']
    PSPM11 = dict_ba['PSPM11']
    PSPM12 = dict_ba['PSPM12']
    PSPM13 = dict_ba['PSPM13']
    PSPM21 = dict_ba['PSPM21']
    PSPM22 = dict_ba['PSPM22']
    SOEKAWATI808 = dict_ba['SOEKAWATI808']
    SOEKAWATI909 = dict_ba['SOEKAWATI909']
    TERANG3001 = dict_ba['TERANG3001']
    TERANG3003 = dict_ba['TERANG3003']
    TERANG3005 = dict_ba['TERANG3005']
    TERANG2701 = dict_ba['TERANG2701']

    ######################
    # CTS
    ######################
    df_cts = pd.DataFrame(data['CTS'])

    ### datetime variable
    col = df_cts.columns
    col = list(col)

    no_date_cts = ['NO', 'NAMA KAPAL', 'NAMA PEMILIK', 'YEARD OF BUILD', 'SURAT UKUR INTERNATIONAL (INTERNATIONAL TONNAGE CERTIFICATE)', 
            '3/6/12 BULAN', 'SPESIAL SURVEY']
    col = [x for x in col if x not in no_date_cts]

    ### apply datetime to selected variable
    df_cts = df_cts.replace(r'^\s*$', np.nan, regex=True)
    df_cts[col] = df_cts[col].apply(pd.to_datetime, format='%d %B %Y')

    ### remove unnecessary variable
    col_del_cts = ['NO', 'NAMA PEMILIK','INTERMEDATE SURVEY',	'SPESIAL SURVEY',	"INTERMEDATE SURVEY2",	'SPESIAL SURVEY2',	'INTERMEDATE SURVEY3',
            'SPESIAL SURVEY3', 'SURAT UKUR INTERNATIONAL (INTERNATIONAL TONNAGE CERTIFICATE)',
            '3/6/12 BULAN', 'NEXT RENEWAL SYABANDAR','NOTA DINAS 1', 'NOTA DINAS 2',
            'NEXT ANNUAL', 'REMOVAL OF WRECKS1', 'HULL & MACHINE', 'CERTIFIACATE DOCUMENT OF COMPLAINCE', ]
    col_stay_cts = [x for x in df_cts.columns if x not in col_del_cts]

    ### set 'NAMA KAPAL' as index
    df_cts = df_cts[df_cts['NAMA PEMILIK'] == 'PT. ABL']
    df_cts = df_cts[col_stay_cts].set_index('NAMA KAPAL')

    ### making new dataframe for remaining days only
    df_cts_days = df_cts.copy()
    for i in df_cts:
        df_cts_days[i] = (df_cts[i]-pd.to_datetime('today')).dt.days

    ### making new dataframe for status with emoji using df_tb_days
    df_cts_status = df_cts_days.copy()
    for i in df_cts_days:
        df_cts_status[i] = df_cts_status[i].apply(lambda x:
                                                '❌' if x < 0 else (
                                                    '⚠️' if x < 30 else(
                                                        '🔲' if pd.isna(x) else '✔️')))
    
    ### making new dataframe for remaining days aggregate within months
    df_cts_months = df_cts.copy()

    # Function for calculating remaining days
    def date_diff(var):
        remaining =[]
        for i in var:
            if i is pd.NaT:
                remaining.append(pd.Timestamp('NaT'))
            else :
                delta = relativedelta(i, pd.to_datetime('today'))
                if (delta.years == 0 and delta.months == 0):
                    remaining.append((str(delta.days)+ ' days'))
                else :
                    res_months = delta.months + (delta.years * 12)
                    remaining.append((str(res_months)+ ' months, '+ str(delta.days)+ ' days'))
        return(remaining)

    for i in df_cts:
        df_cts_months[i] = date_diff(df_cts[i])

    ### seperate all dataframe by 'NAMA KAPAL'
    nama_df_cts = ['SUMATRA', 'KARIMUN', 'NATUNA', 'DERAWAN', 'JAVA', 'DEWATA', 'SUMBA']
    dict_cts = {}
    for i,j in zip(df_cts.index, nama_df_cts):
        days = pd.DataFrame(df_cts_months.loc[i]).reset_index().rename(columns={'index':'Certificate',
                                                                                i:'Remaining Days'})
        exp = pd.DataFrame(df_cts.loc[i]).reset_index().rename(columns={'index':'Certificate',
                                                                                    i:'Expiry Date'})
        status = pd.DataFrame(df_cts_status.loc[i]).reset_index().rename(columns={'index':'Certificate',
                                                                                    i:'Status'})

        df = days.join(exp['Expiry Date']).join(status['Status'])

        df = df.sort_values(by=['Expiry Date'])
        df['Expiry Date'] = df['Expiry Date'].dt.strftime('%d/%m/%Y')
        dict_cts.update({j:df})
    
    SUMATRA = dict_cts['SUMATRA']
    KARIMUN = dict_cts['KARIMUN']
    NATUNA = dict_cts['NATUNA']
    DERAWAN = dict_cts['DERAWAN']
    JAVA = dict_cts['JAVA']
    DEWATA = dict_cts['DEWATA']
    SUMBA = dict_cts['SUMBA']

    value_name = [['PERKASA2','PERKASA3','PERKASA11','PERKASA12','PERKASA13','SELWYN1','BERAU21','BERAU22',
                    'TENANG1601','TENANG1602','TENANG2001','BINTANG1603','BINTANG2002','BINTANG2003'],
                    ['PSPM2','PSPM3','PSPM11','PSPM12','PSPM13','PSPM21','PSPM22','SOEKAWATI808','SOEKAWATI909',
                    'TERANG3001','TERANG3003','TERANG3005','TERANG2701'],
                    ['SUMATRA','KARIMUN','NATUNA','DERAWAN','JAVA','DEWATA','SUMBA']]
    value_comb = list(itertools.product(*value_name))

    records_name = [[PERKASA2.to_dict('records'),PERKASA3.to_dict('records'),PERKASA11.to_dict('records'),PERKASA12.to_dict('records'),
                    PERKASA13.to_dict('records'),SELWYN1.to_dict('records'),BERAU21.to_dict('records'),BERAU22.to_dict('records'),
                    TENANG1601.to_dict('records'),TENANG1602.to_dict('records'),TENANG2001.to_dict('records'),BINTANG1603.to_dict('records'),
                    BINTANG2002.to_dict('records'),BINTANG2003.to_dict('records')],
                    [PSPM2.to_dict('records'),PSPM3.to_dict('records'),PSPM11.to_dict('records'),PSPM12.to_dict('records'),
                    PSPM13.to_dict('records'),PSPM21.to_dict('records'),PSPM22.to_dict('records'),SOEKAWATI808.to_dict('records'),
                    SOEKAWATI909.to_dict('records'),TERANG3001.to_dict('records'),TERANG3003.to_dict('records'),TERANG3005.to_dict('records'),
                    TERANG2701.to_dict('records')],
                    [SUMATRA.to_dict('records'),KARIMUN.to_dict('records'),NATUNA.to_dict('records'),DERAWAN.to_dict('records'),
                    JAVA.to_dict('records'),DEWATA.to_dict('records'),SUMBA.to_dict('records')]]
    records_comb = list(itertools.product(*records_name))
    
    for i in range(len(value_comb)):
        if (value_tb==value_comb[i][0]) & (value_ba==value_comb[i][1]) & (value_cts==value_comb[i][2]):
            return [records_comb[i][0], records_comb[i][1], records_comb[i][2]]
    
    

    
