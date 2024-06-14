import matplotlib.pyplot as plt
import csv
from pathlib import Path
from datetime import datetime

path = Path('weather_data/poland_2024.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header = next(reader)

dates, depths = [], []
for line in reader:

    current_date = datetime.strptime(line[2], '%Y-%m-%d')
    try:
        depth = float(line[4])
    except ValueError:
        print(f"No data for {current_date} found.")
    else:
        dates.append(current_date)
        depths.append(depth)
plt.style.use('bmh')
fig, ax = plt.subplots()
ax.plot(dates, depths, color='red', alpha=0.5)
ax.set_title("Daily Snow Depths, 2024, First Half\nBalice, PL", fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Snow depth (inches)", fontsize=16)
ax.tick_params(labelsize=14)

plt.show()
