import pytest
import tempfile
import os
import json
import sys
from pathlib import Path


sys.path.append(str(Path(__file__).resolve().parents[1]))
from src.gym_data_analysis import (
    load_json_file,
    count_entries,
    most_frequent_entries,
    calculate_statistics,
    filter_by_date_and_key,
    get_all_group_ids
)

# Sample test data
sample_data = [
    {
        "utcdate": "2021-08-15T00:00:00.000Z",
        "area": "Hietaniemi",
        "groupId": "OG10",
        "usageMinutes": 120
    },
    {
        "utcdate": "2021-08-20T00:00:00.000Z",
        "area": "Hietaniemi",
        "groupId": "OG10",
        "usageMinutes": 150
    },
    {
        "utcdate": "2021-08-22T00:00:00.000Z",
        "area": "Pirkkola",
        "groupId": "OG23",
        "usageMinutes": 90
    }
]

@pytest.fixture
def test_load_json_file():
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tmp:
        json.dump(sample_data, tmp)
        tmp.seek(0)
        filename = tmp.name
    
    data = load_json_file(filename)
    assert isinstance(data, list)
    assert data[0]["groupId"] == "OG10"

    os.remove(filename)

def test_count_entries():
    assert count_entries(sample_data) == 3

def test_most_frequent_entries():
    result = most_frequent_entries(sample_data, "groupId")
    assert result[0] == ("OG10", 2)
    assert result[1] == ("OG23", 1)

def test_calculate_statistics():
    stats = calculate_statistics(sample_data, "usageMinutes")
    assert stats["Average"] == 120.0
    assert stats["Maximum"] == 150
    assert stats["Minimum"] == 90
    assert stats["Median"] == 120.0
    assert "Standard deviation" in stats

def test_filter_by_date_and_key():
    filtered = filter_by_date_and_key(
        sample_data,
        "utcdate", "2021-08-01T00:00:00.000Z", "2021-08-31T23:59:59.999Z",
        "groupId", "OG10",
        "area", "Hietaniemi"
    )
    assert len(filtered) == 2
    for entry in filtered:
        assert entry["groupId"] == "OG10"
        assert entry["area"] == "Hietaniemi"

def test_get_all_group_ids():
    group_ids = get_all_group_ids(sample_data)
    assert group_ids == ["OG10", "OG23"]

# pytest -v extra_project/test/test_gym_data_analysis.py  