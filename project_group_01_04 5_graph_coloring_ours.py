from queue import PriorityQueue
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    degree: int
    node: Any=field(compare=False)

def get_graph(all_courses: dict, schedules: dict) -> dict:
    graph = dict()
    for courses in all_courses.values():
        for course in courses:
            graph[course] = set(other_course for other_course in courses
                             if other_course != course)
    
    for courses in schedules.values():
        for course in courses:
            graph[course].update(other_course for other_course in courses
                              if other_course != course)
    return graph        

def first_available_color(neighbor_color: list):
    color_set = set(neighbor_color)
    count = 0
    while True:
        if count in color_set:
            count += 1
        else:
            return count

def greedy_coloring(graph: dict) -> dict:
    color = dict()
    for node in graph:
        neighbor_color = [color[neighbor] for neighbor in graph[node]
                     if neighbor in color]
        color[node] = first_available_color(neighbor_color)
    return color

def get_degree_queue(graph: dict) -> PriorityQueue:
    degree_queue = PriorityQueue()
    for node, adj_list in zip(graph, graph.values()):
        degree_queue.put((-len(adj_list), node))
    return degree_queue


def color_non_adjacency(current, graph: dict, color: dict, color_count: int) -> None:
    for node, adj_list in graph.items():
        if node != current and node not in color:
            is_linked = False
            for neighbor in adj_list:
                if (neighbor == current or 
                   (neighbor in color and color[neighbor] == color_count)):
                    is_linked = True
                    break
            if not is_linked:
                color[node] = color_count

def graph_coloring(graph: dict) -> dict:
    degree_queue = get_degree_queue(graph)
    color = dict()
    color_count = 0
    while not degree_queue.empty():
        _, node = degree_queue.get()
        if node not in color:
            color[node] = color_count
            color_non_adjacency(node, graph, color, color_count)
            color_count += 1
    return color

def main():
    professor_courses = {'professor A': ['CS501', 'CS512'],
                         'professor B': ['CS507'],
                         'professor C': ['CS502', 'CS515'],
                         'professor D': ['CS513'],
                         'professor E': [],
                         'professor F': ['CS520']}
    student_schedules = {'student A': ['CS501', 'CS512', 'CS520'],
                         'student B': ['CS502', 'CS512', 'CS520'],
                         'student C': ['CS507', 'CS513'],
                         'student D': ['CS501', 'CS512', 'CS515']}

    graph = get_graph(professor_courses, student_schedules)
    for node, adj_list in graph.items():
        print(f'{node}:\t{adj_list}')

    print("Class-> Class V ")
    
    for lect in graph:
        print(lect, "->",  graph[lect])


    color = greedy_coloring(graph)

    print()
    print("Coloring for Class:")
    for lect_c in color:
        print("Class: "+ lect_c + " = ", color[lect_c])


if __name__ == '__main__':
    main()
