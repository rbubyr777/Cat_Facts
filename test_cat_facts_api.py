import requests
import pytest

BASE_URL = "https://cat-fact.herokuapp.com"


def test_get_random_fact():
    """Test fetching a random cat fact."""
    response = requests.get(f"{BASE_URL}/facts/random")

    # Assert the response status code is 200 (success)
    assert response.status_code == 200, "Failed to retrieve random fact"

    # Assert the response contains JSON data
    data = response.json()
    assert isinstance(data, dict), "Expected data to be in dictionary format"

    # Check that the returned data has the expected fields
    assert "text" in data, "Missing 'text' in fact data"
    assert "type" in data and data["type"] == "cat", "Fact type is not 'cat'"


@pytest.mark.parametrize("num_facts", range(0, 11))
def test_get_multiple_random_facts(num_facts):
    """Test fetching multiple random cat facts with a specified limit."""
    response = requests.get(f"{BASE_URL}/facts/random?amount={num_facts}")

    # Assert the response status code is 200 (success)
    assert response.status_code == 200, f"Failed to retrieve {num_facts} random facts"

    # Assert the response contains JSON data and matches expected format
    data = response.json()
    if num_facts == 0:
        assert isinstance(data, list), "Expected data to be in list format"
        assert len(data) == num_facts, f"Expected {num_facts} facts, got {len(data)}"
    elif num_facts == 1:
        assert isinstance(data, dict), "Expected data to be in dict format for num_facts = 1"
        assert len(data) == 9, f"Expected number of data dict is 9, got {len(data)}"
    else:
        assert isinstance(data, list), "Expected data to be in list format"
        assert len(data) == num_facts, f"Expected {num_facts} facts, got {len(data)}"

    # Check each fact in the list has the required fields
    if num_facts > 1:
        for fact in data:
            assert "text" in fact, "Missing 'text' in fact data"
            assert "type" in fact and fact["type"] == "cat", "Fact type is not 'cat'"
