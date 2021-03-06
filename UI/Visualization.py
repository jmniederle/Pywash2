import dash_html_components as html
import dash_core_components as dcc
import dash_table
def VisualizationUI():
    return html.Div(
        id = 'Visualization',
        children = [
            html.H3(
                children = "Now, let's have a closer look!",
                style = {'textAlign':'center'}
            ),
            html.Div(
                id = 'result_data',
                children = [
                    html.Div(
                        [
                            html.H5("Data Preview"),
                            dash_table.DataTable(
                                id='ResultDataTable',
                            ),
                        ],
                    ),
                ],
            ),
        ],
        style = {'display': 'none'}
    )
