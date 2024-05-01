import os
import math
import time

def distance(point1, point2):
    """İki nokta arasındaki mesafeyi hesaplar."""
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def greedy_tsp(coordinates):
    """Greedy Algoritması kullanarak TSP çözümü üretir."""
    n = len(coordinates)
    current_index = 0
    visited = [False] * n
    visited[current_index] = True
    total_distance = 0
    path = [current_index]

    while len(path) < n:
        nearest_distance = float('inf')
        nearest_index = None
        for i in range(n):
            if not visited[i] and i != current_index:
                d = distance(coordinates[current_index], coordinates[i])
                if d < nearest_distance:
                    nearest_distance = d
                    nearest_index = i
        visited[nearest_index] = True
        total_distance += nearest_distance
        path.append(nearest_index)
        current_index = nearest_index
    total_distance += distance(coordinates[path[-1]], coordinates[path[0]])
    return path, total_distance

def read_coordinates_from_file(file_path):
    """Dosyadan koordinatları okur."""
    coordinates = []
    with open(file_path, 'r') as file:
        next(file)  
        for line in file:
            x, y = map(float, line.split())
            coordinates.append((x, y))
    return coordinates

def process_tsp(file_paths):
    """Birden fazla dosya yolundan TSP işlemini gerçekleştirir."""
    results = {}
    for i, file_path in enumerate(file_paths, start=1):
        start_time = time.time()
        coordinates = read_coordinates_from_file(file_path)
        tsp_path, tsp_cost = greedy_tsp(coordinates)
        end_time = time.time()
        elapsed_time = end_time - start_time
        results[f"Input {i}"] = {"Path": tsp_path, "Cost": tsp_cost, "Elapsed Time": elapsed_time}
    return results

file_paths = [r"PATH 1",
              r"PATH 2",
              r"PATH 3"]

results = process_tsp(file_paths)

for input_name, result in results.items():
    print(f"{input_name}:")
    print("TSP Path:", result["Path"])
    print("TSP Cost:", result["Cost"])
    print("Elapsed Time:", result["Elapsed Time"], "seconds")
    print()
