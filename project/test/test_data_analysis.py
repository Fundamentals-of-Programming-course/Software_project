import pytest
import sys

from pathlib import Path
from datetime import datetime, timedelta
sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.data_analysis import (
    count_entries,
    calculate_summary_statistics,
    job_posting_analysis,
    filter_and_count_job_titles,
    check_application_deadlines
)


# Sample mock data for tests

sample_data = [
    {
        "organisaatio": "Org A",
        "tyotehtava": "Teacher",
        "haku_paattyy_pvm": (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")
    },
    {
        "organisaatio": "Org B",
        "tyotehtava": "Assistant",
        "haku_paattyy_pvm": (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    },
    {
        "organisaatio": "Org A",
        "tyotehtava": "Teacher",
        "haku_paattyy_pvm": None
    },
    {
        "organisaatio": "Org C",
        "tyotehtava": "Principal",
        "haku_paattyy_pvm": (datetime.today() + timedelta(days=5)).strftime("%Y-%m-%d")
    }
]

@pytest.fixture
def test_count_entries():
    assert count_entries(sample_data) == 4

def test_calculate_summary_statistics():
    stats = calculate_summary_statistics(sample_data)
    assert stats['most_common_organization'] == "Org A"
    assert stats['most_common_job_title'] == "Teacher"

def test_job_posting_analysis():
    analysis = job_posting_analysis(sample_data)
    assert analysis['total_postings'] == 4
    assert analysis['min'] >= 1
    assert analysis['max'] >= 2
    assert 'Org A' in analysis['organization_counter']
    assert analysis['organization_counter']['Org A'] == 2

def test_filter_and_count_job_titles():
    counts = filter_and_count_job_titles(sample_data, "Org A")
    assert counts == {"Teacher": 2}

def test_check_application_deadlines():
    results = check_application_deadlines(sample_data)
    assert results['expired_count'] == 1
    assert results['open_count'] == 2
    assert len(results['expired_postings']) == 1
    assert len(results['open_postings']) == 2
    
# Run the tests with this on root terminal pytest -v project/test/test_data_analysis.py     