from utils.src import hfpy_utils
from coach.src import swimclub

def produce_barchart(filename: str) -> str:
    (swimmer, age, distance, stroke) = swimclub.get_swimmer_info(filename)

    (times, converts, avg_time_string)= swimclub.read_swim_data(filename)
    max_converted_time = max(converts)
    svg = ""

    times.reverse()
    converts.reverse()

    for n, t in enumerate(times):
        bar_value = hfpy_utils.convert2range(converts[n], 0, max_converted_time, 0, 350)
        svg = svg + f"""
            <svg height="30" width="400">
                <rect height="30" width="{bar_value}" style="fill:rgb(0,0,255);" />
            </svg>{t}<br />
        """

    title = f"{swimmer} (Under {age}) {distance} {stroke}"
    html = f"""<!DOCTYPE html>
    <html>
        <head>
            <title>{title}</title>
        </head>
        <body>
            <h3>{title}</h3>
    {svg}
        <p>Average time: {avg_time_string}</p>
        </body>
    </html>
    """

    save_to = f"charts/{filename.removesuffix('.txt')}.html"

    with open(save_to, "w") as tf:
        print(html, file=tf)

    return save_to  