from molecule import api


def test_driver_is_detected():
    drivers = [str(d) for d in api.drivers()]
    assert "gce" in drivers
