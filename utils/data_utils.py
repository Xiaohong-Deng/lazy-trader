import pandas as pd
from pywinauto import application, clipboard
from io import StringIO


def table_to_df(tree_item, table_window):
    tree_item.select()
    table_window.type_keys("^A^C")
    table_string = clipboard.GetData()
    buf = StringIO(table_string)
    df = pd.read_csv(buf, header=0, delim_whitespace=True,
                     index_col=False, dtype=str, error_bad_lines=False)
    return df


def filter_df_by_col_val(df, **kwargs):
    ft = pd.Series([True] * df.shape[0], name='ft')
    for key, val in kwargs.items():
        ft = ft & (df[key] == val)
    return df[ft]
