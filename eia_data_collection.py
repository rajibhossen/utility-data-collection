import requests
from requests.auth import HTTPBasicAuth


class ApiRequest:
    def __init__(self):
        self.base_url = "https://api.eia.gov/v2/"
        self.data_endpoint = "electricity/rto/fuel-type-data/data"
        self.api_key = ""

    def generate_params(self, offset, start_date, end_date):
        params = {
            "frequency": "hourly",
            "data[0]": "value",
            "facets": {},
            "start": start_date,
            "end": end_date,
            "sort[0][column]": "period",
            "sort[0][direction]": "desc",
            "offset": offset,
            "length": 5000,
            "api_key": self.api_key
        }

        return params

    def get_with_pagination(self):
        parameters = self.generate_params(offset=0, start_date="2024-01-01T00", end_date="2024-01-02T00")
        request = requests.get(url=self.base_url + self.data_endpoint, params=parameters)
        print(request.status_code)
        print(request.headers)
        response = request.text
        print(response)


call = ApiRequest()
call.get_with_pagination()
