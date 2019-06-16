import unittest

from sklearn.linear_model import LinearRegression
from numpy import arange

from facade_collectors import ManagerData

import settings


# TODO: refatorar

class TestValidateModel(unittest.TestCase):

    def setUp(self):
        path = settings.PATH_TEST
        url = settings.URL
        self.manager = ManagerData()
        self.manager.set_csv_data_collector(path)
        self.manager.set_api_data_collector(url)
        self.linear = LinearRegression()
        self.list_hi_ws, self.list_thw = self.manager.get_data_csv()
        self.amount_learn = len(self.list_hi_ws) // 2
        self.learn()

    def test_thws(self):
        thws_calculated = self.calculate_thws()
        i = self.amount_learn
        for thw in thws_calculated:
            with self.subTest(self):
                thw_calculated = [round(thw[0], 1)]
                thw_expected = self.list_thw[i]
                range_accepted = self.get_range_accepted(thw_expected)
                self.assertIn(thw_calculated, range_accepted)
            i += 1

    def get_range_accepted(self, thw_expected):
        return [round(diference, 1) for diference in
                arange(thw_expected[0] - 0.5, thw_expected[0] + 0.5, 0.01)]

    def learn(self):
        self.linear.fit(self.list_hi_ws[:self.amount_learn],
                        self.list_thw[:self.amount_learn])

    def calculate_thws(self):
        return self.linear.predict(self.list_hi_ws[self.amount_learn:])
