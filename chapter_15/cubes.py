import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x_value**3 for x_value in x_values]
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.plasma, s=5)

ax.set_title("Cube numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

ax.tick_params(labelsize=14)

ax.axis([0, 5100, 0, 130_000_000_000])

plt.savefig("cubes_plot", bbox_inches="tight")
