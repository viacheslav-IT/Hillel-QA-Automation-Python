import logging
import requests

BASE_URL = "http://127.0.0.1:8080"

# Logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler = logging.FileHandler("test_search.log")
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


def test_search_cars():
    session = requests.Session()

    # Authentication
    response = session.post(
        f"{BASE_URL}/auth",
        auth=("test_user", "test_pass")
    )

    logger.info(f"POST /auth -> {response.status_code}")
    assert response.status_code == 200
    access_token = response.json()["access_token"]
    session.headers.update({
        "Authorization": f"Bearer {access_token}"
    })

    # Search
    params = {
        "sort_by": "price",
        "limit": 5
    }

    response = session.get(
        f"{BASE_URL}/cars",
        params=params
    )
    logger.info(f"GET /cars -> {response.status_code}")
    assert response.status_code == 200
    cars = response.json()
    logger.info(f"Returned cars: {cars}")

    # Validation
    assert len(cars) == 5
    prices = [car["price"] for car in cars]
    assert prices == sorted(prices)
    logger.info("Test passed successfully.")