from mlproject.distance import haversine

def test_haversine():
    assert haversine(14, 14, 14, 14) == 0.0