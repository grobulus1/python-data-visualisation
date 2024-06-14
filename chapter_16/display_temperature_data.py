from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt


def generate_temperature_differences_plot(pth):
    path = Path(pth)
    lines = path.read_text().splitlines()
    reader = csv.reader(lines)
    head = next(reader)

    date_index = head.index('DATE')
    high_index = head.index('TMAX')
    low_index = head.index('TMIN')
    name_index = head.index('NAME')
    dates, highs, lows = [], [], []
    name = ""

    for line in reader:
        date = datetime.strptime(line[date_index], '%Y-%m-%d')
        try:
            high = (int(line[high_index]) - 32) * 5/9
            low = (int(line[low_index]) - 32) * 5/9
            name = line[name_index]
        except ValueError:
            print(f"Can't find data for {date}")
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

    plt.style.use("bmh")

    fig, ax = plt.subplots()
    ax.plot(dates, highs, color='red', alpha=0.5)
    ax.plot(dates, lows, color='blue', alpha=0.5)
    ax.fill_between(dates, highs, lows, color='blue', alpha=0.1)

    title = f"Daily high and low temperatures\n {name}."
    ax.set_title(title, fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_xlim(dates[0], dates[-1])
    ax.set_ylabel('Temperature (C)', fontsize=16)
    ax.tick_params(labelsize=14)
    plt.show()
