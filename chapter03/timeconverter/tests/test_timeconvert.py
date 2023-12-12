from src import timeconvert

def test_string_to_centaseconds():
    time = "1:30.96"
    expected_centasecs = 9096
    assert timeconvert.convert_time_to_centaseconds(time) == expected_centasecs

def test_centaseconds_to_string():
    centasecs = 9096
    expected_time = "1:30.96"
    assert timeconvert.convert_centaseconds_to_time(centasecs) == expected_time