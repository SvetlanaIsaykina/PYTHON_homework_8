import random 
from statistics import mean

# Задача 1. В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки заносятся в таблицу. Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.
def task_1():
  group = 5

  chart = [0] * group

  for index in range(len(chart)):
    chart[index] = [random.randint(2, 5) for _ in range(random.randint(20, 30))]
  
  for el in chart:
    print(el)     
  print()

  mean_list = []
  for i in range(group):
    row_mean = mean(chart[i])
    mean_list.append(round(row_mean, 2))
  print(f'Средние баллы групп - {mean_list}')
  max_mean = max(mean_list)
  print(f'Максимальный балл среди групп - {round(max_mean, 2)}')
  max_i = mean_list.index(max_mean)
  print(f'Группа с наилучшим средним баллом - {max_i+1}') 

task_1()

# Задача 2. Дана квадратная матрица, заполненная случайными числами. Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.

def task_2():
  rows = 5
  numbers = [0] * rows

  for index in range(rows):
    numbers[index] = [random.randint(1, 20) for _ in range(rows)]
  
  for row in numbers:
    print(row)     
  print() 

  diag_sum = 0
  for i in range(rows):
    for j in range(rows):
      if i == j:
        diag_sum += numbers[i][j]

  sum_list = []
  for i in range(rows):
    el_sum = sum(numbers[i])
    sum_list.append(el_sum)

  for el in sum_list:
    if el > diag_sum:
      bigger_row = sum_list.index(el)
      print(f'Сумма элементов строки {bigger_row + 1} превосходит сумму главной диагонали матрицы {diag_sum}')

task_2()


