import pytest
from working import convert

def test_valid():
    assert convert("9:30 AM to 5:45 PM") == "09:30 to 17:45"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("1 AM to 1 PM") == "01:00 to 13:00"
    assert convert("11 AM to 11 PM") == "11:00 to 23:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("7:05 AM to 6:55 PM") == "07:05 to 18:55"

def test_invalid():
    with pytest.raises(ValueError):
        convert("9:75 AM to 5:45 PM")
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("12:60 PM to 1:00 AM")
    with pytest.raises(ValueError):
        convert("00:30 AM to 4:45 PM")
    with pytest.raises(ValueError):
        convert("25:00 AM to 3:00 PM")
    with pytest.raises(ValueError):
        convert("11:61 AM to 2:00 PM")

def test_other_type_errors():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM") 
    with pytest.raises(ValueError):
        convert("9:00AMto5:00PM")
    with pytest.raises(ValueError):
        convert("09:00 am to 05:00 pm")
    with pytest.raises(ValueError):
        convert("9:00AMto5PM")
