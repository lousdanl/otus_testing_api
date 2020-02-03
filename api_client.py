import requests


class APIClient:
    """
    Упрощенный клиент для работы с API
    Инициализируется базовым url на который пойдут запросы
    """

    def __init__(self, base_address):
        self.base_address = base_address

    def get(self, path="/", params=None):
        url = self.base_address + path
        return requests.get(url=url, params=params)

    def post(self, path="/", params=None, data=None, headers=None):
        url = self.base_address + path
        return requests.post(url=url, params=params, data=data, headers=headers)

    def put(self, path="/", params=None, data=None, headers=None):
        url = self.base_address + path
        return requests.put(url=url, params=params, data=data, headers=headers)

    def delete(self, path="/", data=None, headers=None):
        url = self.base_address + path
        return requests.delete(url=url, data=data, headers=headers)
