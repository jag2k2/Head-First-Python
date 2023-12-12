from pathlib import Path
from statistics import mean
from timeconverter.src import timeconvert

FN = "Darius-13-100m-Fly.txt"
FOLDER = Path("./swimdata/")

with open (FOLDER / FN) as file:
    lines = file.readlines()
    contents = lines[0].strip()
    times = contents.split(",")
    converts = []
    for time in times:
        converts.append(timeconvert.convert_time_to_centaseconds(time))
    print(converts)
    avg_time = mean(converts)
    print(timeconvert.convert_centaseconds_to_time(avg_time))