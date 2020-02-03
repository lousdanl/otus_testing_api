import pytest

from api_client import APIClient


@pytest.fixture(scope='session')
def api_client(request):
    base_url = request.config.getoption('--url')
    return APIClient(base_address=base_url)


def pytest_addoption(parser):
    parser.addoption('--url', action='store', default='https://ya.ru')
    parser.addoption('--status_code', action='store', default=200)
