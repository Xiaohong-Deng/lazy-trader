from pywinauto import application, clipboard
from io import StringIO
import pandas as pd

app = application.Application(backend="uia").connect(path="C:\全能行证券交易终端\\xiadan.exe")
dlg = app['Dialog']['网上股票交易系统5.0']
# dialogs = app.windows()
# dlg.print_control_identifiers()
first_panel = dlg.child_window(auto_id="59648", ctrl_index=0)
# first_panel.print_control_identifiers()

order_history = dlg.child_window(title="历史委托")
order_history.select()
order_history.print_control_identifiers()
order_history_list = first_panel.child_window(title="Custom1", control_type="Pane")
order_history_list.type_keys("^A^C")
order_history_text = clipboard.GetData()
order_history_text
buf = StringIO(order_history_text)
buf.seek(0)
df = pd.read_csv(buf, header=0, delim_whitespace=True, index_col=False, dtype=str, error_bad_lines=False)
df
is_002007 = df['证券代码'] == "002007"
is_002007
start = pd.Series([True] * 145, name='证券')
start

start = start & is_002007
df.shape[0]
matches = df[(df['证券代码'] == "002007") & (df['备注'] == "已成")]
matches
# get text
my_stock_list = first_panel.child_window(title="Custom1", control_type="Pane")
my_stock_list.type_keys("^A^C")
stocks_in_text = clipboard.GetData()
stocks_in_text
buf = StringIO(stocks_in_text)
# pointer goes back to start
buf.seek(0)
# as pointer being back at start, read_csv will work, dtype=str keeps the leading zeros
df = pd.read_csv(buf, header=0, delim_whitespace=True, index_col=False, dtype=str)
df
all_lines = buf.readlines()
all_lines
headers = all_lines[0].split('\t')
headers = headers[:-1]
headers
contents = all_lines[1].split('\t')
contents = contents[:-1]
contents
df = pd.DataFrame.from_records([contents], columns=headers)
df
# contents
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
# first_panel.print_control_identifiers()

sell.select()
first_panel.child_window(auto_id="1032", control_type="Edit").set_text("002007")
first_panel.child_window(auto_id="1033", control_type="Edit").set_text("55.2")
first_panel.child_window(auto_id="1034", control_type="Edit").set_text("100")
first_panel.child_window(title="卖出[S]").click()
buy.print_control_identifiers()
buy_spec = buy.wrapper_object().select()
stock_code = first_panel.child_window(auto_id="1032", control_type="Edit").set_text("600196")
buy_price = first_panel.child_window(auto_id="1033", control_type="Edit").set_text("25.2")
buy_amount = first_panel.child_window(auto_id="1034", control_type="Edit").set_text("100")
dir(buy_price.wrapper_object())
dir(buy_spec)
dir(side_bar.get_item(['买入[F1]']))
