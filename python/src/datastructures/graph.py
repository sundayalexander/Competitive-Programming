"""
General implementation of Graph data structure and algorithms.
Resources:
    https://cp-algorithms.com/graph/breadth-first-search.html#__tabbed_2_2
    https://en.wikipedia.org/wiki/Graph_algorithm
    https://www.hellointerview.com/learn/code/breadth-first-search/introduction
    https://medium.com/@rahul.singh.suny/understanding-breadth-first-search-bfs-a-comprehensive-guide-c49d5b39363c
    https://www.youtube.com/watch?v=4jyESQDrpls


BFS vs. DFS
Feature			|	Breadth-First Search (BFS)			         |   Depth-First Search (DFS)
Data Structure	|			Queue (FIFO)				         |	Stack (LIFO) or Recursion
Traversal Order	|			Layer-by-layer (horizontal)	         |		Path-by-path (vertical)
Memory Use:		|		Higher (stores entire levels)	         |		Lower (stores current path)
Best Use Case	|			Shortest path; nodes near source	 |	Deep exploration; puzzles/mazes
"""

from collections import defaultdict
from queue import Queue


def edge_list_to_adjacency_list(
    edge_list: list[tuple[str | int, str | int]], is_undirected: bool = True
) -> dict[str, list[str | int]]:
    """
    This function converts an edge list to an adjacency list.
    Args:
        edge_list (list[tuple[str|int]]): The edge list to be converted to an adjacency list.
        is_undirected (bool, optional): Whether the edge list is undirected. otherwise False (in the case fo a directed graph).

    Returns:
        dict[str, list[str]]: adjacency list.
    """
    adjacency_list = defaultdict(list)
    for from_vertex, to_vertex in edge_list:
        adjacency_list[from_vertex].append(to_vertex)
        if is_undirected:
            adjacency_list[to_vertex].append(from_vertex)

    return dict(adjacency_list)


def edge_list_to_adjacency_matrix(
    edge_list: list[tuple[int, int]],
    total_vertices: int,
    is_undirected: bool = True,
) -> list[list[str | int]]:
    """
    This function converts an edge list to an adjacency matrix.
    Args:
        edge_list (list[tuple[str|int]]): The edge list to be converted to an adjacency matrix.
        is_undirected (bool, optional): Whether the edge list is undirected. otherwise False (in the case fo a directed graph).
        total_vertices (int): The total number of vertices in the graph.

    Returns:
        dict[str, list[str]]: adjacency list.
    """
    adjacency_matrix = [[0] * total_vertices for _ in range(total_vertices)]
    for from_vertex, to_vertex in edge_list:
        adjacency_matrix[from_vertex][to_vertex] = 1
        if is_undirected:
            adjacency_matrix[to_vertex][from_vertex] = 1

    return adjacency_matrix


def bfs_adjacency_list(
    adjacency_list: dict[str, list[str]], start_vertex: str | int
) -> set[str | int]:
    """
    Implementation of breadth-first traversal of an adjacency list.
    This is for educational purposes only.

    How the Algorithm Works
    BFS relies on a Queue data structure (First-In, First-Out) to manage the order of exploration.
    This ensures that nodes closer to the starting point are processed before those further away.

    Initialization: Select a starting node, mark it as visited, and add it to the queue.
    Exploration Loop:
        While the queue is not empty:
            Remove (dequeue) the front node from the queue.
            Examine all its adjacent neighbors.
            For each neighbor that has not been visited:
                Mark it as visited.
                Add (enqueue) it to the back of the queue.
            Termination: The process continues until the queue is empty, meaning all reachable nodes have been visited.

    Core Characteristics
    Time Complexity: \(O(V + E)\), where \(V\) is the number of vertices and \(E\) is the number of edges. Each vertex and edge is processed exactly once.
    Space Complexity: \(O(V)\) in the worst case, as the queue may need to store all nodes at the widest level of the graph.
    Optimality: BFS is guaranteed to find the shortest path in an unweighted graph because it explores all paths of length \(L\) before any path of length \(L+1\).
    Completeness: It will always find a solution if one exists, even in infinite graphs (provided the branching factor is finite).

    Common Applications
    Shortest Path Discovery: Finding the minimum number of steps to reach a destination in unweighted networks or mazes.
    Social Network Analysis: Identifying "friends of friends" or calculating degrees of separation (e.g., LinkedIn connections).
    Web Crawling: Search engines use BFS to discover pages level-by-level starting from a root URL.
    Garbage Collection: Algorithms like Cheney's algorithm use BFS to identify and move reachable objects in memory.
    Networking: Broadcasting packets across all nodes in a network efficiently.

    Args:
        adjacency_list (dict[str, list[str]]): adjacency representation of a graph.
        start_vertex (str): starting vertex of the graph.

    Returns:
        list[str]: visited vertices.
    """
    visited = {start_vertex}
    vertices_queue = Queue()
    vertices_queue.put(start_vertex)
    while not vertices_queue.empty():
        current_vertex = vertices_queue.get()

        for vertex in adjacency_list.get(current_vertex) or []:
            if vertex not in visited:
                visited.add(vertex)
                vertices_queue.put(vertex)

    return visited


def bfs_adjacency_matrix(
    adjacency_matrix: list[list[int]], start_vertex: int
) -> set[int]:
    """
    A Breadth-First Traversal of an adjacency matrix.
    Args:
        adjacency_matrix (list[list[int]]): adjacency representation of a graph.
        start_vertex (int): starting vertex of the graph.
    Returns:
        list[int]: visited vertices.
    """
    visited = {start_vertex}
    vertices_queue = Queue()
    vertices_queue.put(start_vertex)
    while not vertices_queue.empty():
        current_vertex = vertices_queue.get()
        for vertex, status in enumerate(adjacency_matrix[current_vertex]):
            if status and vertex not in visited:
                visited.add(vertex)
                vertices_queue.put(vertex)

    return visited
