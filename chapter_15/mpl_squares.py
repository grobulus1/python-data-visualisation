import matplotlib.pyplot as plt
import threading


def create_plot():
    threading.Timer(5.0, create_plot).start()
    squares = [square*square for square in range(1, 6)]
    input_values = [value for value in range(1, 6)]
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(input_values, squares, linewidth=3)

    ax.set_title(f"Square Numbers", fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Square of Value", fontsize=14)

    ax.tick_params(labelsize=14)

    plt.show()


create_plot()

