def build_graph(cities, storages, pipelines):
    graph = {}

    for node in cities + storages:
        graph[node] = []

    for start, end in pipelines:
        if start not in graph:
            graph[start] = []
        if end not in graph:
            graph[end] = []

        graph[start].append(end)

    return graph


def dfs(graph, start, visited):
    if start in visited:
        return

    visited.add(start)

    for neighbor in graph.get(start, []):
        dfs(graph, neighbor, visited)


def find_unreachable_cities(cities, storages, pipelines):
    graph = build_graph(cities, storages, pipelines)
    result = []

    for storage in storages:
        visited = set()
        dfs(graph, storage, visited)

        unreachable_cities = []

        for city in cities:
            if city not in visited:
                unreachable_cities.append(city)

        if unreachable_cities:
            result.append([storage, unreachable_cities])

    return result


def find_route(graph, current, target, visited, path):
    visited.add(current)
    path.append(current)

    if current == target:
        return True

    for neighbor in graph.get(current, []):
        if neighbor not in visited:
            if find_route(graph, neighbor, target, visited, path):
                return True

    path.pop()
    return False


def find_gas_route(cities, storages, pipelines, storage, city):
    graph = build_graph(cities, storages, pipelines)

    if storage not in graph or city not in graph:
        return []

    visited = set()
    path = []

    if find_route(graph, storage, city, visited, path):
        return path

    return []


if __name__ == "__main__":
    cities = ["Львів", "Стрий", "Долина"]
    storages = ["Сховище_1", "Сховище_2"]
    pipelines = [
        ["Сховище_1", "Львів"],
        ["Сховище_2", "Львів"],
        ["Львів", "Стрий"],
        ["Стрий", "Долина"],
    ]

    print("Основне завдання:")
    print(find_unreachable_cities(cities, storages, pipelines))

    print("Додаткове завдання:")
    print(
        find_gas_route(
            cities,
            storages,
            pipelines,
            "Сховище_1",
            "Долина",
        )
    )