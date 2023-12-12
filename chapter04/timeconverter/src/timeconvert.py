def convert_time_to_centaseconds(time: str) -> int:
    if ":" in time:
        minutes, rest = time.split(":")
        seconds, hundredths = rest.split(".")
    else:
        minutes = 0
        seconds, hundredths = time.split(".")
    centaseconds = int(minutes)*6000 + int(seconds)*100 + int(hundredths)
    return centaseconds

def convert_centaseconds_to_time(centasecs: int) -> str:
    mins_secs, hundredths = str(round(centasecs / 100, 2)).split(".")
    mins_secs = int(mins_secs)
    minutes = mins_secs // 60
    seconds = mins_secs - minutes*60
    return str(minutes) + ":" + str(seconds) + "." + hundredths