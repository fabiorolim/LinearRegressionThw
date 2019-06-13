from collectors import CsvDataCollector, ApiDataCollector


class ManagerData:

    def set_csv_data_collector(self, path):
        self.csv_collector = CsvDataCollector(path)

    def set_api_data_collector(self, url):
        self.api_collector = ApiDataCollector(url)

    def get_data_csv(self):
        lists = self.csv_collector.csv_to_list()
        floats_list = CsvDataCollector.convert_list_to_float(lists)
        list_heat_wind = CsvDataCollector.created_sublist_x(floats_list)
        list_thw = CsvDataCollector.created_sublist_y(floats_list)
        return list_heat_wind, list_thw

    def get_data_api(self):
        response = self.api_collector.get_response()
        json = ApiDataCollector.get_data_json(response)
        values = ApiDataCollector.get_list_values(json)
        return values
