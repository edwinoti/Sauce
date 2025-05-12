import pytest
from api.country_api import get_country_data

@pytest.mark.api
def test_status_code_success():
    response = get_country_data()
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

@pytest.mark.api
def test_get_one_country_name():
    response = get_country_data()
    data = response.json()

    assert len(data) > 0, "No countries found using KES currency"

    country_name = data[0].get('name', {}).get('common')
    assert country_name and isinstance(country_name, str), "Country name not found or invalid"
