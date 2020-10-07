def earliest_ancestor(ancestors, starting_node):
    ### creating the graph ###
    # create an empty dictionary as our graph
    graph = {}
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
        graph[child].add(parent)

    # searching through our graph
    # create an empty stack and an empty visited set
    stack = []

    # initialize the stack with the person we're going to search the earliest ancestor for
    stack.append([starting_node])

    # edge case: starting node has no parents
    earliest_ancestor = -1
    # keep track of the length
    max_path_length = 1

    # repeat this code as long as there are nodes in the stack
    while len(stack) > 0:
        path = stack.pop()
        last_node = path[-1]

        if len(path) > max_path_length:
            max_path_length = len(path)
            earliest_ancestor = last_node
        elif len(path) >= max_path_length and last_node < earliest_ancestor:
            max_path_length = len(path)
            earliest_ancestor = last_node

        for neighbor in graph[last_node]:
            new_path = path + [neighbor]
            stack.append(new_path)

    return earliest_ancestor


# my own testing
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 6))


# # # extra code
# if len(stack) == 2:
#     if stack[0][-1] < stack[1][-1]:
#         earliest_ancestor = stack[0][-1]
#         return earliest_ancestor
#     else:
#         earliest_ancestor = stack[1][-1]
#         return earliest_ancestor

# if len(graph[earliest_ancestor]) == 0:
#     return -1
