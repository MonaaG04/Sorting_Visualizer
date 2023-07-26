 
import tkinter as tk
import random
import time

# Function to generate random data
def generate_data():
    return [random.randint(5, 150) for _ in range(50)]

# Function to draw the bars on the canvas
def draw_data(data, colors):
    canvas.delete("all")
    canvas_width = 600
    canvas_height = 400
    bar_width = canvas_width / len(data)
    offset = 10

    for i, height in enumerate(data):
        x0 = i * bar_width + offset
        y0 = canvas_height - height
        x1 = (i + 1) * bar_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colors[i])
    root.update()

# Sorting Algorithms
def bubble_sort(data, draw, speed):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                colors = ["blue" if x == j or x == j+1 else "red" for x in range(len(data))]
                draw(data, colors)
                time.sleep(speed)

def selection_sort(data, draw, speed):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        colors = ["blue" if x == i or x == min_idx else "red" for x in range(len(data))]
        draw(data, colors)
        time.sleep(speed)

def insertion_sort(data, draw, speed):
    n = len(data)
    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        colors = ["blue" if x == j+1 else "red" for x in range(len(data))]
        draw(data, colors)
        time.sleep(speed)

def merge_sort(data, draw, speed):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        merge_sort(left_half, draw, speed)
        merge_sort(right_half, draw, speed)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1

        draw(data, ["blue" if x >= mid else "red" for x in range(len(data))])
        time.sleep(speed)

def partition(data, low, high, draw, speed):
    i = low - 1
    pivot = data[high]

    for j in range(low, high):
        if data[j] < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
            draw(data, ["blue" if x == i or x == j else "red" for x in range(len(data))])
            time.sleep(speed)

    data[i + 1], data[high] = data[high], data[i + 1]
    draw(data, ["blue" if x == i + 1 or x == high else "red" for x in range(len(data))])
    time.sleep(speed)

    return i + 1

def quick_sort(data, low, high, draw, speed):
    if low < high:
        pi = partition(data, low, high, draw, speed)

        quick_sort(data, low, pi - 1, draw, speed)
        quick_sort(data, pi + 1, high, draw, speed)

def heapify(data, n, i, draw, speed):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[i] < data[left]:
        largest = left

    if right < n and data[largest] < data[right]:
        largest = right

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        draw(data, ["blue" if x == i or x == largest else "red" for x in range(len(data))])
        time.sleep(speed)

        heapify(data, n, largest, draw, speed)

def heap_sort(data, draw, speed):
    n = len(data)

    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i, draw, speed)

    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        draw(data, ["blue" if x == i or x == 0 else "red" for x in range(len(data))])
        time.sleep(speed)
        heapify(data, i, 0, draw, speed)

def counting_sort(data, exp, draw, speed):
    n = len(data)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = data[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = data[i] // exp
        output[count[index % 10] - 1] = data[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        data[i] = output[i]
        colors = ["blue" if x == i else "red" for x in range(len(data))]
        draw(data, colors)
        time.sleep(speed)

def radix_sort(data, draw, speed):
    max_element = max(data)
    exp = 1

    while max_element // exp > 0:
        counting_sort(data, exp, draw, speed)
        exp *= 10






# Function to start sorting with the selected algorithm
def start_sorting():
    algorithm = algorithm_var.get()
    speed = speed_var.get()

    data = generate_data()
    colors = ["red"] * len(data)
    draw_data(data, colors)

    if algorithm == "Bubble Sort":
        bubble_sort(data, draw_data, speed)
    elif algorithm == "Selection Sort":
        selection_sort(data, draw_data, speed)
    elif algorithm == "Insertion Sort":
        insertion_sort(data, draw_data, speed)
    elif algorithm == "Merge Sort":
        merge_sort(data, draw_data, speed)
    elif algorithm == "Quick Sort":
        quick_sort(data, 0, len(data) - 1, draw_data, speed)
    elif algorithm == "Heap Sort":
        heap_sort(data, draw_data, speed)
    
    elif algorithm == "Radix Sort":
        radix_sort(data, draw_data, speed)
   

# GUI setup
root = tk.Tk()
root.title("Sorting Visualizer")
root.geometry("800x600")

canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()

algorithm_var = tk.StringVar()
algorithm_var.set("Bubble Sort")
algorithm_menu = tk.OptionMenu(root, algorithm_var, "Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort","Quick Sort", "Heap Sort","Radix Sort")
algorithm_menu.pack()

speed_var = tk.DoubleVar()
speed_var.set(0.1)
speed_scale = tk.Scale(root, from_=0.01, to=1.0, resolution=0.01, length=200, orient=tk.HORIZONTAL, label="Speed", variable=speed_var)
speed_scale.pack()

start_button = tk.Button(root, text="Start Sorting", command=start_sorting)
start_button.pack()

root.mainloop()
