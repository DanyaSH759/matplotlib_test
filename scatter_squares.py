import matplotlib
import matplotlib.pyplot as plt

def scatter_squares():
    matplotlib.use('Qt5Agg')
    x_value = list(range(1, 1001))
    y_value = [x**2 for x in x_value]

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, s=10)
    #ax.scatter(x_value, y_value, color=(0, 0.8, 0) s=10)


    # Назначение заголовка диаграммы и меток осей
    ax.set_title("Square Numbers", fontsize=20)
    ax.set_xlabel("Value", fontsize = 14)
    ax.set_ylabel("square of valye", fontsize = 14)

    # Назначение размера шрифта делений на осях
    ax.tick_params(axis='both', which = 'major', labelsize = 10)

    #назначение диапазона для кажлой оси
    ax.axis([0,1100,0,1100000])

    plt.show()
    #для автоматического сохранения plt.savefig('swuares_plot.png', bbox_inches ='tight')
