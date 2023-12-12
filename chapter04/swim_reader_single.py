from coach.src import swimclub

filename = "Darius-13-100m-Fly.txt"

swimmer_info = swimclub.get_swimmer_info(filename)
swim_data = swimclub.read_swim_data(filename)

print(swimmer_info[0])
print(swimmer_info[1])
print(swimmer_info[2])
print(swimmer_info[3])

print(swim_data[0])
print(swim_data[1])