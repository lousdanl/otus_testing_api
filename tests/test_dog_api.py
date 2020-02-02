import pytest
from jsonschema import validate

from api_client import APIClient

API_DOG = APIClient(base_address='https://dog.ceo/api')

PATHS = ['/breeds/list/all', '/breeds/image/random',
         '/breeds/image/random/3', '/breed/hound/images',
         '/breed/hound/images/random', '/breed/hound/list',
         '/breed/hound/afghan/images', '/breed/hound/afghan/images/random']
NUMBERS = [0, 1, 3, 10, 50, 51]


@pytest.mark.parametrize('path', PATHS)
def test_valid_request(path):
    """
    Проверка, возвращается валидный статус
    """
    response = API_DOG.get(path=path)
    assert response.ok


def get_breeds():
    """
    Возвращает список парод
    """
    breeds = API_DOG.get(path='/breeds/list/all').json()
    breeds = breeds['message'].keys()
    return list(breeds)


@pytest.mark.parametrize('breed', get_breeds())
def test_breed(breed):
    """
    Проверка, получение изображение по выбранной породе
    """
    response = API_DOG.get(path='/breed/%s/images' % breed)
    assert response.status_code == 200


def test_valid_answer():
    """
    Проверка, ответ валидный
    """
    response = API_DOG.get(path='/breeds/image/random')
    response = response.json()
    assert response['message'][-3:] == 'jpg'
    assert response['status'] == 'success'


@pytest.mark.parametrize('number', NUMBERS)
def test_random(number):
    """
    Проверка, кол-во изображение в ответе соответсвует числу в запросе.
    Минимум 1, Максимум 50
    """
    response = API_DOG.get(path='/breeds/image/random/%s' % number)
    response = response.json()
    if number == 0:
        number = 1
    if number > 50:
        number = 50
    assert len(response['message']) == number


def test_valid_schema():
    """
    Проверка структуры ответа за запрос /breeds/image/random
    """
    response = API_DOG.get(path='/breeds/image/random')
    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "string"},
            "status": {"type": "string"},
        },
        "required": ["message", "status"]
    }

    validate(instance=response.json(), schema=schema)
