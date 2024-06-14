import matplotlib.pyplot as plt
import threading
import numpy as np


def create_plot():
    threading.Timer(5, create_plot).start()
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()

    # Generating random x and y values
    x = np.arange(0, 10, 1)
    y = np.random.randint(1, 50 + 1, size=10)

    ax.scatter(x, y)

    ax.set_title(f"Random data", fontsize=24)

    plt.show()


create_plot()
