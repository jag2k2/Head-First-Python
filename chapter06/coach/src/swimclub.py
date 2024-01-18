from pathlib import Path
from statistics import mean
from coach.src import timeconvert

FOLDER = Path("../swimdata/")

def get_swimmer_info(filename: str) -> (str, int, int, str):
    swimmer, age, distance, stroke = filename.removesuffix(".txt").split("-")
    return swimmer, age, distance, stroke

def read_swim_data(filename: str) -> (list, str):
    with open (FOLDER / filename) as file:
        lines = file.readlines()
        contents = lines[0].strip()
        times = contents.split(",")
        converts = []
        for time in times:
            converts.append(timeconvert.convert_time_to_centaseconds(time))
        avg_time = mean(converts)
        avg_time_string = timeconvert.convert_centaseconds_to_time(avg_time)
        return times, converts, avg_time_string