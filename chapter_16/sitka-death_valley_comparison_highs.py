from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt


path_1 = Path('weather_data/death_valley_2021_simple.csv')
path_2 = Path('weather_data/sitka_weather_2021_simple.csv')
lines_1 = path_1.read_text().splitlines()
lines_2 = path_2.read_text().splitlines()

reader_1 = csv.reader(lines_1)
reader_2 = csv.reader(lines_2)
next(reader_1)
next(reader_2)

dates_1, highs_1 = [], []
dates_2, highs_2 = [], []
for row in reader_1:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates_1.append(current_date)
        highs_1.append(high)

for row in reader_2:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[4])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates_2.append(current_date)
        highs_2.append(high)

plt.style.use('bmh')
fig, ax = plt.subplots()
ax.plot(dates_1, highs_1, color='red', alpha=0.5)
ax.plot(dates_2, highs_2, color='blue', alpha=0.5)
ax.fill_between(dates_1, highs_1, highs_2, facecolor='blue', alpha=0.1)

ax.set_title("Difference in daily high temperatures between Death Valley, CA (red)\nand Sitka, AK (blue).", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
