from pywinauto import application

app = application.Application(backend="uia").connect(path="C:\全能行证券交易终端\\xiadan.exe")
dlg = app['Dialog']['网上股票交易系统5.0']
dialogs = app.windows()
dlg['control']
dlg.print_control_identifiers()
first_panel = dlg.child_window(auto_id="59648", ctrl_index=0).print_control_identifiers()
