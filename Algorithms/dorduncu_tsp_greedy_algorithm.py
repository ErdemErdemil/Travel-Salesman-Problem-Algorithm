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

def process_tsp(file_path):
    """Tek bir dosya yolundan TSP işlemini gerçekleştirir."""
    start_time = time.time()  
    coordinates = read_coordinates_from_file(file_path)
    tsp_path, tsp_cost = greedy_tsp(coordinates)
    end_time = time.time()  
    elapsed_time = end_time - start_time  
    result = {"Path": tsp_path, "Cost": tsp_cost, "Elapsed Time": elapsed_time}
    return result

file_path = r"PATH"

result = process_tsp(file_path)

print("TSP Path:", result["Path"])
print("TSP Cost:", result["Cost"])
print("Elapsed Time:", result["Elapsed Time"], "seconds")
