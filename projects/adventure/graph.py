"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def add_edge(self, exit, room="?"):
        self.edges[exit] = room

    def get_edges(self):
        return self.edges.keys()


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex.value] = vertex

    def add_edge(self, from_exit, to_exit, room="?"):
        self.vertices[from_exit.value].add_edge(to_exit.value, room)
        self.vertices[to_exit.value].add_edge(from_exit.value, room)

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        visited = set()

        # set the starting vertex
        queue.enqueue(starting_vertex)

        # while there are vertices in the queue
        while queue.size():
            # pop the first vertex in line
            current_vertex = queue.dequeue()
            # check whether it's been visited before
            if current_vertex not in visited:
                # print it
                print(current_vertex)
                # add it's neighbors (adjacent nodes) to our queue
                neighbors = self.get_neighbors(current_vertex)
                for neighbor in neighbors:
                    queue.enqueue(neighbor)
                # and add it to our visited
                visited.add(current_vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited = set()

        # set the starting vertex
        stack.push(starting_vertex)

        while stack.size():
            current_vertex = stack.pop()
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)
                neighbors = self.get_neighbors(current_vertex)
                for neighbor in neighbors:
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        if visited is None:
            visited = set()
        # add the starting vertex to visited
        visited.add(starting_vertex)
        print(starting_vertex)

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

        # stack = Stack()
        # visited = set()

        # # set the starting vertex
        # stack.push(starting_vertex)

        # # base case: stack size is empty
        # if stack.size() == 0:
        #     return

        # current_vertex = stack.pop()

        # if current_vertex not in visited:
        #     print(current_vertex)
        #     visited.add(current_vertex)
        #     for neighbor in self.get_neighbors(current_vertex):
        #         stack.push(neighbor)
        #     return self.dft_recursive(current_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        queue.enqueue([starting_vertex])
        visited = set()

        while queue.size():
            current_path = queue.dequeue()
            last_vertex = current_path[len(current_path)-1]
            if last_vertex not in visited:
                if last_vertex == destination_vertex:
                    return current_path
                visited.add(last_vertex)
                neighbors = self.get_neighbors(last_vertex)
                for neighbor in neighbors:
                    new_path = current_path.copy()
                    new_path.append(neighbor)
                    queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        stack.push([starting_vertex])
        visited = set()

        while stack.size():
            current_path = stack.pop()
            last_vertex = current_path[len(current_path)-1]
            if last_vertex not in visited:
                if last_vertex == destination_vertex:
                    return current_path
                visited.add(last_vertex)
                neighbors = self.get_neighbors(last_vertex)
                for neighbor in neighbors:
                    new_path = current_path.copy()
                    new_path.append(neighbor)
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []

        visited.add(starting_vertex)
        path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return path

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                dfs_path = self.dfs_recursive(
                    neighbor, destination_vertex, visited, path)
                if dfs_path is not None:
                    return dfs_path

        # if it doesn't find anything, return None
        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    print("DFT RECURSIVE BELOW")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
