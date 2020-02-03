import random

import pytest

from api_client import APIClient

API_JPH = APIClient(base_address='https://jsonplaceholder.typicode.com')


@pytest.mark.parametrize('post_id', [random.randint(1, 10) for i in range(1, 6)])
def test_get_posts1(post_id):
    """
    Проверка, запрос возвращается заданное id поста
    """
    response = API_JPH.get(path='/posts/%s' % post_id)
    response = response.json()
    assert response['id'] == post_id
    assert response['userId'] == 1


@pytest.mark.parametrize('post_id, user_id', [(20, 2), (30, 3), (60, 6)])
def test_get_posts2(post_id, user_id):
    """
    Проверка, id пользователя соответсвует количеству десятков в id поста
    """
    response = API_JPH.get(path='/posts/%s' % post_id)
    response = response.json()
    assert response['id'] == post_id
    assert response['userId'] == user_id


def test_post_users():
    """
    Отправка post запроса
    """
    response = API_JPH.post(path='/users/1/todos',
                            data={'userId': 5,
                                  'title': 'delectus aut autem',
                                  'completed': 'false'
                                  }).json()
    assert response['userId'] == '5'
    assert response['title'] == 'delectus aut autem'
    assert response['completed'] == 'false'


def test_put_posts():
    """
    Отправка put запроса
    """
    response = API_JPH.put(path='/posts/20',
                           data={'userId': 2,
                                 'id': 20,
                                 'title': 'doloribus',
                                 'body': 'consequuntur',
                                 }).json()
    assert response['userId'] == '2'
    assert response['id'] == 20
    assert response['title'] == 'doloribus'
    assert response['body'] == 'consequuntur'


def test_delete_posts():
    """
    Отправка delete запроса
    """
    response = API_JPH.delete(path='/posts/10/')
    assert response.ok
