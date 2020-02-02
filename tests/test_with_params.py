def test_ya_status(api_client, request):
    """
    Задаем статус ответа напрямую
    """
    status_code = request.config.getoption('--status_code')
    response = api_client.get()
    response.status_code = status_code
