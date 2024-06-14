import matplotlib.pyplot as plt
from die import Die

die_1 = Die()
die_2 = Die()
results = [die_1.roll() + die_2.roll() for value in range(1_000)]
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
frequencies = [results.count(value) for value in poss_results]
plt.style.use('classic')
fig, ax = plt.subplots()
ax.bar(poss_results, frequencies)
ax.set_title("Result of Rolling Two D6s 1,000 Times")
ax.set_xlabel("Roll")
ax.set_ylabel("Frequency")
ax.set_xticks(poss_results)
ax.axis([1, 13, 0, 200])
plt.show()

