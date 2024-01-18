import os
import webbrowser
from coach.src import swimclub
from display.src import display_generator

swim_files = os.listdir(swimclub.FOLDER)

swimmers = {}
for file in swim_files:
    name = swimclub.get_swimmer_info(file)[0]
    if name not in swimmers:
        swimmers[name] = []
    swimmers[name].append(file)

sorted(swimmers)

for filename in swimmers["Calvin"]:
    chart_path = display_generator.produce_barchart(filename)
    full_chart_path = "file://wsl$/Ubuntu-20.04" + os.path.realpath(chart_path)
    webbrowser.open(full_chart_path)