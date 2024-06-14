import csv
import matplotlib.pyplot as plt
from datetime import datetime
from pathlib import Path

path = Path("weather_data/sitka_weather_2021_full.csv")
lines = path.read_text().splitlines()
reader = csv.reader(lines)
head = next(reader)
dates, amounts = [], []
for line in reader:
    date = datetime.strptime(line[2], '%Y-%m-%d')
    try:
        amount = float(line[5])
    except ValueError:
        print(f"Data for {date} not found.")
    else:
        dates.append(date)
        amounts.append(amount)
plt.style.use('bmh')
fig, ax = plt.subplots()
ax.plot(dates, amounts, color='blue', alpha=0.5)
fig.autofmt_xdate()
ax.set_title("Daily Rainfall Amounts, 2024 \n Sitka AK")
ax.set_xlabel('', fontsize=12)
ax.set_ylabel("Rainfall Amounts (inches)", fontsize=16)
ax.tick_params(labelsize=12)
ax.set_ylim(bottom=0)

plt.show()
