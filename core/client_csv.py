from core.facade_collectors import ManagerData
from sklearn.linear_model import LinearRegression
import core.settings

path = core.settings.PATH

manager = ManagerData()
manager.set_csv_data_collector(path)

linear = LinearRegression()

list_hi_ws, list_thw = manager.get_data_csv()

amount_learn = len(list_hi_ws) // 2
linear.fit(list_hi_ws[:amount_learn], list_thw[:amount_learn])
thws_calculated = linear.predict(list_hi_ws[amount_learn:])

for thw in thws_calculated:
    print(round(thw[0], 1))
