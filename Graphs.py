import heapq  


class Graph:
    def __init__(self):
      
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = {}

    def add_edge(self, source, destination, weight):
        
        if source in self.vertices and destination in self.vertices:
         
            self.vertices[source][destination] = weight
            
            self.vertices[destination][source] = weight

    def dijkstra(self, source):
        queue = []
      
        distances = {vertex: float('inf') for vertex in self.vertices}
     
        paths = {vertex: [] for vertex in self.vertices}

       
        distances[source] = 0
        paths[source] = [source]
        
        heapq.heappush(queue, (0, source))  

        while queue: 
            
            current_distance, current_vertex = heapq.heappop(queue)

           
            if current_distance > distances[current_vertex]:
                continue

          
            for neighbor, weight in self.vertices[current_vertex].items():
                
                distance = current_distance + weight

                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance 
                    
                    paths[neighbor] = paths[current_vertex] + [neighbor]
                   
                    heapq.heappush(queue, (distance, neighbor))

     
        return distances, paths


graph = Graph()  
graph.add_vertex('A')  
graph.add_vertex('B') 
graph.add_vertex('C')

graph.add_edge('A', 'B', 5) 
graph.add_edge('B', 'C', 3)  
graph.add_edge('A', 'C', 10)


distances, paths = graph.dijkstra('A') 

print("Distances from A:", distances)  
print("Paths from A:", paths)           


graph2 = Graph()  
graph2.add_vertex('A') 
graph2.add_vertex('B') 
graph2.add_vertex('C')  
graph2.add_vertex('D')  

graph2.add_edge('A', 'B', 1)  
graph2.add_edge('A', 'C', 4) 
graph2.add_edge('B', 'C', 2)  
graph2.add_edge('B', 'D', 5)  
graph2.add_edge('C', 'D', 1)  


distances2, paths2 = graph2.dijkstra('A')  

print("Distances from A (graph 2):", distances2)  
print("Paths from A (graph 2):", paths2)          



# Time Complexity: O((M  + N) log V), M = vertices, N = Edges


# Space Complexity: O(N), N = Vertices


