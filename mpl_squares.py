import matplotlib
import matplotlib.pyplot as plt


def square():
    matplotlib.use('Qt5Agg')
    input_values = [1,2,3,4,5]
    squares = [1, 4, 9, 16, 25]

    plt.style.use('fivethirtyeight')
    fig, ax = plt.subplots()#функция генерирует диаграммы
    ax.plot(input_values, squares, linewidth = 3)

    # Назначение заголовка диаграммы
    ax.set_title("Square Numbers", fontsize=24)
    ax.set_xlabel("Value", fontsize = 14)
    ax.set_ylabel("square of valye", fontsize = 14)

    # Назначение размера шрифта делений на осях
    ax.tick_params(axis='both', labelsize = 14)


    #plt.savefig('test_save.jpeg') если необходимо сохранить файл отдельно
    plt.show()