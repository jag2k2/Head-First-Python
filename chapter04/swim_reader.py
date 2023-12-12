from coach.src import swimclub

filename = "Darius-13-100m-Fly.txt"

swimmer, age, distance, stroke = swimclub.get_swimmer_info(filename)
converts, avg_time = swimclub.read_swim_data(filename)

print(swimmer)
print(age)
print(distance)
print(stroke)

print(converts)
print(avg_time)