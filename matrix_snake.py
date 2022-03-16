"""
  A program that fills a matrix in the form of a snake.
  Author @keh9mark.
"""

n = int(input("Please enter a number greater than 0: "))


def first_methods(n: int, display: bool = False) -> None:
  """The first script for filling in matrices, contains 5 cycles"""
  print(f"\nStart 'first_methods' for matrix size: {n}")
  matrix: dict = {}

  count_of_items: int = n * n
  min_i, max_i = 0, n
  min_j, max_j = 0, n
  count = 0
  current_j, current_i = 0, 0

  while count < count_of_items:
    for index in range(min_i, max_i):
      matrix[index, current_j] = count
      count += 1
    current_i = index
    min_j += 1
    for index in range(min_j, max_j):
      matrix[current_i, index] = count
      count += 1
    current_j = index
    max_i -= 1
    for index in range(max_i - 1, min_i - 1, -1):
      matrix[index, current_j] = count
      count += 1
    current_i = index
    max_j -= 1
    for index in range(max_j - 1, min_j - 1, -1):
      matrix[current_i, index] = count
      count += 1
    current_j = index
    min_i += 1
  if display:
    print(matrix)


def second_methods(n: int, display: bool = False) -> None:
  """The first script for filling in matrices, contains 3 cycles"""
  print(f"\nStart 'second_methods' for matrix size: {n}")
  matrix: dict = {}
  count_of_items: int = n * n

  min_i, max_i = 0, n
  min_j, max_j = 0, n
  count = 0

  while count < count_of_items:
    count_insert_right = (max_i - min_i) + (max_j - min_j) - 1
    indexes = [min_i, min_j]
    set_row = 0
    for _ in range(0, count_insert_right):
      count += 1
      matrix[indexes[0], indexes[1]] = count - 1
      if indexes[set_row] >= max_i - 1:
        set_row = 1
      if indexes[set_row] == max_j - 1:
        continue
      indexes[set_row] += 1

    count_insert_left = count_insert_right - 2
    set_row = 0
    for _ in range(0, count_insert_left):
      if indexes[set_row] <= min_i:
        set_row = 1
      indexes[set_row] -= 1
      count += 1
      matrix[indexes[0], indexes[1]] = count - 1
    min_i += 1
    max_i -= 1
    min_j += 1
    max_j -= 1
  if display:
    print(matrix)


first_methods(n, display=True)
second_methods(n, display=True)
