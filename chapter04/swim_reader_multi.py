import os
from coach.src import swimclub

swim_files = os.listdir(swimclub.FOLDER)

for i, swim_file in enumerate(swim_files, 1):
    swimmer_info = swimclub.get_swimmer_info(swim_file)
    swim_data = swimclub.read_swim_data(swim_file)
    
    print(i, ": " + swim_file)
    print("Name: " + swimmer_info[0] + ", Age: " + swimmer_info[1] + ", Distance: " + swimmer_info[2] + ", Stroke: " + swimmer_info[3])
    print(swim_data[0])
    print(swim_data[1])