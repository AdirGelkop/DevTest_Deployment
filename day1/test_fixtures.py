import pytest

@pytest.fixture
def sample_candidate():
    return {
        "name": "alice",
        "role": "developer",
        "exp": 3,
    }
def test_name_aint_empty(sample_candidate):
    assert sample_candidate["name"] != ""
def test_name_is_longer_than_0(sample_candidate):
    assert len(sample_candidate["name"]) > 0
def test_candidate_exp(sample_candidate):
    assert sample_candidate["exp"] >= 0

