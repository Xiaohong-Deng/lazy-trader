import pandas as pd
from io import StringIO
from pywinauto import application, clipboard
from time import sleep
from utils.data_utils import table_to_df, filter_df_by_col_val


class LazyTrader:
    def __init__(self):
        self._app = application.Application(backend="uia").connect(
            path="C:\全能行证券交易终端\\xiadan.exe")
        self._dlg = self._app['Dialog']['网上股票交易系统5.0']
        self._top_panel = self._dlg.child_window(auto_id="59648", ctrl_index=0)
        self._side_menu = self._dlg.child_window(auto_id="129", control_type="Tree")
        self._table_window = self._top_panel.child_window(title="Custom1", control_type="Pane")
        self._buy = self._dlg.child_window(title="买入[F1]")
        self._sell = self._dlg.child_window(title="卖出[F2]")
        self._buy_button = self._top_panel.child_window(title="买入[B]")
        self._sell_button = self._top_panel.child_window(title="卖出[S]")
        self._deal_panel = self._dlg.child_window(title="当日委托")

    def buy(self, stock_code, price, amount):
        self._buy.select()
        self._top_panel.child_window(auto_id="1032", control_type="Edit").set_text(stock_code)
        self._top_panel.child_window(auto_id="1033", control_type="Edit").set_text(price)
        self._top_panel.child_window(auto_id="1034", control_type="Edit").set_text(amount)
        self._buy_button.click()

    def buy_after_sold(self, buy_tuple, sold_tuple):
        try:
            buy_stock_code, buy_price, buy_amount = buy_tuple
        except ValueError:
            print("buy_tuple has wrong number of values. Aborting")
            return

        try:
            sold_stock_code, sold_price, sold_amount = sold_tuple
        except ValueError:
            print("sold_tuple has wrong number of values. Aborting")
            return

        if sold_amount > 0:
            sold_amount = -sold_amount

        sold = False

        col_vals = {"证券代码": sold_stock_code, "成交均价": sold_price, "成交数量": sold_amount}

        # how to make it nonblocking
        while not sold:
            done_deals = table_to_df(self._deal_panel, self._table_window)
            sold = filter_df_by_col_val(done_deals, col_vals)
            sleep(600)

        self.buy(buy_stock_code, buy_price, buy_amount)

    def sell(self, stock_code, price, amount):
        self._sell.select()
        self._top_panel.child_window(auto_id="1032", control_type="Edit").set_text(stock_code)
        self._top_panel.child_window(auto_id="1033", control_type="Edit").set_text(price)
        self._top_panel.child_window(auto_id="1034", control_type="Edit").set_text(amount)
        self._sell_button.click()

    def sell_after_(self, bought_tuple, sell_tuple):
        pass
