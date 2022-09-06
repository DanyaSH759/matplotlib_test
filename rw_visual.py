import matplotlib
import matplotlib.pyplot as plt

from random_walk import RandomWalk

def print_randow_walk():
	matplotlib.use('Qt5Agg')
	#Построение случайного блуждания
	rw = RandomWalk(10000)
	rw.fill_walk()

	''' 
	#Нанесение точек на диаграмму (без изменения цвета точек)
	plt.style.use('classic')
	fig, ax = plt.subplots()
	ax.scatter(rw.x_values, rw.y_values, s=5)
	'''

	# Нанесение точек на диаграмму c постепенным уменьшением интенсивности цвета точек
	plt.style.use('classic')
	fig, ax = plt.subplots(figsize=(15, 9), dpi=64)  # назначение размера области просмотра
	point_numbers = range(rw.num)
	ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
			   edgecolors='none', s=1)

	# Выделение первой и последней точки
	ax.scatter(0, 0, c='green', edgecolors='none', s=100)
	ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)


	# Удаление осей
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)

	plt.show()



