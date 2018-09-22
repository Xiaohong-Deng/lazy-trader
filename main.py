from pywinauto import application, clipboard
from io import StringIO
import numpy as np
import pandas as pd

app = application.Application(backend="uia").connect(path="C:\全能行证券交易终端\\xiadan.exe")
dlg = app['Dialog']['网上股票交易系统5.0']
dialogs = app.windows()
dlg['control']
dlg.print_control_identifiers()
first_panel = dlg.child_window(auto_id="59648", ctrl_index=0)
first_panel.print_control_identifiers()

# get text
my_stock_list = first_panel.child_window(title="Custom1", control_type="Pane")
my_stock_list.type_keys("^A^C")
stocks_in_text = clipboard.GetData()
buf = StringIO(stocks_in_text)
all_lines = buf.readlines()
headers = all_lines[0].split('\t')
headers = headers[:-1]
headers
contents = all_lines[1].split('\t')
contents = contents[:-1]
contents
row_format = "{:^10}" * len(headers)
print(row_format.format(*headers))
print(row_format.format(*contents))
dir(my_stock_list.wrapper_object())

recipe = first_panel.child_window(title="交 割 单")
recipe.get_value()
dir(recipe.wrapper_object())

# navigate to buy stock panel and fill in the field
side_bar = dlg.child_window(auto_id="129", control_type="Tree")
buy = dlg.child_window(title="买入[F1]")
sell = dlg.child_window(title="卖出[F2]")
buy.print_control_identifiers()
buy_spec = buy.wrapper_object().select()
stock_code = first_panel.child_window(auto_id="1032", control_type="Edit").set_text("600196")
buy_price = first_panel.child_window(auto_id="1033", control_type="Edit").set_text("25.2")
buy_amount = first_panel.child_window(auto_id="1034", control_type="Edit").set_text("100")
dir(buy_price.wrapper_object())
dir(buy_spec)
dir(side_bar.get_item(['买入[F1]']))
