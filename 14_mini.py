import numpy as np
import matplotlib.pyplot as plt
import time
SIZE = 128
ITERATIONS = 128

def generate_field(size):
    return np.random.randint(0, 2, (size, size))

def game_of_life_python(field, iterations):
    rows, cols = len(field), len(field[0])
    for _ in range(iterations):
        new_field = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                live_neighbors = sum(
                    field[i + di][j + dj]
                    for di in (-1, 0, 1)
                    for dj in (-1, 0, 1)
                    if (di != 0 or dj != 0) and 0 <= i + di < rows and 0 <= j + dj < cols
                )
                if field[i][j] == 1 and live_neighbors in (2, 3):
                    new_field[i][j] = 1
                elif field[i][j] == 0 and live_neighbors == 3:
                    new_field[i][j] = 1
        field = new_field
    return field

def game_of_life_numpy(field, iterations):
    rows, cols = field.shape
    for _ in range(iterations):
        neighbors = np.zeros_like(field)
        neighbors[1:, 1:] += field[:-1, :-1]  # Верхний левый
        neighbors[1:, :-1] += field[:-1, 1:]  # Верхний правый
        neighbors[:-1, 1:] += field[1:, :-1]  # Нижний левый
        neighbors[:-1, :-1] += field[1:, 1:]  # Нижний правый
        neighbors[1:, :] += field[:-1, :]    # Верхний
        neighbors[:-1, :] += field[1:, :]    # Нижний
        neighbors[:, 1:] += field[:, :-1]    # Левый
        neighbors[:, :-1] += field[:, 1:]    # Правый
        field = (neighbors == 3) | ((field == 1) & (neighbors == 2))
        field = field.astype(int)
    return field

def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, end_time - start_time

initial_field = generate_field(SIZE)
python_field = initial_field.tolist()
numpy_field = np.copy(initial_field)

python_result, python_time = measure_time(game_of_life_python, python_field, ITERATIONS)
numpy_result, numpy_time = measure_time(game_of_life_numpy, numpy_field, ITERATIONS)

assert np.array_equal(np.array(python_result), numpy_result), "Результаты не совпадают!"

print(f"Python версия: {python_time:.2f} секунд")
print(f"NumPy версия: {numpy_time:.2f} секунд")

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title("Python версия")
plt.imshow(python_result, cmap='binary')
plt.subplot(1, 2, 2)
plt.title("NumPy версия")
plt.imshow(numpy_result, cmap='binary')
plt.show()