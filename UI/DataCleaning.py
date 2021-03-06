import dash_html_components as html
import dash_core_components as dcc
import dash_daq as daq
import dash_table

import pandas as pd

#Example for column types
def DataCleaningUI():
    return html.Div(
        id = 'DataCleaning',
        children = [
        #Cleaning Options Layer 1: Column Type Detecting
            dcc.Store(
                id = 'columnStorage',
            ),
            html.Div(
                id = 'Cleaning_Layer_1',
                children = [
                    html.Div(
                        html.H5("  "), #Creates a white space
                        style = {'width': '5%','display': 'inline-block','vertical-align': 'middle'}
                    ),
                    html.Div(
                        id = 'Column_Type_Changing',
                        children = [
                            html.Div(
                                html.H5("Check and/or change column types"),
                                style = {'width':'100%','display': 'inline-block','textAlign':'center','vertical-align': 'middle'}
                            ),
                            html.Div(
                                children = [
                                    html.Div( #Check updateMapSelect in visualization for example of dynamically changing list entries
                                        dcc.Dropdown(
                                            id = 'dropdown_column_1',
                                            options=[{'label': 'Import data to get started', 'value': '0'}],
                                            value="0",
                                        ),
                                        style = {'width':'60%','display': 'inline-block','vertical-align': 'middle'}
                                    ),
                                    html.Div(
                                        dcc.Dropdown(
                                            id = 'dropdown_column_2',
                                            options=[
                                                {'label': 'Integer', 'value': 'int64'},
                                                {'label': 'Float', 'value': 'float64'},
                                                {'label': 'String', 'value': 'object'},
                                                {'label': 'Boolean', 'value': 'bool'},
                                                {'label': 'Date/Time', 'value': 'datetime64[ns]'},
                                                {'label': 'Categorical', 'value': 'category'},
                                            ],
                                        ),
                                        style = {'width':'40%','display': 'inline-block','vertical-align': 'middle'}
                                    ),
                                ],
                            ),
                        ],
                        style = {'width':'40%','display': 'inline-block','vertical-align': 'middle'}
                    ),
                    html.Div(
                        html.H5("  "), #Creates a white space
                        style = {'width': '10%','display': 'inline-block','vertical-align': 'middle'}
                    ),
                    html.Div(
                        id = 'Anomaly_Checking',
                        children = [
                            html.Div(
                                html.H5("Inspect found anomalies per column, change column type or delete columns that are not anomalous"),
                                style = {'width':'100%','display': 'inline-block','textAlign':'center','vertical-align': 'middle'}
                            ),
                            html.Div(
                                children = [
                                    html.Div(
                                        dcc.Dropdown(
                                            id = 'dropdown_anomaly_1',
                                            options = [{'label': 'Import data to get started', 'value': ''}],
                                            value='',
                                        ),
                                        style = {'width': '60%','display': 'inline-block','vertical-align': 'middle'}
                                    ),
                                    html.Div(
                                        dcc.Dropdown(
                                            id = 'dropdown_anomaly_2',
                                        ),
                                        style = {'width': '40%','display': 'inline-block','vertical-align': 'middle'}
                                    ),
                                ],
                            ),
                            html.Div(
                                html.Button('Selected column does not contain anomalies', id='anomaliesbutton'),
                            ),
                        ],
                        style = {'width':'40%','display': 'inline-block','vertical-align': 'middle'}
                    ),
                    html.Div(
                        html.H5("  "), #Creates a white space
                        style = {'width': '5%','display': 'inline-block','vertical-align': 'middle'}
                    ),
                ],
                style = {'vertical-align': 'middle'}
            ),
        #Cleaning Options Layer 2: Missing Values & Duplicated Rows
            html.Div(
                id = 'Cleaning2',
                children = [
                    html.Div(
                        html.H5("   "), #Creates a white space
                        style = {'width': '40%','display': 'inline-block'}
                    ), #could also put below 2 in 1 div and do width 40%,textalign center on div to center all instead of manual
                    html.Div(
                        id = 'Missing_Values_Box',
                        children = [
                            html.H5("Test for missing values?"),
                            dcc.RadioItems(
                                id = 'missingValues',
                                options=[
                                    {'label': 'No', 'value': '0'},
                                    {'label': 'Yes', 'value': '1'},
                                ],
                                value='1',
                                labelStyle={'display': 'inline-block'}
                            )
                        ],
                        style = {'width': '20%','display': 'inline-block','vertical-align': 'middle'}
                    ),
                    html.Div(
                        id = 'Duplicated_Rows',
                        children = [
                            html.H5("Test for duplicated rows?"),
#                            daq.BooleanSwitch(
#                                id='Duplicated_Rows_Booleanswitch',
#                                on=True
#                            )
                            dcc.RadioItems(
                                id = 'DuplicatedRows',
                                options=[
                                    {'label': 'No', 'value': '0'},
                                    {'label': 'Yes', 'value': '1'},
                                ],
                                value='1',
                                labelStyle={'display': 'inline-block'}
                            )
                        ],
                        style = {'width': '20%','display': 'inline-block','vertical-align': 'middle'}
                    ),
                ],
                style = {'vertical-align': 'middle'}

            ),
            html.Div(
                id = 'outlier handling',
                children = [
                    html.Div([
                            html.Div(
                                html.H5("  "), #Creates a white space
                                style = {'width': '10%','display': 'inline-block','vertical-align': 'middle'}
                            ),
                            html.Div(
                                html.H5('Handle outliers?'),
                                style = {'width': '80%','display': 'inline-block','vertical-align': 'middle'}
                            ),
                            html.Div(
                                html.H5("  "), #Creates a white space
                                style = {'width': '10%','display': 'inline-block','vertical-align': 'middle'}
                            ),
                        ]
                    ),
                    html.Div([
                            html.Div(
                                html.H5("  "), #Creates a white space
                                style = {'width': '10%','display': 'inline-block','vertical-align': 'middle'}
                            ),
                            html.Div(
                                dcc.Dropdown(
                                    id = 'dropdown_outliers',
                                    options=[
                                        {'label': 'No', 'value': '0'},
                                        {'label': 'Yes, mark in an extra column', 'value': '1'},
                                        {'label': 'Yes, remove rows', 'value': '2'}],
                                    multi=False,
                                    value='1'
                                ),
                                style = {'width': '80%','display': 'inline-block','vertical-align': 'middle',}
                            ),
                            html.Div(
                                html.H5("  "), #Creates a white space
                                style = {'width': '10%','display': 'inline-block','vertical-align': 'middle'}
                            ),
                        ]
                    )
                ]
            ),
            html.Div(
                id = 'standardize/Normalize',
                children = [
                    html.Div([
                            html.Div(
                                html.H5("  "), #Creates a white space
                                style = {'width': '10%','display': 'inline-block','vertical-align': 'middle'}
                            ),
                            html.Div(
                                html.H5("Normalize column(s)?"),
                                style = {'width': '80%','display': 'inline-block','vertical-align': 'middle',}
                            ),
                            html.Div(
                                html.H5("  "), #Creates a white space
                                style = {'width': '10%','display': 'inline-block','vertical-align': 'middle'}
                            ),
                        ]
                    ),
                    html.Div([
                            html.Div(
                                html.H5("  "), #Creates a white space
                                style = {'width': '10%','display': 'inline-block','vertical-align': 'middle'}
                            ),
                            html.Div(
                                dcc.Dropdown(
                                    id = 'dropdown_normalization',
                                    options=[{'label': 'Import data to get started', 'value': '0'}],
                                    multi=True,
                                ),
                                style = {'width': '80%','display': 'inline-block','vertical-align': 'middle',}
                            ),
                            html.Div(
                                html.H5("  "), #Creates a white space
                                style = {'width': '10%','display': 'inline-block','vertical-align': 'middle'}
                            ),
                        ]
                    ),
                    html.Div([
                            html.Div(
                                html.H5("  "), #Creates a white space
                                style = {'width': '10%','display': 'inline-block','vertical-align': 'middle'}
                            ),
                            html.Div(
                                html.H5("Standardize column(s)?"),
                                style = {'width': '80%','display': 'inline-block','vertical-align': 'middle',}
                            ),
                            html.Div(
                                html.H5("  "), #Creates a white space
                                style = {'width': '10%','display': 'inline-block','vertical-align': 'middle'}
                            ),
                        ]
                    ),
                    html.Div([
                            html.Div(
                                html.H5("  "), #Creates a white space
                                style = {'width': '10%','display': 'inline-block','vertical-align': 'middle'}
                            ),
                            html.Div(
                                dcc.Dropdown(
                                    id = 'dropdown_standardization',
                                    options=[{'label': 'Import data to get started', 'value': '0'}],
                                    multi=True,
                                ),
                                style = {'width': '80%','display': 'inline-block','vertical-align': 'middle',}
                            ),
                            html.Div(
                                html.H5("  "), #Creates a white space
                                style = {'width': '10%','display': 'inline-block','vertical-align': 'middle'}
                            ),
                        ],
                    ),
                ],
            ),
            html.Div( #empty space
                style = {'height':'40px'},
            ),
            html.Div(
                id = 'temp_button',
                children = [
                    html.Button('Start', id='button'),
                ],
                style = {'width': '100%','textAlign':'center','display': 'inline-block'}
            ),
            html.Div(
                id = 'preview_data',
                children = [
                    html.H3("Data Preview"),
                    dash_table.DataTable(
                        id='PreviewDataTable',
                    ),
                ],
            )
        ],
        style = {'textAlign':'center'}
    )
