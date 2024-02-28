import time
import random
import matplotlib.pyplot as plt
import sys

# Set recursion limit to prevent RecursionError
sys.setrecursionlimit(10**6)

# Quicksort implementations
def quicksort_random(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return quicksort_random(less) + equal + quicksort_random(greater)

def quicksort_non_random(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort_non_random(less) + [pivot] + quicksort_non_random(greater)

# Benchmark function
def benchmark(sort_func, input_generator, sizes, repetitions):
    results = {}
    for size in sizes:
        total_time = 0
        for _ in range(repetitions):
            data = input_generator(size)
            start_time = time.time()
            sort_func(data)
            end_time = time.time()
            total_time += end_time - start_time
        avg_time = total_time / repetitions
        results[size] = avg_time
    return results

# Input generators
def best_case_input(size):
    return list(range(1, size + 1))

def worst_case_input(size):
    return list(range(size, 0, -1))

def average_case_input(size):
    return [random.randint(1, size) for _ in range(size)]

# Benchmark settings
input_sizes = [1000, 2000, 3000, 4000, 5000]
repetitions = 10

# Benchmarking
best_case_random_results = benchmark(quicksort_random, best_case_input, input_sizes, repetitions)
worst_case_random_results = benchmark(quicksort_random, worst_case_input, input_sizes, repetitions)
average_case_random_results = benchmark(quicksort_random, average_case_input, input_sizes, repetitions)

best_case_non_random_results = benchmark(quicksort_non_random, best_case_input, input_sizes, repetitions)
worst_case_non_random_results = benchmark(quicksort_non_random, worst_case_input, input_sizes, repetitions)
average_case_non_random_results = benchmark(quicksort_non_random, average_case_input, input_sizes, repetitions)

# Plotting the results
plt.figure(figsize=(12, 8))

plt.plot(input_sizes, list(best_case_random_results.values()), label='Best Case (Random Pivot)', marker='o')
plt.plot(input_sizes, list(worst_case_random_results.values()), label='Worst Case (Random Pivot)', marker='o')
plt.plot(input_sizes, list(average_case_random_results.values()), label='Average Case (Random Pivot)', marker='o')

plt.plot(input_sizes, list(best_case_non_random_results.values()), label='Best Case (Non-Random Pivot)', marker='o')
plt.plot(input_sizes, list(worst_case_non_random_results.values()), label='Worst Case (Non-Random Pivot)', marker='o')
plt.plot(input_sizes, list(average_case_non_random_results.values()), label='Average Case (Non-Random Pivot)', marker='o')

plt.title('Quicksort Benchmarking')
plt.xlabel('Input Size')
plt.ylabel('Average Runtime (seconds)')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()
