BE Module 12 Lesson 8: Assignment | Graphs
Remember to take your time and work through each question diligently! Test your code, make sure it works, and try to find ways to improve. Once you are happy and satisfied with your code, upload it to Github, then turn in your Github link at the bottom of the page!


Don't forget. Make sure this assignment is in it's own repository. Not mixed in with others!

Solving Shortest Path Problem with Dijkstra's Algorithm
Objective: The objective of this assignment is to implement Dijkstra's algorithm to find the shortest path through a graph from a given source node to all other nodes.

Problem Statement: You are given a weighted graph representing a network of interconnected nodes. Your task is to implement Dijkstra's algorithm to find the shortest path from a given source node to all other nodes in the graph. The algorithm should compute the shortest path distances and paths for all nodes reachable from the source node.

Task 1: Define Graph Representation

Define a data structure to represent the weighted graph. You can use an adjacency list or any other suitable data structure to represent the graph. You can use the following example

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = {}

    def add_edge(self, source, destination, weight):
        if source in self.vertices and destination in self.vertices:
            self.vertices[source][destination] = weight
            self.vertices[destination][source] = weight  # For undirected graph

    def get_neighbors(self, vertex):
        if vertex in self.vertices:
            return self.vertices[vertex]
        else:
            return {}

# Example usage:
graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_edge('A', 'B', 5)
graph.add_edge('B', 'C', 3)
graph.add_edge('A', 'C', 10)

print(graph.vertices)  # Output: {'A': {'B': 5, 'C': 10}, 'B': {'A': 5, 'C': 3}, 'C': {'B': 3, 'A': 10}}
Task 2: Implement Dijkstra's Algorithm

Implement Dijkstra's algorithm to compute the shortest path from a given source node ( A node) to all other nodes in the graph. Ensure that your implementation correctly handles weighted edges and computes the shortest path distances and paths.

Task 3: Test the Algorithm Implementation

Test your Dijkstra's algorithm implementation with different graph configurations. Verify that the algorithm correctly computes the shortest paths from the source node to all other nodes in the graph.

Task 4: Analyze Time and Space Complexity

Analyze the time and space complexity of your Dijkstra's algorithm implementation. Provide insights into the efficiency of the algorithm and any potential optimization opportunities.

Expected Outcomes:

Upon completing this assignment, students should be able to:

Define a suitable data structure to represent the weighted graph for Dijkstra's algorithm.
Implement Dijkstra's algorithm to compute the shortest path from a given source node to all other nodes in the graph.
Test the correctness of the algorithm implementation with different graph configurations.
Analyze the time and space complexity of Dijkstra's algorithm and identify potential optimization strategies for improved performance.
NOTE: Ensure that all code in your file is ready to run. This means that if someone opens your file and clicks the run button at the top, all code executes as intended. For example, if there are if statements, print statements, or for loops, they should function correctly and display output in the console as expected. If you have a function, make sure the function is called and runs. If there are classes/objects, make sure they are instantiated and the methods are called.

The goal of this note is to ensure that all code in your Python file runs smoothly and that is has been tested.
