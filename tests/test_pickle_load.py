import pickle
from core.facade_collectors import ManagerData
import core.settings

path = core.settings.PATH_TEST

manager = ManagerData()
manager.set_csv_data_collector(path)

linear_file = open("linear_shared", "rb")
linear = pickle.load(linear_file)

list_hi_ws, list_thw = manager.get_data_csv()

thws_calculated = linear.predict([[18.20, 0.00]])

for thw_c in thws_calculated:
    assert(round(thw_c[0], 2) == 18.15)
