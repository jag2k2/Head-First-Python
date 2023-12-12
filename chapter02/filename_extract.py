file_name = "Darius-13-100m-Fly.txt"

if __name__ == "__main__":
    swimmer, age, distance, stroke = file_name.removesuffix(".txt").split("-")
    print(swimmer)
    print(age)
    print(distance)
    print(stroke)