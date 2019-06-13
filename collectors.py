import csv
import requests
from requests.exceptions import RequestException


class CsvDataCollector:

    def __init__(self, path):
        self.path = path

    def csv_to_list(self):
        """
        Extrai os dados do csv
        :return: lists of [hi, ws, thw]
        """
        list_of_lists = []
        with open(self.path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for list_ in reader:
                list_of_lists.append(list_)
        return list_of_lists

    @staticmethod
    def convert_list_to_float(list_of_lists):
        list_of_lists_float = []
        for hi, ws, thw in list_of_lists:
            list_of_lists_float.append([float(hi), float(ws), float(thw)])
        return list_of_lists_float

    @staticmethod
    def created_sublist_x(list_of_lists_float):
        list_of_lists_hi_ws = []
        for list_ in list_of_lists_float:
            list_of_lists_hi_ws.append([list_[0], list_[1]])
        return list_of_lists_hi_ws

    @staticmethod
    def created_sublist_y(list_of_lists_float):
        list_of_lists_thw = []
        for list_ in list_of_lists_float:
            list_of_lists_thw.append([list_[2]])
        return list_of_lists_thw


class ApiDataCollector:

    def __init__(self, url):
        self.url = url

    def get_response(self):
        try:
            response = requests.get(self.url)
        except RequestException as e:
            print(e)
        return response

    @staticmethod
    def get_data_json(response):
        json_data = response.json()
        return json_data

    @staticmethod
    def get_list_values(json_data):
        list_thw = []
        for data in json_data:
            list_thw.append([data['HeatIndex'], data['WindChill']])
        return list_thw
