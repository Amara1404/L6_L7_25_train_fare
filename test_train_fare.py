import pytest
from train_fare import base_fare, concession, tatkal_charge

#Example test cases:
def test_sleeper_fare():
    assert base_fare("SL", 500) == 500

def test_adult_no_concession():
    assert concession(30, "M", False) == 0

#--- Code (statement) coverage test cases ---

def test_base_fare_unknown_class():
    with pytest.raises(ValueError):
        base_fare("XY", 100)

def test_base_fare_invalid_distance():
    with pytest.raises(ValueError):
        base_fare("SL", 0)

def test_base_fare_minimum_bump():
    assert base_fare("SL", 10) == 50

def test_concession_tatkal():
    assert concession(30, "M", True) == 0

def test_concession_infant():
    assert concession(3, "M", False) == 100

def test_concession_child():
    assert concession(10, "M", False) == 50

def test_concession_senior_female():
    assert concession(65, "F", False) == 50

def test_concession_senior_male():
    assert concession(65, "M", False) == 40

def test_tatkal_charge_non_sl_clamped_high():
    assert tatkal_charge("2A", 2000) == 400

def test_tatkal_charge_sl_clamped_low():
    assert tatkal_charge("SL", 500) == 100

#--- Branch coverage test cases ---

def test_tatkal_charge_no_clamp():
    assert tatkal_charge("SL", 2000) == 200
