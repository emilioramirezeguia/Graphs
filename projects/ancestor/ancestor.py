
def earliest_ancestor(ancestors, starting_node):
    # create an empty dictionary as our graph
    graph = dict()
    # loop through ancestors
    for parent_child in ancestors:
        # for each person in a parent-child relationship
        for person in parent_child:
            # if the vertex doesn't exist for that person
            if person not in graph:
                # create a vertex in our graph and set it equal to an empty set
                graph[person] = set()
        # then add the second person as an adjacent vertex to the first person
        parent = parent_child[0]
        child = parent_child[1]
        graph[parent].add(child)

    return graph


# my own testing
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print("Graph", earliest_ancestor(test_ancestors, 3))
