import heapq
from datetime import timedelta

class Node:
    def __init__(self, name, cost, time):
        self.name = name
        self.cost = cost
        self.time = time

    def __lt__(self, other):
        return self.cost < other.cost

def pfp_search(start, goal, neighbors_fn, predict_fn):
    open_set = []
    heapq.heappush(open_set, (0, start, predict_fn.start_time))
    visited = set()

    while open_set:
        cost, node, t = heapq.heappop(open_set)
        if node == goal:
            print(f"Reached {goal} at time {t} with total cost {cost}")
            return True

        if node in visited:
            continue
        visited.add(node)

        for neighbor in neighbors_fn(node):
            arrival_time = t + timedelta(minutes=1)
            predicted_cost = predict_fn(neighbor, arrival_time)
            total_cost = cost + predicted_cost
            heapq.heappush(open_set, (total_cost, neighbor, arrival_time))

    print("No path found")
    return False
