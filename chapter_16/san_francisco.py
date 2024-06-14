from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/san_francisco')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
head = next(reader)
dates, highs, lows = [], [], []
for line in reader:
    if line[1] != "VALLEJO, CA US":
        break
    date = datetime.strptime(line[2], "%Y-%m-%d")
    try:
        high = (int(line[9]) - 32) * 5/9
        low = (int(line[10]) - 32) * 5/9
    except ValueError:
        print(f"Can't find data for {date}.")
    else:
        dates.append(date)
        highs.append(high)
        lows.append(low)

plt.style.use("bmh")

fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, color='blue', alpha=0.1)


title = "Daily high and low temperatures\n San Francisco"
ax.set_title(title, fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylim(0)
ax.set_xlim(dates[0], dates[-1])
ax.set_ylabel('Temperature (C)', fontsize=16)
ax.tick_params(labelsize=14)
plt.show()

