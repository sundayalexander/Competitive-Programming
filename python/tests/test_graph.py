import pytest

from impy.datastructures.graph import (
    bfs_adjacency_list,
    edge_list_to_adjacency_list,
    edge_list_to_adjacency_matrix,
    bfs_adjacency_matrix,
)


@pytest.mark.parametrize(
    "adjacency_list,start_vertex,expected",
    [
        (
            {
                "A": ["B", "C"],
                "B": ["A", "D", "E"],
                "C": ["A", "F"],
                "D": ["B"],
                "E": ["B", "F"],
                "F": ["C", "E"],
            },
            "A",
            {"A", "B", "C", "D", "E", "F"},
        ),
        (
            {
                "A": ["B", "C"],
                "B": ["A", "D", "E"],
                "C": ["A", "F"],
                "D": ["B"],
                "E": ["B", "F"],
                "F": ["C", "E"],
            },
            "D",
            {"A", "B", "C", "D", "E", "F"},
        ),
    ],
)
def test_bft_adjacency_list(adjacency_list, start_vertex, expected) -> None:
    assert bfs_adjacency_list(adjacency_list, start_vertex) == expected


@pytest.mark.parametrize(
    "edge_list,is_undirected_graph,expected",
    [
        (
            [(0, 1), (0, 2), (1, 3)],
            True,
            {
                0: [1, 2],
                1: [0, 3],
                2: [0],
                3: [1],
            },
        ),
        (
            [(0, 1), (0, 2), (1, 3)],
            False,
            {0: [1, 2], 1: [3]},
        ),
        (
            [("A", "B"), ("A", "C"), ("B", "D")],
            True,
            {
                "A": ["B", "C"],
                "B": ["A", "D"],
                "C": ["A"],
                "D": ["B"],
            },
        ),
    ],
)
def test_edge_list_to_adjacency_list(edge_list, is_undirected_graph, expected) -> None:
    assert edge_list_to_adjacency_list(edge_list, is_undirected_graph) == expected


@pytest.mark.parametrize(
    "edge_list,is_undirected_graph,expected, total_vertices",
    [
        (
            [(0, 1), (0, 2), (1, 3)],
            True,
            [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]],
            4,
        ),
        (
            [(0, 1), (0, 2), (1, 3)],
            False,
            [[0, 1, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]],
            4,
        ),
    ],
)
def test_edge_list_to_adjacency_matrix(
    edge_list, is_undirected_graph, expected, total_vertices
) -> None:
    assert (
        edge_list_to_adjacency_matrix(edge_list, total_vertices, is_undirected_graph)
        == expected
    )


@pytest.mark.parametrize(
    "adjacency_matrix,expected, start_vertex",
    [
        ([[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]], {0, 1, 2, 3}, 0),
        ([[0, 1, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]], {1, 3}, 1),
    ],
)
def test_bfs_adjacency_matrix(adjacency_matrix, start_vertex, expected) -> None:
    assert bfs_adjacency_matrix(adjacency_matrix, start_vertex) == expected
