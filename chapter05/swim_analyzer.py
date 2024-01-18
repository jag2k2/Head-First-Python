import os
import webbrowser

from display.src import display_generator

# filename = "Darius-13-100m-Fly.txt"
# filename = "Dave-17-100m-Free.txt"
filename = "Lizzie-14-100m-Back.txt"
chart_path = display_generator.produce_barchart(filename)

full_chart_path = "file://wsl$/Ubuntu-20.04" + os.path.realpath(chart_path)
webbrowser.open(full_chart_path)