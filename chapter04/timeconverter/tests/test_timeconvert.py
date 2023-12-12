from src import timeconvert

def test_convert_with_min():
    time = "1:30.96"
    expected_centasecs = 9096
    assert timeconvert.convert_time_to_centaseconds(time) == expected_centasecs

def test_convert_with_wo_min():
    time = "30.96"
    expected_centasecs = 3096
    assert timeconvert.convert_time_to_centaseconds(time) == expected_centasecs

def test_centaseconds_to_string():
    centasecs = 9096
    expected_time = "1:30.96"
    assert timeconvert.convert_centaseconds_to_time(centasecs) == expected_time