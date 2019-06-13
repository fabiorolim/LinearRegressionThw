import unittest
from facade_collectors import ManagerData
import settings


class TestGetData(unittest.TestCase):

    def setUp(self):
        url = settings.URL
        path = settings.PATH
        self.manager = ManagerData()
        self.manager.set_csv_data_collector(path)
        self.manager.set_api_data_collector(url)

    def test_data_list_x_csv(self):
        list_x = self.manager.get_data_csv()[0][0]
        self.assertEqual([22.8, 2.41], list_x)

    def test_data_list_y_csv(self):
        list_y = self.manager.get_data_csv()[1][0]
        self.assertEqual([22.8], list_y)

    def test_data_api(self):
        list_ = self.manager.get_data_api()[0]
        self.assertEqual(list_, [23.3, 22.2])
