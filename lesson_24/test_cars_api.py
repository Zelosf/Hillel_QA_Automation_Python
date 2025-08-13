import pytest
import logging
import requests
from requests.auth import HTTPBasicAuth


logger = logging.getLogger("car_search_test")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("test_search.log", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(logging.StreamHandler())

BASE_URL = "http://127.0.0.1:8080"


@pytest.fixture(scope="class")
def authenticated_session():
    session = requests.Session()
    auth_url = f"{BASE_URL}/auth"
    auth = HTTPBasicAuth('test_user', 'test_pass')
    response = session.post(auth_url, auth=auth)

    assert response.status_code == 200, "Помилка Аутентифікації"
    token = response.json()["access_token"]
    session.headers.update({'Authorization': f'Bearer {token}'})
    return session


@pytest.mark.usefixtures("authenticated_session")
class TestCarSearch:

    @pytest.mark.parametrize("sort_by,limit", [
        ("price", 5),
        ("year", 10),
        ("engine_volume", 7),
        ("brand", 3),
        ("price", 15),
        ("year", 2),
        ("engine_volume", 20)
    ])
    def test_car_search(self, authenticated_session, sort_by, limit):
        logger.info(f"Тест запиту: sort_by={sort_by}, limit={limit}")
        url = f"{BASE_URL}/cars"
        params = {"sort_by": sort_by, "limit": limit}
        response = authenticated_session.get(url, params=params)

        assert response.status_code == 200, f"Очікувався статус 200, отримано {response.status_code}"
        cars = response.json()
        assert isinstance(cars, list), "Відповідь не є списком"
        assert len(cars) <= limit, f"Отримано більше записів, ніж limit={limit}"

        if cars:
            keys = {"brand", "year", "engine_volume", "price"}
            for car in cars:
                assert keys.issubset(car.keys()), f"Відсутні поля у записі: {car}"

        logger.info(f"Отримано {len(cars)} машин(и): {[car['brand'] for car in cars]}")


@pytest.mark.usefixtures("authenticated_session")
class TestCarByEngineVolume:

    @pytest.mark.parametrize("expected_engine_volume, expected_count", [
        (2.0, 6),
        (1.6, 2),
        (3.0, 21)
    ])
    def test_cars_by_engine_volume(self, authenticated_session, expected_engine_volume, expected_count):
        logger.info(f"Тест вибірки по engine_volume={expected_engine_volume}, очікується {expected_count} шт.")
        url = f"{BASE_URL}/cars"
        response = authenticated_session.get(url)

        assert response.status_code == 200, f"Очікувався статус 200, отримано {response.status_code}"
        cars = response.json()
        assert isinstance(cars, list), "Відповідь не є списком"

        filtered_cars = [car for car in cars if car["engine_volume"] == expected_engine_volume]
        assert len(filtered_cars) == expected_count, (
            f"Очікувалось {expected_count} машин, отримано {len(filtered_cars)}"
        )

        for car in filtered_cars:
            assert car["engine_volume"] == expected_engine_volume, \
                f"Очікувався engine_volume={expected_engine_volume}, отримано {car['engine_volume']}"

        logger.info(f"Знайдено {len(filtered_cars)} машин: {[car['brand'] for car in filtered_cars]}")

