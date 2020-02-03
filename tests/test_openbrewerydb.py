import random

import pytest
from jsonschema import validate

from api_client import APIClient

API_BREWERY = APIClient(base_address='https://api.openbrewerydb.org')

CITIES = ['New York', 'Los Angeles', 'Chicago', 'Phoenix', 'San Francisco']
TAGS = ['dog-friendly', 'patio', 'food-service', 'food-truck', 'tours']


def test_list_breweries():
    """
    Проверка, возвращается валидный статус
    """
    response = API_BREWERY.get(path='/breweries')
    assert response.ok


def test_valid_schema():
    """
    Проверка структуры ответа за запрос /breweries/5494
    """
    response = API_BREWERY.get(path='/breweries/5494')
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "name": {"type": "string"},
            "brewery_type": {"type": "string"},
            "street": {"type": "string"},
            "city": {"type": "string"},
            "state": {"type": "string"},
            "postal_code": {"type": "string"},
            "country": {"type": "string"},
            "longitude": {"type": "string"},
            "latitude": {"type": "string"},
            "phone": {"type": "string"},
            "website_url": {"type": "string"},
            "updated_at": {"type": "string"},
            "tag_list": {"type": "array"}

        },
        "required": ["id", "name", "brewery_type", "street",
                     "city", "state", "postal_code", "country",
                     "longitude", "latitude", "phone", "website_url",
                     "updated_at", "tag_list"]
    }

    validate(instance=response.json(), schema=schema)


@pytest.mark.parametrize('city', CITIES)
def test_filter_by_city(city):
    """
    Проверка, фильр по городу
    """
    city.lower()
    city.replace(' ', '_')
    response = API_BREWERY.get(path='/breweries', params={'by_city': city})
    assert response.ok


@pytest.mark.parametrize('tag', TAGS)
def test_search_brewery(tag):
    """
    Проверка, фильтр по тегам
    """
    tag.replace('-', '_')
    response = API_BREWERY.get(path='/breweries', params={'by_tag': tag})
    assert response.ok


def get_random_number():
    """
    Возвращает список рандомных цифрт
    """
    random_numbers = []
    for i in range(1, 10):
        ran_id = random.randint(10, 500)
        random_numbers.append(ran_id)
    return random_numbers


@pytest.mark.parametrize('id_brewery', get_random_number())
def test_random_brewery(id_brewery):
    """
    Проверка, поиск пивоварни по случайному ид
    """
    response = API_BREWERY.get(path='/breweries/%s' % id_brewery)
    assert response.ok
