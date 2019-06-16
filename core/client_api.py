from core.facade_collectors import ManagerData
from sklearn.linear_model import LinearRegression
import core.settings

url = core.settings.URL
path = core.settings.PATH

manager = ManagerData()
manager.set_api_data_collector(url)
manager.set_csv_data_collector(path)

linear = LinearRegression()

list_hi_ws_csv, list_thw_csv = manager.get_data_csv()
list_hi_ws_api = manager.get_data_api()

linear.fit(list_hi_ws_csv, list_thw_csv)
thws_calculated = linear.predict(list_hi_ws_api)

for thw in thws_calculated:
    print(round(thw[0], 1))
