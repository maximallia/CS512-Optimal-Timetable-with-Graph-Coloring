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
    print(graph)

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
